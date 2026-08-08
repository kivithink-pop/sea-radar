// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://kivithink-pop.github.io',
  base: '/sea-radar',
  i18n: {
    defaultLocale: 'zh',
    locales: ['zh', 'en', 'th', 'vi', 'km'],
    routing: {
      prefixDefaultLocale: false,
    },
    fallback: {
      th: 'en',
      vi: 'en',
      km: 'en',
    },
  },
  build: {
    format: 'directory',
  },
});
