#!/usr/bin/env python3
"""
Sea Radar - 东南亚信息采集器

每天运行一次，从 6+ 个东南亚主流媒体抓取 RSS，输出到 data/raw/YYYY-MM-DD.json
"""

import feedparser
import json
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

# === 配置 ===
ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "data" / "raw"
HOURS_LOOKBACK = int(os.environ.get("HOURS_LOOKBACK", "48"))  # 默认抓 48 小时内
MAX_PER_SOURCE = int(os.environ.get("MAX_PER_SOURCE", "20"))  # 每个源最多 20 条
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()

# === RSS 信息源 ===
RSS_SOURCES = [
    # 越南
    {"name": "Vietnam Plus", "url": "https://en.vietnamplus.vn/rss", "country": "vn", "lang": "en", "type": "综合"},
    {"name": "VNExpress International", "url": "https://e.vnexpress.net/rss", "country": "vn", "lang": "en", "type": "综合"},
    # 泰国
    {"name": "Bangkok Post", "url": "https://www.bangkokpost.com/rss/data/topstories.xml", "country": "th", "lang": "en", "type": "综合"},
    {"name": "The Nation", "url": "https://www.nationthailand.com/rss", "country": "th", "lang": "en", "type": "综合"},
    # 印尼
    {"name": "Jakarta Post", "url": "https://www.thejakartapost.com/feed", "country": "id", "lang": "en", "type": "综合"},
    {"name": "Antara News", "url": "https://en.antaranews.com/rss/news", "country": "id", "lang": "en", "type": "综合"},
    # 新加坡
    {"name": "Channel NewsAsia", "url": "https://www.channelnewsasia.com/rss", "country": "sg", "lang": "en", "type": "综合"},
    {"name": "The Straits Times", "url": "https://www.straitstimes.com/news/singapore/rss.xml", "country": "sg", "lang": "en", "type": "综合"},
    # 菲律宾
    {"name": "Inquirer", "url": "https://www.inquirer.net/fullfeed", "country": "ph", "lang": "en", "type": "综合"},
    {"name": "Rappler", "url": "https://www.rappler.com/feed/", "country": "ph", "lang": "en", "type": "综合"},
    # 马来西亚
    {"name": "The Star", "url": "https://www.thestar.com.my/rss", "country": "my", "lang": "en", "type": "综合"},
    {"name": "Malay Mail", "url": "https://www.malaymail.com/feed", "country": "my", "lang": "en", "type": "综合"},
    # 缅甸
    {"name": "The Irrawaddy", "url": "https://www.irrawaddy.com/rss.xml", "country": "mm", "lang": "en", "type": "综合"},
    # 柬埔寨
    {"name": "Khmer Times", "url": "https://www.khmertimeskh.com/feed/", "country": "kh", "lang": "en", "type": "综合"},
    # 区域
    {"name": "ASEAN Briefing", "url": "https://www.aseanbriefing.com/feed/", "country": "regional", "lang": "en", "type": "商业"},
]

# === 主题关键词（按优先级排序）===
# 检测时返回第一个匹配的主题，所以更具体的主题应放在前面
KEYWORDS = {
    "politics": [
        "election", "government", "parliament", "policy", "minister",
        "president", "vote", "law", "regulation", "diplomat",
        "court", "judge", "supreme", "party", "coalition",
        "sanction", "treaty", "summit", "protest", "opposition",
    ],
    "economy": [
        "GDP", "economy", "trade", "investment", "market",
        "inflation", "currency", "export", "import", "fiscal",
        "central bank", "monetary", "tax", "tariff", "recession",
        "GDP growth", "unemployment",
    ],
    "business": [
        "company", "acquisition", "merger", "IPO", "revenue",
        "earnings", "profit", "startup", "unicorn", "shares",
        "stock", "listed", "quarterly", "valuation", "funding",
    ],
    "tech": [
        "AI", "artificial intelligence", "machine learning",
        "technology", "tech company", "digital", "software",
        "chip", "semiconductor", "cloud", "5G", "data center",
        "blockchain", "crypto", "fintech",
    ],
    "environment": [
        "climate", "environment", "sustainability", "carbon",
        "renewable", "forest", "pollution", "flood", "deforestation",
        "wildlife", "biodiversity", "emissions", "green energy",
    ],
    "society": [
        "education", "health", "social", "community", "youth",
        "family", "culture", "tradition", "human rights", "labor",
        "worker", "women", "children", "poverty", "inequality",
    ],
}

COUNTRY_NAMES = {
    "vn": "Vietnam", "th": "Thailand", "id": "Indonesia",
    "sg": "Singapore", "ph": "Philippines", "my": "Malaysia",
    "mm": "Myanmar", "kh": "Cambodia", "la": "Laos",
    "bn": "Brunei", "tl": "Timor-Leste", "regional": "Southeast Asia",
}


def log(level: str, msg: str):
    if LOG_LEVEL == "DEBUG" or level in ("INFO", "ERROR", "WARN"):
        prefix = {"INFO": "ℹ️ ", "ERROR": "❌", "WARN": "⚠️ ", "DEBUG": "🔍"}.get(level, "  ")
        print(f"{prefix} {msg}", file=sys.stderr)


def detect_topic(text: str) -> Optional[str]:
    """根据关键词检测主题（按 KEYWORDS 顺序优先匹配，先匹配先返回）"""
    text_lower = text.lower()
    for topic, keywords in KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in text_lower:
                return topic
    return None


def clean_html(text: str, max_len: int = 400) -> str:
    """去掉 HTML 标签，截断到 max_len"""
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = (text.replace("&nbsp;", " ")
                .replace("&amp;", "&")
                .replace("&lt;", "<")
                .replace("&gt;", ">")
                .replace("&quot;", '"')
                .replace("&#39;", "'"))
    if len(text) > max_len:
        text = text[:max_len].rsplit(" ", 1)[0] + "..."
    return text


def parse_date(entry) -> Optional[datetime]:
    """解析 entry 的发布日期"""
    for attr in ("published_parsed", "updated_parsed"):
        v = getattr(entry, attr, None)
        if v:
            try:
                return datetime(*v[:6])
            except Exception:
                pass
    for attr in ("published", "updated", "created"):
        v = getattr(entry, attr, None)
        if v:
            try:
                return datetime.fromisoformat(v.replace("Z", "+00:00")).replace(tzinfo=None)
            except Exception:
                pass
    return None


def fetch_source(source: dict, cutoff: datetime) -> list:
    """从单个源抓取"""
    items = []
    try:
        log("INFO", f"📡 {source['name']} ({source['url']})")
        # 设置 User-Agent，避免被某些网站拒访
        feedparser.USER_AGENT = "SeaRadar/1.0 (+https://kivithink-pop.github.io/sea-radar/)"
        feed = feedparser.parse(source["url"], agent=feedparser.USER_AGENT)
        if feed.bozo and not feed.entries:
            bozo = feed.get("bozo_exception", "unknown")
            # 一些源返回 atom 格式但 MIME 写错，我们仍然能解析
            if "not well-formed" in str(bozo) or "not xml" in str(bozo).lower():
                log("WARN", f"  解析警告: {bozo}（继续尝试）")
            else:
                log("WARN", f"  解析失败: {bozo}")
                return items

        for entry in feed.entries[:MAX_PER_SOURCE]:
            published = parse_date(entry)
            if published and published < cutoff:
                continue

            title = clean_html(getattr(entry, "title", ""), 200)
            summary = clean_html(getattr(entry, "summary", "") or getattr(entry, "description", ""), 400)
            link = getattr(entry, "link", "")

            if not title or not link:
                continue

            full_text = f"{title} {summary}"
            topic = detect_topic(full_text)
            if not topic:
                continue

            items.append({
                "id": f"{source['country']}-{int((published or datetime.now()).timestamp())}-{abs(hash(link)) % 1000000}",
                "title": title,
                "summary": summary,
                "url": link,
                "source": source["name"],
                "country": source["country"],
                "countryName": COUNTRY_NAMES.get(source["country"], source["country"]),
                "topic": topic,
                "language": source["lang"],
                "published": published.isoformat() if published else None,
                "collected_at": datetime.now().isoformat(),
            })
        log("INFO", f"  ✓ 抓到 {len(items)} 条")
    except Exception as e:
        log("ERROR", f"  {source['name']}: {e}")
    return items


def dedupe(items: list) -> list:
    """去重（按 URL）"""
    seen = set()
    result = []
    for it in items:
        if it["url"] in seen:
            continue
        seen.add(it["url"])
        result.append(it)
    return result


def save_results(items: list, output_path: Path):
    """保存到 JSON 文件"""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 加载当日已有数据
    existing = []
    if output_path.exists():
        try:
            with open(output_path, encoding="utf-8") as f:
                existing = json.load(f)
        except Exception:
            existing = []

    # 合并去重
    existing_urls = {it["url"] for it in existing}
    new_items = [it for it in items if it["url"] not in existing_urls]
    all_items = existing + new_items

    # 按时间倒序
    all_items.sort(
        key=lambda x: x.get("published") or x.get("collected_at") or "",
        reverse=True,
    )

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_items, f, ensure_ascii=False, indent=2)

    return len(new_items), len(all_items)


def main():
    log("INFO", "🚀 Sea Radar 信息采集器启动")
    log("INFO", f"   时间窗口: {HOURS_LOOKBACK} 小时")
    log("INFO", f"   信息源数: {len(RSS_SOURCES)}")

    cutoff = datetime.now() - timedelta(hours=HOURS_LOOKBACK)
    all_items = []

    for source in RSS_SOURCES:
        all_items.extend(fetch_source(source, cutoff))

    all_items = dedupe(all_items)

    # 统计
    by_country = {}
    by_topic = {}
    for it in all_items:
        by_country[it["country"]] = by_country.get(it["country"], 0) + 1
        by_topic[it["topic"]] = by_topic.get(it["topic"], 0) + 1

    today = datetime.now().strftime("%Y-%m-%d")
    output_path = OUTPUT_DIR / f"{today}.json"

    new_count, total_count = save_results(all_items, output_path)

    log("INFO", "")
    log("INFO", f"📊 采集结果:")
    log("INFO", f"   新增: {new_count} 条")
    log("INFO", f"   当日累计: {total_count} 条")
    log("INFO", f"   按国家: {by_country}")
    log("INFO", f"   按主题: {by_topic}")
    log("INFO", f"   保存到: {output_path}")

    # 同时写一个 latest.json 方便访问
    latest_path = OUTPUT_DIR / "latest.json"
    with open(latest_path, "w", encoding="utf-8") as f:
        json.dump({
            "updated_at": datetime.now().isoformat(),
            "total": total_count,
            "items": all_items[:50],  # 最近 50 条
            "by_country": by_country,
            "by_topic": by_topic,
        }, f, ensure_ascii=False, indent=2)

    return 0


if __name__ == "__main__":
    sys.exit(main())
