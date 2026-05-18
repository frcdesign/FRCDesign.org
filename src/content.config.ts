import { defineCollection } from 'astro:content';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';
import { z } from 'astro/zod';

export const collections = {
	docs: defineCollection({
		loader: docsLoader(),
		schema: docsSchema({
			extend: z.object({
				socialCard: z
					.union([
						z.boolean(),
						z.object({
							title: z.string().optional(),
							description: z.string().optional(),
							label: z.string().optional(),
							image: z.string().optional(),
							layout: z.enum(['default', 'mechanism-wide', 'mechanism-tall']).optional(),
						}),
					])
					.optional(),
				image: z.string().optional(),
			}),
		}),
	}),
};
