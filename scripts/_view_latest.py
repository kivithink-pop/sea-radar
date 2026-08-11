"""临时工具：查看 latest.json 内容"""
import json
from pathlib import Path

p = Path("data/raw/latest.json")
d = json.load(p.open(encoding="utf-8"))

print(f"最新采集: {d['updated_at']}")
print(f"总条数: {d['total']}")
print(f"按国家: {d['by_country']}")
print(f"按主题: {d['by_topic']}")
print()
print("=== 前 3 条样例 ===")
for i, item in enumerate(d["items"][:3], 1):
    print(f"--- 第 {i} 条 ---")
    print(f"[{item['countryName']}] {item['title']}")
    print(f"  摘要: {item['summary'][:200]}")
    print(f"  主题: {item['topic']} | 来源: {item['source']}")
    print(f"  链接: {item['url']}")
    print()
