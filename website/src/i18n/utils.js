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
  const [, lang] = url.pathname.split('/');
  if (lang in languages) return lang;
  return defaultLang;
}

export function useTranslations(lang) {
  return function t(key) {
    const keys = key.split('.');
    let result = languages[lang] || languages[defaultLang];
    for (const k of keys) {
      if (result && typeof result === 'object' && k in result) {
        result = result[k];
      } else {
        // Fallback to English
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
  if (lang === defaultLang) {
    return cleanPath;
  }
  return `/${lang}${cleanPath}`;
}
