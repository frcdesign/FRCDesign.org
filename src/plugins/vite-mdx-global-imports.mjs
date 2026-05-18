/**
 * Vite plugin that auto-injects common component imports into every MDX file.
 * Contributors no longer need to manually import ContentFigure, Aside, Slides,
 * or LinkButton. They are available in all MDX pages automatically.
 *
 * Runs with enforce: 'pre' so it modifies the raw MDX source before Astro's
 * MDX compiler processes it. Imports are inserted after the frontmatter block
 * (between --- markers) so frontmatter always stays at the top of the file.
 * Skips injection for any component already imported to avoid duplicate errors.
 */

const GLOBAL_IMPORTS = [
  { name: 'ContentFigure', path: '@components/content/ContentFigure.astro' },
  { name: 'Aside',         path: '@components/content/Aside.astro' },
  { name: 'Slides',        path: '@components/content/Slides.astro' },
  { name: 'LinkButton',    path: '@components/content/LinkButton.astro' },
];

export function viteMdxGlobalImports() {
  return {
    name: 'vite-mdx-global-imports',
    enforce: 'pre',
    transform(code, id) {
      // Strip query params (e.g. ?astro&type=content) before checking extension
      const filePath = id.split('?')[0];
      if (!filePath.endsWith('.mdx')) return null;

      const toInject = GLOBAL_IMPORTS
        .filter(({ name }) => !new RegExp(`\\bimport\\s+${name}\\s+from\\b`).test(code))
        .map(({ name, path }) => `import ${name} from '${path}';`)
        .join('\n');

      if (!toInject) return null;

      // Frontmatter must stay at the very top of the file. Insert imports
      // immediately after the closing --- so MDX sees them as ESM imports.
      const frontmatterMatch = code.match(/^(?:﻿)?---[\s\S]*?---\r?\n/);
      if (frontmatterMatch) {
        const insertAt = frontmatterMatch.index + frontmatterMatch[0].length;
        return {
          code: code.slice(0, insertAt) + toInject + '\n' + code.slice(insertAt),
          map: null,
        };
      }

      // No frontmatter block, just insert at the top
      return { code: `${toInject}\n${code}`, map: null };
    },
  };
}
