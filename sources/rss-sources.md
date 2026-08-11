# 东南亚主流信息源 RSS 订阅

每个国家选择 1-3 个主流媒体作为信息源。优先选择：RSS 稳定、内容质量高、有英文版。

## 越南 Vietnam 🇻🇳

- **Vietnam Plus（VNA 英文）** — 官方通讯社
  - URL: https://en.vietnamplus.vn/rss
  - 类型: 综合
- **VNExpress** — 最大私营媒体
  - URL: https://vnexpress.net/rss
  - 类型: 综合
- **VnEconomy** — 经济专刊
  - URL: https://vneconomy.vn/rss
  - 类型: 经济

## 泰国 Thailand 🇹🇭

- **Bangkok Post** — 英文老牌媒体
  - URL: https://www.bangkokpost.com/rss/data/topstories.xml
  - 类型: 综合
- **The Nation** — 泰英文双语
  - URL: https://www.nationthailand.com/rss
  - 类型: 综合
- **Thai PBS World** — 公共广播
  - URL: https://www.thaipbsworld.com/feed/
  - 类型: 社会/政治

## 印度尼西亚 Indonesia 🇮🇩

- **Jakarta Post** — 英文旗舰媒体
  - URL: https://www.thejakartapost.com/feed
  - 类型: 综合
- **Antara News** — 官方通讯社
  - URL: https://en.antaranews.com/rss/news
  - 类型: 综合
- **Tempo.co** — 调查性新闻
  - URL: https://en.tempo.co/rss
  - 类型: 政治/调查

## 新加坡 Singapore 🇸🇬

- **Channel NewsAsia** — 区域旗舰
  - URL: https://www.channelnewsasia.com/rss
  - 类型: 综合
- **The Straits Times** — 主流大报
  - URL: https://www.straitstimes.com/news/singapore/rss.xml
  - 类型: 综合

## 菲律宾 Philippines 🇵🇭

- **Inquirer** — 主流大报
  - URL: https://www.inquirer.net/fullfeed
  - 类型: 综合
- **Rappler** — 数字原生媒体
  - URL: https://www.rappler.com/feed/
  - 类型: 综合
- **Philippine Daily Inquirer - Business**
  - URL: https://business.inquirer.net/feed
  - 类型: 经济

## 马来西亚 Malaysia 🇲🇾

- **The Star** — 最大英文报
  - URL: https://www.thestar.com.my/rss
  - 类型: 综合
- **Malay Mail** — 主流媒体
  - URL: https://www.malaymail.com/feed
  - 类型: 综合
- **New Straits Times** — 主流大报
  - URL: https://www.nst.com.my/rss
  - 类型: 综合

## 缅甸 Myanmar 🇲🇲

- **The Irrawaddy** — 缅甸流亡英文媒体
  - URL: https://www.irrawaddy.com/rss.xml
  - 类型: 综合

## 柬埔寨 Cambodia 🇰🇭

- **Khmer Times** — 英文媒体
  - URL: https://www.khmertimeskh.com/feed/
  - 类型: 综合
- **Phnom Penh Post** — 英文老牌
  - URL: https://www.phnompenhpost.com/feed
  - 类型: 综合

---

## 区域/跨国媒体

- **ASEAN Briefing** — 东盟商业资讯
  - URL: https://www.aseanbriefing.com/feed/
  - 类型: 区域商业
- **East Asia Forum** — 区域分析
  - URL: https://www.eastasiaforum.org/feed/
  - 类型: 学术/分析
- **CNA Asia** — CNA 亚洲版
  - URL: https://www.channelnewsasia.com/rss/asianews
  - 类型: 区域综合

---

## 使用说明

采集脚本 `scripts/collect_rss.py` 会读取上面的 URL 列表，并每天定时抓取一次。

如果你要新增/修改信息源，请：
1. 编辑本文件
2. 同步修改 `scripts/collect_rss.py` 中的 `RSS_SOURCES` 配置
3. 提交 PR 并说明理由
