import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import remarkGlossary from './src/plugins/remark-glossary';
import remarkCenter from './src/plugins/remark-center';
import cloudflare from '@astrojs/cloudflare';
import sitemap from '@astrojs/sitemap';
import socialCards from './src/integrations/social-cards.mjs';
import { remarkMdxGlobalImports } from './src/plugins/remark-mdx-global-imports.ts';

const sitemapExcludedPaths = ['/test-content-figure/'];

export default defineConfig({
  site: 'https://frcdesign.org',
  prefetch: true,
  markdown: {
    remarkPlugins: [remarkCenter, remarkGlossary, remarkMdxGlobalImports],
    rehypePlugins: [],
  },

  integrations: [
    socialCards(),
    starlight({
      title: 'FRCDesign.org',
      logo: {
        src: './src/assets/universal/book.svg',
        alt: 'FRCDesign.org logo',
      },
      customCss: [
        './src/styles/global.css',
      ],
      components: {
        Header: './src/starlightOverrides/Header.astro',
        Footer: './src/starlightOverrides/Footer.astro',
        Sidebar: './src/starlightOverrides/Sidebar.astro',
        Pagination: './src/starlightOverrides/Pagination.astro',
        Hero: './src/starlightOverrides/Hero.astro',
        TableOfContents: './src/starlightOverrides/TableOfContents.astro',
        MobileTableOfContents: './src/starlightOverrides/MobileTableOfContents.astro',
      },
      // TOC is disabled globally but can be enabled per-directory in src/config/tocConfig.ts
      // or per-page via frontmatter (tableOfContents: true)
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
      // Sidebar configuration is now managed in src/config/sidebarConfig.ts
      // This allows different sidebars per top-level navigation section
      disable404Route: true,
    }),
    sitemap({
      filter: (page) => !sitemapExcludedPaths.includes(new URL(page).pathname),
    }),
  ],

  adapter: cloudflare({ imageService: 'compile' }),
});
