/**
 * Remark plugin to handle :::center directive blocks
 *
 * Usage in MDX:
 * :::center
 * Content to center
 * :::
 *
 * This plugin works with remark-directive (already included in Starlight)
 * to add a class to center directive containers.
 */

import { visit } from 'unist-util-visit';
import type { Root } from 'mdast';

// Define the directive node type (from remark-directive)
interface ContainerDirective {
  type: 'containerDirective';
  name: string;
  attributes?: Record<string, string>;
  children: any[];
  data?: {
    hName?: string;
    hProperties?: Record<string, any>;
  };
}

export function remarkCenter() {
  return (tree: Root) => {
    visit(tree, 'containerDirective', (node: ContainerDirective) => {
      if (node.name !== 'center') return;

      // Add data properties to control the HTML output
      node.data = node.data || {};
      node.data.hName = 'div';
      node.data.hProperties = node.data.hProperties || {};
      node.data.hProperties.class = 'centered-content';
    });
  };
}

export default remarkCenter;
