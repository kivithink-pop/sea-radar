/**
 * Sea Radar - 采集数据加载器
 *
 * 在 Astro 构建时读取 data/raw/latest.json，
 * 提供给所有 5 语言版本的信息流页使用。
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

function loadLatestData() {
  // 路径：website/src/lib/ -> ../../data/raw/latest.json
  const dataPath = path.resolve(__dirname, '../../../data/raw/latest.json');

  if (!fs.existsSync(dataPath)) {
    return {
      updated_at: null,
      total: 0,
      items: [],
      by_country: {},
      by_topic: {},
    };
  }

  const raw = fs.readFileSync(dataPath, 'utf-8');
  return JSON.parse(raw);
}

function loadSampleData() {
  // 加载 src/content/news/ 下的示例（手动维护的 .md 文件）
  return null;
}

export function getCollectedItems(options = {}) {
  const { limit = 100, topic = null, country = null } = options;
  const data = loadLatestData();
  let items = data.items || [];

  if (topic) {
    items = items.filter((it) => it.topic === topic);
  }
  if (country) {
    items = items.filter((it) => it.country === country);
  }

  return {
    items: items.slice(0, limit),
    total: data.total,
    updated_at: data.updated_at,
    by_country: data.by_country,
    by_topic: data.by_topic,
  };
}

export function getAllItems() {
  return loadLatestData();
}
