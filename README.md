# FRCDesign.org

A community-driven learning course and resource hub for FRC design and CAD, focused on Onshape. The site is built with [Astro](https://astro.build) and [Starlight](https://starlight.astro.build), and deploys with the Cloudflare adapter.

## Project Structure

```text
.
├── .github/workflows/          # GitHub Actions checks
├── public/                     # Static files served exactly by URL
├── scripts/                    # Maintenance scripts
│   └── check-local-links.mjs   # Rendered local link/asset checker
├── src/
│   ├── assets/                 # Imported theme, header, footer, and homepage assets
│   ├── components/
│   │   ├── content/            # Components used inside MDX pages
│   │   ├── general/            # Site-wide utility components
│   │   └── homepage/           # Homepage components
│   ├── config/                 # Sidebar and table-of-contents configuration
│   ├── content/docs/           # Starlight MDX documentation pages
│   ├── data/                   # Static data such as glossary terms
│   ├── plugins/                # Remark plugins
│   ├── starlightOverrides/     # Custom Starlight component overrides
│   └── styles/                 # Global CSS
├── astro.config.mjs            # Astro, Starlight, sitemap, and Cloudflare config
├── package.json
├── package-lock.json
├── tsconfig.json
└── wrangler.jsonc
```

Generated folders such as `dist/`, `.astro/`, and `node_modules/` are ignored by git.

## Content Organization

All docs live under `src/content/docs/`. Page URLs are based on the folder path and `.mdx` filename.

File naming rules:
- Use lowercase filenames.
- Use hyphens between words: `methods-of-contributing.mdx`, not `methodsofcontributing.mdx`.
- Keep `index.mdx` for section landing pages.
- Existing team/year mechanism examples use underscore-style identifiers, such as `2910_2023_dt.mdx`.

When renaming or moving a page, update:
- `src/config/sidebarConfig.ts` — controls sidebar order and labels
- Any Markdown links to the old route
- Header or navigation links if the page is a nav target

## Assets

For normal content images, place them near the page that uses them, usually in an `img/` folder beside the MDX file, and reference them with `ContentFigure`, `Slides`, or Markdown image syntax.

Use `public/` only when the browser needs to request an exact static URL, such as raw HTML `<video>` sources or files that should not go through Astro image optimization.

## Global MDX Imports

`ContentFigure`, `Aside`, `Slides`, `LinkButton`, and `ImageTable` are auto-imported into every `.mdx` file via `src/plugins/remark-mdx-global-imports.ts`. No import statement is needed to use them. To register a new global component, add it to the `GLOBAL_IMPORTS` array in that file.

Documentation for Markdown/MDX page components is maintained on the site itself in the [Adding a Page guide](https://frcdesign.org/contribution/adding-a-page/).

## Local Development

### Prerequisites

- Node.js 22 is used in CI. Node.js 18 or higher should work locally.
- Git
- A code editor such as VS Code

### Setup

```bash
git clone https://github.com/frcdesign/FRCDesign.org.git
cd FRCDesign.org
npm install
npm run dev
```

Visit [http://localhost:4321](http://localhost:4321).

## Commands

| Command | Action |
| :-- | :-- |
| `npm install` | Install dependencies |
| `npm run dev` | Start the dev server at `localhost:4321` |
| `npm run build` | Build the production site to `./dist/` |
| `npm run preview` | Preview the production build locally |
| `npm run check:links:local` | Build the site and check rendered local links/assets plus Onshape workspace-link rules |

## Link Checking

`npm run check:links:local` builds the site, serves `dist/` locally, crawls rendered same-origin links, and fails on broken local `href`, `src`, `srcset`, and `poster` URLs.

The checker also inspects `cad.onshape.com/documents/...` links. Onshape document links must use workspace URLs containing `/w/`; version URLs containing `/v/` and placeholder document links fail the check.

External links other than Onshape document shape checks are not fetched, which keeps PR checks stable.

## CI

GitHub Actions runs `.github/workflows/checks.yml` on pull requests and pushes to `main`.

The workflow:
- Installs dependencies with `npm ci`
- Runs `npm run check:links:local`

## Deployment

The site is configured for Cloudflare via `@astrojs/cloudflare` and `wrangler.jsonc`.

## Contributing

See the [Contribution Guide](https://frcdesign.org/contribution/methods-of-contributing/) on the website.

## Links

- [FRCDesign.org](https://frcdesign.org)
- [GitHub Repository](https://github.com/frcdesign/FRCDesign.org)
- [Contributor Discord Server](https://discord.gg/25pk6Mnh8k)
- [Community Discord Server](https://discord.gg/frcdesign)
