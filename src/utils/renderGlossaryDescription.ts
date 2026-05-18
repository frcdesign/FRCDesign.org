import { glossaryTerms } from '../data/glossary';

const escapeHtml = (value: string) =>
  value
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');

const escapeRegExp = (value: string) => value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

const glossaryByTerm = new Map(
  glossaryTerms.map((entry) => [entry.term.toLowerCase(), entry])
);

const glossaryPattern = new RegExp(
  `(^|[^\\w-])(${glossaryTerms
    .map((entry) => escapeRegExp(entry.term))
    .sort((a, b) => b.length - a.length)
    .join('|')})(?=$|[^\\w-])`,
  'gi'
);

export const renderGlossaryDescription = (description: string) =>
  escapeHtml(description).replace(glossaryPattern, (match, prefix, term) => {
    const entry = glossaryByTerm.get(term.toLowerCase());
    if (!entry) return match;

    return `${prefix}<span class="glossary-term" data-tooltip="${escapeHtml(entry.definition)}">${term}</span>`;
  });
