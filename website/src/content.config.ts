import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const news = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/news' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    topic: z.enum(['politics', 'economy', 'tech', 'society', 'culture', 'environment', 'business', 'education']),
    country: z.string().length(2).optional(),
    source: z.string(),
    sourceUrl: z.string().url(),
    summary: z.string(),
    language: z.enum(['zh', 'en']).default('zh'),
  }),
});

export const collections = { news };
