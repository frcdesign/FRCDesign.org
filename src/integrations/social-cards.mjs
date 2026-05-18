import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { generateSocialCards } from '../../scripts/social-cards.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..', '..');
const socialCardsDirName = 'social-cards';

const routeFromHtmlPath = (htmlPath, outDir) => {
  const relative = path.relative(outDir, htmlPath).replace(/\\/g, '/');
  if (relative === 'index.html') return '/';
  return `/${relative.replace(/\/index\.html$/, '/').replace(/\.html$/, '/')}`;
};

const cardFileFromRoute = (route, cardsDir) =>
  route === '/'
    ? path.join(cardsDir, 'index.png')
    : path.join(cardsDir, route.replace(/^\/|\/$/g, ''), 'index.png');

const cardPathFromRoute = (route) =>
  route === '/' ? '/social-cards/index.png' : `/social-cards${route}index.png`;

const workerEntrypointFromOutDir = (outDir) => path.join(outDir, '_worker.js', 'index.js');

const listHtmlFiles = async (dir) => {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  const files = [];

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await listHtmlFiles(fullPath)));
    } else if (entry.name.endsWith('.html')) {
      files.push(fullPath);
    }
  }

  return files;
};

const hasFile = async (filePath) => {
  try {
    await fs.access(filePath);
    return true;
  } catch {
    return false;
  }
};

const injectAfter = (html, marker, tags) => {
  if (!html.includes(marker)) return html.replace('</head>', `${tags}</head>`);
  return html.replace(marker, `${marker}${tags}`);
};

const socialTags = (imageUrl) =>
  [
    `<meta property="og:image" content="${imageUrl}">`,
    '<meta property="og:image:width" content="1200">',
    '<meta property="og:image:height" content="630">',
    '<meta property="og:image:type" content="image/png">',
    `<meta name="twitter:image" content="${imageUrl}">`,
  ].join('');

const patchCloudflareWorkerEntrypoint = async (outDir) => {
  const workerEntrypoint = workerEntrypointFromOutDir(outDir);
  if (!(await hasFile(workerEntrypoint))) return;

  const source = await fs.readFile(workerEntrypoint, 'utf8');
  if (source.includes('__frcdesignSocialCardWorker')) return;

  const exportStatement = 'export { __astrojsSsrVirtualEntry as default, pageMap };';
  if (!source.includes(exportStatement)) return;

  const wrapper = `
const __frcdesignSocialCardPathPattern = /(property="og:image"|name="twitter:image") content="(\\/social-cards\\/[^"]+)"/g;
const __frcdesignSocialCardWorker = {
\tasync fetch(request, env, context) {
\t\tconst response = await __astrojsSsrVirtualEntry.fetch(request, env, context);
\t\tconst contentType = response.headers.get('content-type') || '';

\t\tif (!contentType.includes('text/html')) {
\t\t\treturn response;
\t\t}

\t\tconst origin = new URL(request.url).origin;
\t\tconst html = await response.text();
\t\tconst updated = html.replace(__frcdesignSocialCardPathPattern, (_match, attribute, imagePath) => {
\t\t\treturn \`\${attribute} content="\${origin}\${imagePath}"\`;
\t\t});

\t\treturn new Response(updated, response);
\t},
};

export { __frcdesignSocialCardWorker as default, pageMap };`;

  await fs.writeFile(workerEntrypoint, source.replace(exportStatement, wrapper));
};

export default function socialCardsIntegration() {
  let site;
  let outDir;
  let clientOutDir;

  return {
    name: 'frcdesign-social-cards',
    hooks: {
      'astro:config:done': ({ config }) => {
        site = config.site?.toString() || 'https://frcdesign.org';
        outDir = fileURLToPath(config.outDir);
        clientOutDir = config.build.client ? fileURLToPath(config.build.client) : path.join(outDir, 'client');
      },
      'astro:build:start': async () => {
        await generateSocialCards({ site });
      },
      'astro:build:done': async () => {
        const htmlRoot = (await hasFile(clientOutDir)) ? clientOutDir : outDir;
        const cardsDir = path.join(htmlRoot, socialCardsDirName);
        const htmlFiles = await listHtmlFiles(htmlRoot);

        for (const htmlFile of htmlFiles) {
          const route = routeFromHtmlPath(htmlFile, htmlRoot);
          if (!(await hasFile(cardFileFromRoute(route, cardsDir)))) continue;

          const html = await fs.readFile(htmlFile, 'utf8');
          if (html.includes('property="og:image"') || html.includes('name="twitter:image"')) continue;

          const imageUrl = cardPathFromRoute(route);
          const updated = injectAfter(
            html,
            '<meta name="twitter:card" content="summary_large_image"/>',
            socialTags(imageUrl)
          );

          await fs.writeFile(htmlFile, updated);
        }

        await patchCloudflareWorkerEntrypoint(outDir);
      },
    },
  };
}
