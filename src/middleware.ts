import { defineMiddleware } from 'astro:middleware';

const socialCardPathPattern = /(property="og:image"|name="twitter:image") content="(\/social-cards\/[^"]+)"/g;

export const onRequest = defineMiddleware(async (context, next) => {
  const response = await next();
  const contentType = response.headers.get('content-type') || '';

  if (!contentType.includes('text/html')) {
    return response;
  }

  const origin = new URL(context.url).origin;
  const html = await response.text();
  const updated = html.replace(socialCardPathPattern, (_match, attribute, imagePath) => {
    return `${attribute} content="${origin}${imagePath}"`;
  });

  return new Response(updated, response);
});
