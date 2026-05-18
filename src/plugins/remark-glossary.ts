/**
 * Remark plugin to automatically wrap glossary terms with tooltip markup
 *
 * This scans text content and wraps matching terms in <abbr> tags
 * with the definition as the title attribute.
 */

import { visit } from 'unist-util-visit';
import type { Root, Text } from 'mdast';
import { glossaryTerms } from '../data/glossary';

// Build a case-insensitive regex pattern for all terms
// Sort by length (longest first) to match longer terms before shorter ones
const sortedTerms = [...glossaryTerms].sort((a, b) => b.term.length - a.term.length);

// Create a map for quick definition lookup
const termMap = new Map<string, string>();
glossaryTerms.forEach(({ term, definition }) => {
  termMap.set(term.toLowerCase(), definition);
});

// Build regex pattern - match whole words only
const pattern = new RegExp(
  `\\b(${sortedTerms.map(t => escapeRegex(t.term)).join('|')})\\b`,
  'gi'
);

function escapeRegex(str: string): string {
  return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

export function remarkGlossary() {
  return (tree: Root) => {
    visit(tree, 'text', (node: Text, index, parent) => {
      if (!parent || index === undefined) return;

      // Skip if inside a link, code, or already processed element
      if (
        parent.type === 'link' ||
        parent.type === 'code' ||
        parent.type === 'inlineCode' ||
        (parent as any).tagName === 'abbr' ||
        (parent as any).tagName === 'a' ||
        (parent as any).tagName === 'code'
      ) {
        return;
      }

      const text = node.value;
      const matches = [...text.matchAll(pattern)];

      if (matches.length === 0) return;

      // Build new nodes array
      const newNodes: any[] = [];
      let lastIndex = 0;

      matches.forEach((match) => {
        const matchStart = match.index!;
        const matchEnd = matchStart + match[0].length;
        const matchedTerm = match[0];
        const definition = termMap.get(matchedTerm.toLowerCase());

        // Add text before match
        if (matchStart > lastIndex) {
          newNodes.push({
            type: 'text',
            value: text.slice(lastIndex, matchStart),
          });
        }

        // Add glossary term as HTML
        newNodes.push({
          type: 'html',
          value: `<abbr class="glossary-term" title="${escapeHtml(definition || '')}">${escapeHtml(matchedTerm)}</abbr>`,
        });

        lastIndex = matchEnd;
      });

      // Add remaining text
      if (lastIndex < text.length) {
        newNodes.push({
          type: 'text',
          value: text.slice(lastIndex),
        });
      }

      // Replace the node with new nodes
      parent.children.splice(index, 1, ...newNodes);
    });
  };
}

function escapeHtml(str: string): string {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

export default remarkGlossary;
