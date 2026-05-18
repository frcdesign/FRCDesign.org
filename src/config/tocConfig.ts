/**
 * Table of Contents configuration per directory
 *
 * This config allows enabling TOC for entire directories without
 * adding frontmatter to each individual page.
 *
 * Priority order:
 * 1. Frontmatter `tableOfContents: false` - always hides TOC
 * 2. Frontmatter `tableOfContents: true` - always shows TOC
 * 3. Directory config (this file) - shows TOC for matching paths
 *
 * Usage:
 * - Add a path prefix to enable TOC for all pages under that path
 * - Use `true` for default heading levels (h2-h3)
 * - Use `{ minHeadingLevel: 2, maxHeadingLevel: 4 }` for custom levels
 */

export interface TocConfig {
  minHeadingLevel?: number;
  maxHeadingLevel?: number;
}

/**
 * Directories where TOC should be enabled
 * Use path prefixes - they match all pages starting with that path
 *
 * Examples:
 *   '/design-handbook': true                           // Enable for all design handbook pages
 *   '/best-practices': { minHeadingLevel: 2, maxHeadingLevel: 4 }  // Custom levels
 */
export const tocEnabledDirectories: Record<string, TocConfig | true> = {
  // Add directories here to enable TOC
  '/design-handbook': true,
  // '/best-practices': true,
};

/**
 * Check if TOC should be enabled for a given path
 * Returns the config if enabled, or false if not in any enabled directory
 */
export function getTocConfigForPath(pathname: string): TocConfig | false {
  // Normalize pathname
  const normalizedPath = pathname.endsWith('/') ? pathname.slice(0, -1) : pathname;

  // Check for exact match first
  if (tocEnabledDirectories[normalizedPath]) {
    const config = tocEnabledDirectories[normalizedPath];
    return config === true ? {} : config;
  }

  // Find the longest matching prefix
  let bestMatch = '';
  let bestConfig: TocConfig | true | undefined;

  for (const [key, config] of Object.entries(tocEnabledDirectories)) {
    if (normalizedPath.startsWith(key) && key.length > bestMatch.length) {
      bestMatch = key;
      bestConfig = config;
    }
  }

  if (bestMatch && bestConfig) {
    return bestConfig === true ? {} : bestConfig;
  }

  return false;
}
