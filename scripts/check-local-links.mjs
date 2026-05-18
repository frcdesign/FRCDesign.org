import { spawn } from 'node:child_process';
import { createServer } from 'node:http';
import { extname, join, normalize } from 'node:path';
import { readFile, stat } from 'node:fs/promises';

const host = '127.0.0.1';
const requestedPort = Number(process.env.LINK_CHECK_PORT || '0');
let origin;
const startPath = '/';
const requestTimeoutMs = 15_000;
const astroEntry = join(process.cwd(), 'node_modules', 'astro', 'bin', 'astro.mjs');
const distDir = join(process.cwd(), 'dist', 'client');

const skippedProtocols = new Set(['data:', 'mailto:', 'tel:', 'javascript:']);
const checked = new Set();
const crawled = new Set();
const broken = [];
const invalidOnshapeLinks = [];
const seenOnshapeLinks = new Set();
const queue = [];

if (process.env.LINK_CHECK_SKIP_BUILD === '1') {
  console.log('Skipping build because LINK_CHECK_SKIP_BUILD=1.');
} else {
  await runAstroBuild();
}

const server = createStaticServer();
await listen(server);
queue.push(new URL(startPath, origin).href);

try {
  await crawlSite();
} finally {
  server.close();
}

if (broken.length > 0 || invalidOnshapeLinks.length > 0) {
  if (invalidOnshapeLinks.length > 0) {
    console.error(`\nFound ${invalidOnshapeLinks.length} Onshape link(s) that are not workspace links:`);
    for (const item of invalidOnshapeLinks) {
      console.error(`- ${item.url}`);
      console.error(`  linked from ${item.from}`);
      console.error('  Onshape document links must use /w/ workspace URLs, not /v/ version URLs.');
    }
  }

  if (broken.length > 0) {
    console.error(`\nFound ${broken.length} broken local link(s):`);
    for (const item of broken) {
      console.error(`- ${item.status} ${item.url}`);
      console.error(`  linked from ${item.from}`);
    }
  }
  process.exit(1);
}

console.log(`Checked ${checked.size} local URL(s); no broken local links found.`);

async function crawlSite() {
  while (queue.length > 0) {
    const pageUrl = queue.shift();
    if (!pageUrl || crawled.has(pageUrl)) continue;
    crawled.add(pageUrl);

    const response = await checkUrl(pageUrl, pageUrl, { crawl: true });
    if (!response || !isHtml(response)) continue;

    const html = await response.text();
    for (const link of extractLocalUrls(html, response.url)) {
      const checkResponse = await checkUrl(link.url, pageUrl);
      if (checkResponse && isHtml(checkResponse) && !crawled.has(link.url)) {
        queue.push(link.url);
      }
    }
  }
}

async function checkUrl(url, from, options = {}) {
  const normalized = normalizeLocalUrl(url, from);
  if (!normalized || (!options.crawl && checked.has(normalized))) return null;

  checked.add(normalized);

  try {
    const method = options.crawl ? 'GET' : 'HEAD';
    let response = await fetchWithTimeout(normalized, { method }, requestTimeoutMs);

    if (!options.crawl && response.status === 405) {
      response = await fetchWithTimeout(normalized, { method: 'GET' }, requestTimeoutMs);
    }

    if (!response.ok) {
      broken.push({ url: normalized, from, status: response.status });
      return null;
    }

    return response;
  } catch (error) {
    broken.push({
      url: normalized,
      from,
      status: error instanceof Error ? error.message : 'request failed',
    });
    return null;
  }
}

function extractLocalUrls(html, baseUrl) {
  html = html
    .replaceAll(/<script\b[\s\S]*?<\/script>/gi, '')
    .replaceAll(/<style\b[\s\S]*?<\/style>/gi, '')
    .replaceAll(/<template\b[\s\S]*?<\/template>/gi, '')
    .replaceAll(/<pre\b[\s\S]*?<\/pre>/gi, '')
    .replaceAll(/<code\b[\s\S]*?<\/code>/gi, '');

  const urls = [];
  const attrPattern = /\s(?:href|src|poster)=["']([^"']+)["']/gi;
  const srcsetPattern = /\ssrcset=["']([^"']+)["']/gi;

  for (const match of html.matchAll(attrPattern)) {
    const rawUrl = decodeHtml(match[1]);
    checkOnshapeLink(rawUrl, baseUrl);
    const url = normalizeLocalUrl(rawUrl, baseUrl);
    if (url) urls.push({ url });
  }

  for (const match of html.matchAll(srcsetPattern)) {
    for (const candidate of decodeHtml(match[1]).split(',')) {
      const urlPart = candidate.trim().split(/\s+/)[0];
      checkOnshapeLink(urlPart, baseUrl);
      const url = normalizeLocalUrl(urlPart, baseUrl);
      if (url) urls.push({ url });
    }
  }

  return urls;
}

function checkOnshapeLink(rawUrl, baseUrl) {
  if (!rawUrl) return;

  let parsed;
  try {
    parsed = new URL(rawUrl, baseUrl);
  } catch {
    return;
  }

  if (parsed.hostname !== 'cad.onshape.com') return;
  if (!parsed.pathname.startsWith('/documents/')) return;
  if (parsed.pathname.includes('/w/') && !parsed.pathname.includes('/v/')) return;

  const key = `${parsed.href}\n${baseUrl}`;
  if (seenOnshapeLinks.has(key)) return;

  seenOnshapeLinks.add(key);
  invalidOnshapeLinks.push({
    url: parsed.href,
    from: baseUrl,
  });
}

function normalizeLocalUrl(rawUrl, baseUrl) {
  if (!rawUrl || rawUrl.startsWith('#')) return null;

  let parsed;
  try {
    parsed = new URL(rawUrl, baseUrl);
  } catch {
    return null;
  }

  if (skippedProtocols.has(parsed.protocol)) return null;
  if (parsed.origin !== origin) return null;
  if (parsed.pathname === '/_image') return null;

  parsed.hash = '';
  return parsed.href;
}

function isHtml(response) {
  return response.headers.get('content-type')?.includes('text/html');
}

function fetchWithTimeout(url, options, timeoutMs) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), timeoutMs);

  return fetch(url, {
    ...options,
    redirect: 'follow',
    signal: controller.signal,
  }).finally(() => clearTimeout(timeout));
}

function decodeHtml(value) {
  return value
    .replaceAll(/&#x([0-9a-f]+);/gi, (_, hex) => String.fromCodePoint(Number.parseInt(hex, 16)))
    .replaceAll(/&#([0-9]+);/g, (_, decimal) => String.fromCodePoint(Number.parseInt(decimal, 10)))
    .replaceAll('&amp;', '&')
    .replaceAll('&quot;', '"')
    .replaceAll('&#39;', "'")
    .replaceAll('&lt;', '<')
    .replaceAll('&gt;', '>');
}

async function runAstroBuild() {
  console.log('Building site before checking local links...');

  const build = spawn(process.execPath, [astroEntry, 'build'], {
    env: {
      ...process.env,
      ASTRO_TELEMETRY_DISABLED: '1',
    },
    stdio: ['ignore', 'pipe', 'pipe'],
  });

  let output = '';
  build.stdout.on('data', (chunk) => {
    output += chunk.toString();
  });
  build.stderr.on('data', (chunk) => {
    output += chunk.toString();
  });

  const exitCode = await new Promise((resolve) => {
    build.on('close', resolve);
  });

  if (exitCode !== 0) {
    throw new Error(`astro build failed before link checking.\n${output}`);
  }
}

function createStaticServer() {
  return createServer(async (request, response) => {
    const redirect = await trailingSlashRedirect(request.url || '/');
    if (redirect) {
      response.writeHead(301, { location: redirect });
      response.end();
      return;
    }

    const filePath = await resolveDistPath(request.url || '/');

    if (!filePath) {
      response.writeHead(404);
      response.end();
      return;
    }

    response.writeHead(200, {
      'content-type': contentType(filePath),
    });

    if (request.method === 'HEAD') {
      response.end();
      return;
    }

    response.end(await readFile(filePath));
  });
}

async function trailingSlashRedirect(requestUrl) {
  const url = new URL(requestUrl, origin);
  if (url.pathname.endsWith('/') || extname(url.pathname)) return null;

  const relativePath = normalize(decodeURIComponent(url.pathname)).replace(/^[/\\]+/, '');
  if (relativePath.startsWith('..')) return null;

  const directoryPath = join(distDir, relativePath);
  const indexPath = join(directoryPath, 'index.html');

  try {
    const [directoryInfo, indexInfo] = await Promise.all([stat(directoryPath), stat(indexPath)]);
    if (directoryInfo.isDirectory() && indexInfo.isFile()) {
      url.pathname += '/';
      return url.pathname + url.search;
    }
  } catch {
    return null;
  }

  return null;
}

function listen(server) {
  return new Promise((resolve, reject) => {
    server.once('error', reject);
    server.listen(requestedPort, host, () => {
      server.off('error', reject);
      const address = server.address();
      const actualPort = typeof address === 'object' && address ? address.port : requestedPort;
      origin = `http://${host}:${actualPort}`;
      resolve();
    });
  });
}

async function resolveDistPath(requestUrl) {
  const url = new URL(requestUrl, origin);
  const pathname = decodeURIComponent(url.pathname);
  const relativePath = normalize(pathname).replace(/^[/\\]+/, '');

  if (relativePath.startsWith('..')) return null;

  const directPath = join(distDir, relativePath);
  const direct = await fileIfExists(directPath);
  if (direct) return direct;

  const indexPath = join(directPath, 'index.html');
  const index = await fileIfExists(indexPath);
  if (index) return index;

  return null;
}

async function fileIfExists(filePath) {
  try {
    const info = await stat(filePath);
    if (info.isDirectory()) {
      return fileIfExists(join(filePath, 'index.html'));
    }
    return info.isFile() ? filePath : null;
  } catch {
    return null;
  }
}

function contentType(filePath) {
  switch (extname(filePath).toLowerCase()) {
    case '.html':
      return 'text/html; charset=utf-8';
    case '.css':
      return 'text/css; charset=utf-8';
    case '.js':
    case '.mjs':
      return 'text/javascript; charset=utf-8';
    case '.json':
      return 'application/json; charset=utf-8';
    case '.svg':
      return 'image/svg+xml';
    case '.png':
      return 'image/png';
    case '.jpg':
    case '.jpeg':
      return 'image/jpeg';
    case '.webp':
      return 'image/webp';
    case '.webm':
      return 'video/webm';
    case '.mp4':
      return 'video/mp4';
    case '.xml':
      return 'application/xml; charset=utf-8';
    default:
      return 'application/octet-stream';
  }
}
