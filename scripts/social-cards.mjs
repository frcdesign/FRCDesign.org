import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import sharp from 'sharp';
import yaml from 'js-yaml';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..');
const docsDir = path.join(rootDir, 'src', 'content', 'docs');
const publicDir = path.join(rootDir, 'public');
const publicCardsDir = path.join(rootDir, 'public', 'social-cards');
const layoutAssetsDir = path.join(rootDir, 'src', 'assets', 'social-card-layouts');
const defaultSite = 'https://frcdesign.org';
const width = 1200;
const height = 630;
const siteName = 'FRCDesign.org';
const siteDescription = 'FRC robot design and CAD resources for students, mentors, and teams.';

const escapeHtml = (value = '') =>
  String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');

const slugify = (value) =>
  value
    .toLowerCase()
    .replace(/\\/g, '/')
    .replace(/\.[^.]+$/, '')
    .replace(/\/index$/, '')
    .replace(/^index$/, '')
    .replace(/[^a-z0-9/_-]+/g, '-')
    .replace(/\/+/g, '/')
    .replace(/^-+|-+$/g, '');

const routeFromFile = (filePath) => {
  const relative = path.relative(docsDir, filePath).replace(/\\/g, '/');
  const slug = slugify(relative);
  return slug ? `/${slug}/` : '/';
};

const cardPathFromRoute = (route) =>
  route === '/'
    ? path.join(publicCardsDir, 'index.png')
    : path.join(publicCardsDir, route.replace(/^\/|\/$/g, ''), 'index.png');

const cardUrlFromRoute = (route, site = defaultSite) => {
  const cardPath = route === '/' ? '/social-cards/index.png' : `/social-cards${route}index.png`;
  return new URL(cardPath, site).href;
};

const parseFrontmatter = (source) => {
  const cleanSource = source.replace(/^\uFEFF/, '');
  const match = cleanSource.match(/^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/);
  if (!match) return {};
  return yaml.load(match[1]) || {};
};

const listContentFiles = async (dir) => {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  const files = [];

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await listContentFiles(fullPath)));
    } else if (/\.(md|mdx)$/.test(entry.name)) {
      files.push(fullPath);
    }
  }

  return files;
};

const splitLongWord = (word, maxChars) => {
  const parts = [];
  for (let index = 0; index < word.length; index += maxChars) {
    parts.push(word.slice(index, index + maxChars));
  }
  return parts;
};

const wrapText = (text, maxChars, maxLines) => {
  const words = String(text || '').trim().split(/\s+/).flatMap((word) =>
    word.length > maxChars ? splitLongWord(word, maxChars) : word
  );
  const lines = [];
  let current = '';

  for (const word of words) {
    const next = current ? `${current} ${word}` : word;
    if (next.length <= maxChars) {
      current = next;
      continue;
    }

    if (current) lines.push(current);
    current = word;
    if (lines.length === maxLines) break;
  }

  if (current && lines.length < maxLines) lines.push(current);
  if (words.length && lines.length === maxLines) {
    const original = words.join(' ');
    if (lines.join(' ').length < original.length) {
      lines[maxLines - 1] = `${lines[maxLines - 1].replace(/[.,;:!?-]*$/, '')}...`;
    }
  }

  return lines;
};

const fontSizeForLines = (lines, base, min) => Math.max(min, base - Math.max(0, lines.length - 1) * 8);

const renderBookLogo = (x, y, size) => `
  <svg x="${x}" y="${y}" width="${size}" height="${size}" viewBox="0 0 576 512">
    <path fill="#ffffff" d="M249.6 471.5c10.8 3.8 22.4-4.1 22.4-15.5V78.6c0-4.2-1.6-8.4-5-11C247.4 52 202.4 32 144 32C87.5 32 35.1 48.6 9 59.9c-5.6 2.4-9 8-9 14V454.1c0 11.9 12.8 20.2 24.1 16.5C55.6 460.1 105.5 448 144 448c33.9 0 79 14 105.6 23.5zm76.8 0C353 462 398.1 448 432 448c38.5 0 88.4 12.1 119.9 22.6c11.3 3.8 24.1-4.6 24.1-16.5V73.9c0-6.1-3.4-11.6-9-14C540.9 48.6 488.5 32 432 32c-58.4 0-103.4 20-123 35.6c-3.3 2.6-5 6.8-5 11V456c0 11.4 11.7 19.3 22.4 15.5z"/>
  </svg>`;

const renderTextLines = ({ lines, x, y, fontSize, lineHeight = 1.25, weight = 700, color = '#ffffff' }) =>
  lines
    .map(
      (line, index) =>
        `<text x="${x}" y="${y + index * fontSize * lineHeight}" fill="${color}" font-family="Roboto, Arial, sans-serif" font-size="${fontSize}" font-weight="${weight}" letter-spacing="0">${escapeHtml(line)}</text>`
    )
    .join('\n  ');

const descriptionBox = { left: 30, top: 410, width: 730, height: 186, radius: 42 };

const renderDescriptionBoxSvg = (description) => {
  const descriptionLines = wrapText(description, 44, 3);
  const labelFontSize = 34;
  const descriptionFontSize = 22;
  const descriptionLineHeight = 1.08;
  const labelDescriptionGap = 18;
  const descriptionBlockHeight =
    descriptionFontSize + Math.max(0, descriptionLines.length - 1) * descriptionFontSize * descriptionLineHeight;
  const contentHeight = labelFontSize + labelDescriptionGap + descriptionBlockHeight;
  const contentTop = (descriptionBox.height - contentHeight) / 2;
  const labelBaseline = contentTop + labelFontSize;
  const descriptionBaseline = contentTop + labelFontSize + labelDescriptionGap + descriptionFontSize;

  return `<svg width="${descriptionBox.width}" height="${descriptionBox.height}" viewBox="0 0 ${descriptionBox.width} ${descriptionBox.height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="description-box-clip">
      <rect x="3" y="3" width="${descriptionBox.width - 6}" height="${descriptionBox.height - 6}" rx="${descriptionBox.radius - 3}"/>
    </clipPath>
  </defs>
  <rect x="3" y="3" width="${descriptionBox.width - 6}" height="${descriptionBox.height - 6}" rx="${descriptionBox.radius - 3}" fill="#1b2028" stroke="#4d5662" stroke-width="6"/>
  <g clip-path="url(#description-box-clip)">
    ${renderTextLines({ lines: [siteName], x: 56, y: labelBaseline, fontSize: labelFontSize, weight: 700 })}
    ${renderTextLines({ lines: descriptionLines, x: 56, y: descriptionBaseline, fontSize: descriptionFontSize, lineHeight: descriptionLineHeight, weight: 400 })}
  </g>
</svg>`;
};

const renderDefaultTextSvg = ({ title, description }) => {
  const titleLines = wrapText(title, 20, 2);
  const titleFontSize = fontSizeForLines(titleLines, 76, 60);

  return `<svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg">
  ${renderBookLogo(992, 64, 144)}
  ${renderTextLines({ lines: titleLines, x: 62, y: 172, fontSize: titleFontSize, weight: 700 })}
</svg>`;
};

const renderMechanismTextSvg = ({ title, description, layout }) => {
  const isTall = layout === 'mechanism-tall';
  const titleLines = wrapText(title, isTall ? 24 : 21, isTall ? 2 : 3);
  const titleFontSize = fontSizeForLines(titleLines, isTall ? 72 : 64, isTall ? 60 : 52);

  return `<svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg">
  ${renderTextLines({ lines: titleLines, x: 62, y: isTall ? 172 : 136, fontSize: titleFontSize, weight: 700 })}
  ${isTall ? '' : renderBookLogo(1036, 498, 100)}
</svg>`;
};

const inferLayout = (route, frontmatter, socialCard, image) => {
  if (socialCard.layout) return socialCard.layout;
  if (route === '/mechanism-examples/') return 'default';
  if (route.startsWith('/mechanism-examples/elevator/')) return 'mechanism-tall';
  if (route.startsWith('/mechanism-examples/') && image) return 'mechanism-wide';
  if (frontmatter.image || socialCard.image) return 'mechanism-wide';
  return 'default';
};

const assetPath = (name) => path.join(layoutAssetsDir, name);

const imageExists = async (imagePath) => {
  try {
    const stat = await fs.stat(imagePath);
    return stat.isFile();
  } catch {
    return false;
  }
};

const resolveImagePath = async (imageValue, sourceFile) => {
  if (!imageValue || typeof imageValue !== 'string') return undefined;

  const normalized = imageValue.replace(/\\/g, '/').replace(/^@fs\//, '');
  const candidates = [];

  if (path.isAbsolute(normalized)) {
    candidates.push(normalized);
  } else if (normalized.startsWith('/')) {
    candidates.push(path.join(publicDir, normalized));
    candidates.push(path.join(rootDir, normalized));
  } else {
    candidates.push(path.resolve(path.dirname(sourceFile), normalized));
    candidates.push(path.resolve(rootDir, normalized));
    candidates.push(path.resolve(publicDir, normalized));
  }

  for (const candidate of candidates) {
    if (await imageExists(candidate)) return candidate;
  }

  return undefined;
};

const inferContentImage = (source) => {
  const patterns = [
    /socialCard:\s*[\s\S]*?\n\s+image:\s*['"]?([^'"\n]+)['"]?/,
    /^image:\s*['"]?([^'"\n]+)['"]?/m,
    /<ContentFigure[^>]*\ssrc=["']([^"']+)["']/,
    /import\s+\w+\s+from\s+['"]([^'"]*\.(?:png|jpe?g|webp|svg))['"]/,
    /!\[[^\]]*]\(([^)]+\.(?:png|jpe?g|webp|svg))\)/,
  ];

  for (const pattern of patterns) {
    const match = source.match(pattern);
    if (match) return match[1].trim();
  }

  return undefined;
};

const mechanismImageLayer = async (card) => {
  if (!card.imagePath) return undefined;

  const isTall = card.layout === 'mechanism-tall';
  const box = isTall
    ? { width: 278, height: 430, left: 842, top: 100 }
    : { width: 500, height: 324, left: 660, top: 60 };

  const input = await sharp(card.imagePath)
    .trim({ threshold: 10 })
    .resize(box.width, box.height, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
    .png()
    .toBuffer();

  return { input, left: box.left, top: box.top };
};

const renderCard = async (card, outputPath) => {
  const base = sharp({
    create: {
      width,
      height,
      channels: 4,
      background: '#54AC58',
    },
  });

  const layers = [];

  if (card.layout === 'default') {
    layers.push(
      { input: assetPath('cornerCircles.png'), left: 850, top: 280 },
      { input: assetPath('bubbles.png'), left: 0, top: 0 },
      { input: Buffer.from(renderDescriptionBoxSvg(card.description)), left: descriptionBox.left, top: descriptionBox.top },
      { input: Buffer.from(renderDefaultTextSvg(card)), left: 0, top: 0 }
    );
  } else {
    const imageLayer = await mechanismImageLayer(card);
    layers.push(
      { input: assetPath('wavyBorder.png'), left: 0, top: 0 },
      imageLayer || { input: assetPath('transparentImage.png'), left: 0, top: 0 },
      { input: Buffer.from(renderDescriptionBoxSvg(card.description)), left: descriptionBox.left, top: descriptionBox.top },
      { input: Buffer.from(renderMechanismTextSvg(card)), left: 0, top: 0 }
    );
  }

  await base
    .composite(layers.filter(Boolean))
    .png({ compressionLevel: 9 })
    .toFile(outputPath);
};

const getCardData = async ({ frontmatter, route, source, file }) => {
  if (frontmatter.socialCard === false) return undefined;
  const socialCard = typeof frontmatter.socialCard === 'object' ? frontmatter.socialCard : {};
  const title = socialCard.title || frontmatter.title;
  if (!title) return undefined;
  const image = socialCard.image || frontmatter.image || inferContentImage(source);
  const imagePath = await resolveImagePath(image, file);
  const layout = inferLayout(route, frontmatter, socialCard, imagePath);

  return {
    route,
    title,
    description:
      socialCard.description ||
      frontmatter.description ||
      siteDescription,
    imagePath,
    layout,
  };
};

export async function generateSocialCards(options = {}) {
  const site = options.site || defaultSite;
  const outDir = options.outDir || publicCardsDir;
  const files = await listContentFiles(docsDir);
  const cards = [];

  await fs.mkdir(outDir, { recursive: true });

  for (const file of files) {
    const source = await fs.readFile(file, 'utf8');
    const frontmatter = parseFrontmatter(source);
    const route = routeFromFile(file);
    const card = await getCardData({ frontmatter, route, source, file });
    if (!card) continue;

    const outputPath =
      route === '/'
        ? path.join(outDir, 'index.png')
        : path.join(outDir, route.replace(/^\/|\/$/g, ''), 'index.png');

    await fs.mkdir(path.dirname(outputPath), { recursive: true });
    await renderCard(card, outputPath);

    cards.push({
      ...card,
      file: outputPath,
      imageUrl: cardUrlFromRoute(route, site),
    });
  }

  return cards;
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const cards = await generateSocialCards();
  console.log(`Generated ${cards.length} social cards.`);
}
