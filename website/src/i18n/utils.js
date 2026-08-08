import en from './en.json';
import zh from './zh.json';
import th from './th.json';
import vi from './vi.json';
import km from './km.json';

export const languages = {
  en,
  zh,
  th,
  vi,
  km,
};

export const defaultLang = 'zh';
export const basePath = '/sea-radar';

export const ui = languages;

export const localeNames = {
  en: 'English',
  zh: '简体中文',
  th: 'ไทย',
  vi: 'Tiếng Việt',
  km: 'ភាសាខ្មែរ',
};

export const localeFlags = {
  en: '🇺🇸',
  zh: '🇨🇳',
  th: '🇹🇭',
  vi: '🇻🇳',
  km: '🇰🇭',
};

export function getLocaleFromUrl(url) {
  const pathname = url.pathname;

  const cleanPath = pathname.startsWith(basePath)
    ? pathname.slice(basePath.length)
    : pathname;

  const segments = cleanPath.split('/').filter(Boolean);
  const first = segments[0];

  if (first && first in languages) {
    return first;
  }
  return defaultLang;
}

export function getPathWithoutLocale(url) {
  const pathname = url.pathname;
  const cleanPath = pathname.startsWith(basePath)
    ? pathname.slice(basePath.length)
    : pathname;
  const segments = cleanPath.split('/').filter(Boolean);
  if (segments.length > 0 && segments[0] in languages) {
    return '/' + segments.slice(1).join('/');
  }
  return cleanPath || '/';
}

export function useTranslations(lang) {
  return function t(key) {
    const keys = key.split('.');
    let result = languages[lang] || languages[defaultLang];
    for (const k of keys) {
      if (result && typeof result === 'object' && k in result) {
        result = result[k];
      } else {
        result = languages.en;
        for (const k2 of keys) {
          if (result && typeof result === 'object' && k2 in result) {
            result = result[k2];
          } else {
            return key;
          }
        }
        return result;
      }
    }
    return result;
  };
}

export function getLocalizedPath(path, lang) {
  const cleanPath = path.startsWith('/') ? path : `/${path}`;
  const normalized = cleanPath === '/' ? '/' : cleanPath.replace(/\/$/, '');
  const langPrefix = lang === defaultLang ? '' : `/${lang}`;
  return `${basePath}${langPrefix}${normalized === '/' ? '/' : normalized}`;
}
