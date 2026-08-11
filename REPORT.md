# 📋 Sea Radar 建站阶段汇报

> 文档版本：v2.0
> 汇报日期：2026-08-12
> 汇报人：TRAE AI 助手
> 审阅人：kivithink-pop

---

## 🆕 v2.0 更新（阶段 2 完成）

**新增加的内容**：

1. ✅ **Python 自动采集器**（`scripts/collect_rss.py`，15 个东南亚信息源）
2. ✅ **GitHub Actions 定时任务**（每天 UTC 0:00 自动跑）
3. ✅ **首批 67 条真实信息**（已自动入 GitHub 仓库 `data/raw/2026-08-11.json`）
4. ✅ **网站信息流页**已改造为自动读取真实数据
5. ✅ **3 条 AI 示例** + 67 条真实数据并存（后续可由人工筛选替换）

---

## ⚡ 重要更新（v1.1）

**汇报生成后发现并修复了一个严重 bug**：

> 🔴 **Bug**：第一版部署后，所有 5 种语言页面实际上**都显示中文**（i18n 字典没有正确加载）
> 🟢 **修复**：已修复 `getLocaleFromUrl` 和 `getLocalizedPath` 函数，添加 base path 支持
> ✅ **当前状态**：5 种语言全部正确本地化，已重新部署

**修复前 vs 修复后**：

| 语言 | 修复前 | 修复后 |
|---|---|---|
| 中文 | ✅ 东南亚前沿信息雷达 | ✅ 东南亚前沿信息雷达 |
| English | ❌ 显示中文 | ✅ Southeast Asia Frontier Information Radar |
| ไทย | ❌ 显示中文 | ✅ เอเชียตะวันออกเฉียงใต้ |
| Tiếng Việt | ❌ 显示中文 | ✅ Radar Thông tin Tiên phong |
| ភាសាខ្មែរ | ❌ 显示中文 | ✅ រ៉ាដារព័ត៌មានជាយុទ្ធសាលីអាស៊ីអាគ្នេយ៍ |

**当前建议**：请直接访问以下地址，**应该看到对应语言的本地化内容**。

---

## 🎯 一、本次工作概览

本次会话完成了 **从零到一** 的 sea-radar 开源项目基础设施搭建，包含：

1. **GitHub 仓库创建**（公开，含完整中文文档）
2. **5 语言多语种网站搭建**（中/英/泰/越/柬，i18n 已修复）
3. **自动部署流水线**（GitHub Actions → GitHub Pages）
4. **协作工具链准备**（gh CLI、Git for Windows、Node.js）

整体架构已具备**持续运行**能力，后续所有内容生产只需 `git push` 即可自动上线。

---

## 🌐 二、网站访问地址（**重要！请审阅**）

### 🇨🇳 默认（中文）
- **首页**：[https://kivithink-pop.github.io/sea-radar/](https://kivithink-pop.github.io/sea-radar/)
- **信息流**：[https://kivithink-pop.github.io/sea-radar/news/](https://kivithink-pop.github.io/sea-radar/news/)
- **关于**：[https://kivithink-pop.github.io/sea-radar/about/](https://kivithink-pop.github.io/sea-radar/about/)

### 🇺🇸 English
- **Home**：[https://kivithink-pop.github.io/sea-radar/en/](https://kivithink-pop.github.io/sea-radar/en/)
- **News**：[https://kivithink-pop.github.io/sea-radar/en/news/](https://kivithink-pop.github.io/sea-radar/en/news/)
- **About**：[https://kivithink-pop.github.io/sea-radar/en/about/](https://kivithink-pop.github.io/sea-radar/en/about/)

### 🇹🇭 ไทย / 泰语
- **หน้าแรก**：[https://kivithink-pop.github.io/sea-radar/th/](https://kivithink-pop.github.io/sea-radar/th/)
- **ข่าวสาร**：[https://kivithink-pop.github.io/sea-radar/th/news/](https://kivithink-pop.github.io/sea-radar/th/news/)
- **เกี่ยวกับ**：[https://kivithink-pop.github.io/sea-radar/th/about/](https://kivithink-pop.github.io/sea-radar/th/about/)

### 🇻🇳 Tiếng Việt / 越南语
- **Trang chủ**：[https://kivithink-pop.github.io/sea-radar/vi/](https://kivithink-pop.github.io/sea-radar/vi/)
- **Bản tin**：[https://kivithink-pop.github.io/sea-radar/vi/news/](https://kivithink-pop.github.io/sea-radar/vi/news/)
- **Giới thiệu**：[https://kivithink-pop.github.io/sea-radar/vi/about/](https://kivithink-pop.github.io/sea-radar/vi/about/)

### 🇰🇭 ភាសាខ្មែរ / 柬埔寨语
- **ទំព័រដើម**：[https://kivithink-pop.github.io/sea-radar/km/](https://kivithink-pop.github.io/sea-radar/km/)
- **ព័ត៌មាន**：[https://kivithink-pop.github.io/sea-radar/km/news/](https://kivithink-pop.github.io/sea-radar/km/news/)
- **អំពី**：[https://kivithink-pop.github.io/sea-radar/km/about/](https://kivithink-pop.github.io/sea-radar/km/about/)

### 🔗 GitHub 仓库
- **仓库主页**：[https://github.com/kivithink-pop/sea-radar](https://github.com/kivithink-pop/sea-radar)

> 💡 **建议审阅顺序**：
> 1. 先打开**中文首页** [https://kivithink-pop.github.io/sea-radar/](https://kivithink-pop.github.io/sea-radar/)，查看整体设计、布局、视觉风格
> 2. 点击右上角的**语言切换器**（5 国国旗下拉菜单），体验 5 语言切换效果
> 3. 浏览信息流页和关于页
> 4. 最后查看仓库代码（README、docs、GitHub Actions）

---

## 🐛 三、已发现并修复的 Bug 详情（v1.1）

### 3.1 Bug 现象

汇报文档第一版生成后，验证 5 语言访问时发现：

- 5 个页面的 HTML 体积相近（约 10-11 KB），内容大致相同
- 切换到 `/en/` 后，看到的标题仍然是"东南亚前沿信息雷达"
- 5 个页面的 `<html lang>` 都是 `zh`

### 3.2 根因分析

问题出在 `website/src/i18n/utils.js`：

```javascript
// ❌ 原版（错误）
export function getLocaleFromUrl(url) {
  const [, lang] = url.pathname.split('/');
  // 问题：url.pathname 是 /en/，split 后是 ['', 'en', '']，
  // 取 [1] 得到 'en'，但当 url.pathname 是 /sea-radar/en/ 时，
  // 实际 split 出来是 ['', 'sea-radar', 'en', '']，取 [1] 拿到 'sea-radar'
}
```

**核心问题**：
- 部署到 GitHub Pages 后，URL 实际是 `https://kivithink-pop.github.io/sea-radar/en/`
- `url.pathname` 返回 `/sea-radar/en/`
- split('/') 拿到 `['', 'sea-radar', 'en', '']`
- 取 `[1]` 得到 `'sea-radar'`（不是 `'en'`）
- 所以所有页面都被当作中文（default lang）

### 3.3 修复方案

```javascript
// ✅ 修复版
export function getLocaleFromUrl(url) {
  const pathname = url.pathname;
  const basePath = '/sea-radar';

  // 1. 去掉 base path
  const cleanPath = pathname.startsWith(basePath)
    ? pathname.slice(basePath.length)
    : pathname;

  // 2. 取第一段作为语言代码
  const segments = cleanPath.split('/').filter(Boolean);
  const first = segments[0];

  if (first && first in languages) {
    return first;
  }
  return defaultLang;
}
```

同时还修复了：

1. **BaseLayout.astro** 的 `currentPath` 计算（之前用正则替换，现在用专门函数）
2. **getLocalizedPath** 函数（之前没考虑 base path，现在正确返回 `/sea-radar/...`）

### 3.4 修复验证

重新部署后，5 种语言各自返回对应语言的本地化内容：

```
✓ 中文 [10080 bytes] -> 包含: 东南亚前沿信息雷达
✓ English [10725 bytes] -> 包含: Southeast Asia Frontier Information Radar
✓ ไทย [10632 bytes] -> 包含: เอเชียตะวันออกเฉียงใต้
✓ Tiếng Việt [10696 bytes] -> 包含: Radar Thông tin Tiên phong
✓ ភាសាខ្មែរ [10683 bytes] -> 包含: រ៉ាដារព័ត៌មានជាយុទ្ធសាលីអាស៊ីអាគ្នេយ៍
```

### 3.5 经验教训

✅ **正面教训**：
- 部署后必须**端到端验证**（这是第一次部署时漏掉的步骤）
- 实际生产环境与开发环境 URL 不同（base path 问题）
- 多语言项目需要逐语言验证内容

⚠️ **建议**：
- 后续每次添加新页面时，应编写自动化测试脚本，逐语言验证关键文案
- 在 GitHub Actions 中加入"内容验证"步骤

---

## 🏗️ 四、技术架构

### 4.1 仓库结构

```
sea-radar/
├── README.md                    # 项目主说明（中文）
├── LICENSE                      # MIT 许可证
├── REPORT.md                    # 本汇报文档
├── .gitignore                   # Git 忽略规则
├── package-lock.json            # 根目录依赖锁文件（GitHub Actions 需要）
├── .github/
│   └── workflows/
│       └── deploy.yml           # 自动部署工作流
└── website/                     # Astro 网站目录
    ├── package.json
    ├── astro.config.mjs         # Astro + i18n 配置
    ├── public/
    │   └── favicon.svg          # 网站图标
    └── src/
        ├── content.config.ts    # 内容集合定义
        ├── content/
        │   └── news/            # 信息条目存放处（当前为空）
        ├── i18n/                # 多语言字典
        │   ├── zh.json          # 简体中文
        │   ├── en.json          # English
        │   ├── th.json          # ไทย
        │   ├── vi.json          # Tiếng Việt
        │   ├── km.json          # ភាសាខ្មែរ
        │   └── utils.js         # 语言工具函数（含 i18n 修复）
        ├── styles/
        │   └── global.css       # 全局样式（含暗色模式）
        ├── layouts/
        │   └── BaseLayout.astro # 公共布局（导航 + 页脚 + 语言切换）
        ├── components/
        │   ├── HomeContent.astro
        │   ├── NewsContent.astro
        │   └── AboutContent.astro
        └── pages/
            ├── index.astro              # 中文首页
            ├── about.astro              # 中文关于
            ├── news/index.astro         # 中文信息流
            ├── en/                      # 英文（3 页面）
            ├── th/                      # 泰文（3 页面）
            ├── vi/                      # 越南文（3 页面）
            └── km/                      # 柬埔寨文（3 页面）
```

### 4.2 技术栈选型

| 层级 | 选型 | 理由 |
|---|---|---|
| **静态站点生成器** | Astro 5.1 | 多语言支持一流（官方 i18n）、性能极快、零 JS 默认输出 |
| **托管平台** | GitHub Pages | 免费、自动 HTTPS、零运维 |
| **CI/CD** | GitHub Actions | 与 GitHub Pages 原生集成，构建 44-50 秒 |
| **样式** | 原生 CSS + CSS 变量 | 轻量，无需额外构建，支持暗色模式 |
| **包管理** | npm | 与 Node.js LTS 自带，无需额外安装 |
| **运行环境** | Node.js 20.19.5 LTS | 便携版安装，免 UAC |

### 4.3 自动化部署流程

```
本地编辑 website/src/
    ↓
git add . → git commit -m "..." → git push
    ↓
GitHub 接收 main 分支推送
    ↓
GitHub Actions 自动触发 deploy.yml
    ↓
Checkout 代码 → npm ci → npm run build
    ↓
上传 website/dist 到 GitHub Pages
    ↓
网站自动更新（~1-2 分钟）
```

---

## 📊 五、交付物清单

### 5.1 已完成

| 类别 | 交付物 | 状态 |
|---|---|---|
| **基础设施** | GitHub 仓库 `sea-radar` | ✅ 公开 |
| **核心文档** | README.md（中文，含项目目标/特性/结构/技术栈） | ✅ 81 行 |
| **许可证** | MIT License | ✅ |
| **汇报文档** | REPORT.md（本文档） | ✅ v1.1 |
| **网站** | 5 语言 × 3 页面 = 15 个 HTML | ✅ 全部 200 OK，5 语言均已本地化 |
| **样式** | 全局 CSS（含暗色模式、响应式） | ✅ |
| **多语言** | 5 个语言字典文件（JSON） | ✅ 完整 + 修复 |
| **工具链** | gh CLI、Git for Windows、Node.js | ✅ 已安装 |
| **CI/CD** | `.github/workflows/deploy.yml` | ✅ 自动部署 |
| **部署** | GitHub Pages + HTTPS | ✅ 上线 |

### 5.2 待开发（后续阶段）

| 类别 | 内容 | 优先级 |
|---|---|---|
| **信息条目** | 首批 5-10 条示例信息（手动录入） | 🟡 高 |
| **采集管道** | Python/Node.js 自动化采集脚本 | 🟡 高 |
| **数据存储** | 本地 JSON / SQLite 数据库 | 🟡 高 |
| **搜索功能** | Pagefind 集成（全文搜索） | 🟢 中 |
| **分类视图** | 主题/国家筛选 | 🟢 中 |
| **订阅功能** | RSS 订阅生成 | 🟢 中 |
| **推送通知** | Email / Telegram Bot | 🔵 低 |
| **API** | 对外开放 API | 🔵 低 |

---

## 🎨 六、页面设计与功能

### 6.1 通用元素

每个页面都包含：

- **顶部导航栏**：Logo + 首页/信息流/关于 + 语言切换器
- **页脚**：项目标语 + GitHub 链接 + 许可证声明
- **响应式设计**：手机/平板/电脑自适应
- **暗色模式**：跟随系统设置自动切换
- **语言切换**：右上角下拉菜单，包含 5 种语言及对应国旗

### 6.2 首页（Home）

包含 5 大模块：

1. **Hero 区**：🌏 图标 + 项目标题 + 价值主张 + 两个 CTA 按钮（查看信息流 / GitHub）
2. **今日精选**：当前为空（等待数据接入）
3. **主题入口**：8 个主题卡片（政治/经济/科技/社会/文化/环境/商业/教育），含 emoji 图标
4. **项目数据**：4 个统计卡片（信息条目/覆盖国家/信息源/语言数）
5. **订阅区**：RSS / GitHub Star 入口

### 6.3 信息流页（News Feed）

当前为占位状态：

- 📡 大图标 + "暂无信息条目" 提示
- 多语言空状态文案（5 种语言都已翻译）
- "返回首页" 按钮

**下一步**：当采集管道就绪后，此页面会自动展示按时间倒序排列的甄选信息。

### 6.4 关于页（About）

包含 5 大板块：

- 🎯 **项目使命** — 详细描述项目的目标与价值
- 👥 **团队** — 提及 kivithink-pop 与 HU 共同维护
- 🗺️ **路线图** — 6 个里程碑（已完成 / 进行中 / 规划中）
- 📜 **许可证** — MIT 许可证说明
- 🤝 **贡献** — 3 个 GitHub 入口（Issues / Discussions / Fork）

---

## 🔧 七、关键决策与备选方案

### 7.1 静态站点 vs. 动态站点

**选择**：静态站点（Astro + GitHub Pages）

**理由**：
- ✅ 零运维成本（GitHub Pages 自动管理）
- ✅ 全球 CDN 加速，访问快
- ✅ 安全性高（无数据库、无后端）
- ✅ 免费
- ⚠️ 内容更新需要重新构建（但对个人项目足够）

**未来考虑**：如果后期需要用户评论、登录、个性化推荐等功能，可平滑迁移到 Vercel/Netlify + SSR。

### 7.2 多语言策略

**选择**：每种语言独立 URL 前缀（`/zh/`, `/en/`, `/th/`, `/vi/`, `/km/`）

**理由**：
- ✅ SEO 友好（每种语言独立索引）
- ✅ 利于维护（语言间相互独立）
- ✅ 切换成本低（用户可随时切换）

**未来考虑**：增加自动浏览器语言检测，根据 `Accept-Language` 自动重定向。

### 7.3 内容管理

**选择**：Markdown 文件 + Astro Content Collections

**理由**：
- ✅ 简单直观（用记事本就能写）
- ✅ Git 版本管理（每次修改都有历史）
- ✅ 前置元数据（front matter）支持结构化
- ✅ 无需 CMS 系统

**未来考虑**：可接入 Decap CMS（之前的 Netlify CMS）提供网页编辑后台。

---

## 📈 八、当前限制与已知问题

### 8.1 当前限制

| 限制 | 影响 | 解决方案 |
|---|---|---|
| GitHub Pages 域名 | 使用 `kivithink-pop.github.io/sea-radar/`，不够简短 | 后续可绑定自定义域名（如 `sea-radar.com`） |
| 采集自动化 | 暂无，需要手动录入信息 | 阶段 2 建设 Python 采集脚本 |
| 数据存储 | `src/content/news/` 为空 | 阶段 2 接入数据源 |
| 搜索功能 | 无 | 阶段 3 集成 Pagefind |
| 移动端优化 | 已实现但未做 PWA | 后续考虑 |

### 8.2 已知小问题

- **首页 emoji 显示**：使用了 🌏 🐛 💰 等 emoji，依赖系统字体支持。在大多数设备上正常显示。
- **柬埔寨语字体**：需要在用户设备上安装 Khmer 字体才能完美显示。
- **首次部署验证不充分**：v1.0 部署时只验证了 HTTP 200，没验证内容本地化。已修复并加入自动化检查思路。

---

## 🛠️ 九、本地开发指南

### 9.1 环境准备（已完成）

| 工具 | 版本 | 路径 |
|---|---|---|
| Node.js | v20.19.5 | `C:\Tools\node\` |
| Git for Windows | 2.55.0 | 系统 PATH |
| GitHub CLI | 2.97.0 | 系统 PATH |

### 9.2 常用命令

```powershell
# 切换到工作目录
cd "C:\Users\leo\Documents\个人网站"

# 启动本地开发服务器（带热更新）
$env:Path = "C:\Tools\node;" + $env:Path
cd website
npm run dev
# 浏览器访问 http://localhost:4321

# 构建生产版本
npm run build

# 预览构建结果
npm run preview

# 提交修改
cd ..
git add .
git commit -m "feat: 描述本次修改"
git push
```

### 9.3 目录约定

- `website/src/i18n/*.json` — 修改翻译
- `website/src/pages/<lang>/` — 修改对应语言页面
- `website/src/components/` — 修改可复用组件
- `website/src/layouts/BaseLayout.astro` — 修改导航/页脚
- `website/src/styles/global.css` — 修改全局样式
- `website/src/i18n/utils.js` — 修改语言工具函数

---

## 🎯 十、下一步建议

### 阶段 2：内容生产（1-2 周）

1. **手动录入 5-10 条示例信息**（创建 `.md` 文件到 `src/content/news/`）
2. **配置采集源**（先接入 1-2 个高质量 RSS 源）
3. **编写 Python 采集脚本**（自动抓取 + 简单筛选）
4. **建立本地数据存储**（JSON 或 SQLite）

### 阶段 3：功能增强（2-4 周）

1. **集成 Pagefind**（全文搜索）
2. **添加主题/国家视图**
3. **生成 RSS 订阅**
4. **添加时间线筛选器**
5. **加入自动化多语言验证测试**（防止再次出现 v1.0 的 bug）

### 阶段 4：分发与推送（按需）

1. **设置 Telegram Bot**（自动推送每日精选）
2. **Email 邮件订阅**
3. **对接社交媒体**（Twitter/Mastodon 自动发布）

---

## 📝 十一、本次工作总结

### 11.1 完成度

| 维度 | 完成度 |
|---|---|
| **基础设施** | 🟢 100% |
| **网站搭建** | 🟢 100% |
| **多语言支持** | 🟢 100%（v1.1 修复后） |
| **自动化部署** | 🟢 100% |
| **内容填充** | 🔴 0%（待采集管道） |

### 11.2 关键里程碑

- ✅ **2026-08-08 14:28** — GitHub 仓库创建
- ✅ **2026-08-08 14:29** — README 推送到远程
- ✅ **2026-08-08 21:50** — Astro 网站代码提交
- ✅ **2026-08-08 22:00** — Workflow 修复完成
- ✅ **2026-08-08 22:02** — 网站首次上线
- 🔴 **2026-08-08 22:20** — 发现 i18n bug（5 语言都显示中文）
- ✅ **2026-08-08 22:25** — i18n bug 修复，5 语言正确本地化

### 11.3 工作量统计

- **代码文件**：35+ 个新增文件
- **总代码行数**：约 13,000 行（含依赖锁文件）
- **手动录入字典**：5 个语言文件，每个约 100-150 个 key
- **构建时间**：44-50 秒
- **部署时间**：即时（GitHub Pages CDN）
- **工作时长**：约 2 小时（含问题诊断与修复）

### 11.4 验证清单

- ✅ 仓库已创建并可访问
- ✅ 5 种语言 × 3 页面 = 15 个 HTML 全部 200 OK
- ✅ 5 种语言内容已验证为对应本地化文本
- ✅ 语言切换器在所有页面工作正常
- ✅ GitHub Actions 自动化部署已生效
- ✅ 文档完整（README、REPORT、LICENSE）

---

## 🙏 致谢

感谢你授权我在你电脑上完成所有工作。这次会话的成果已经全部安全保存到：

- **本地仓库**：`C:\Users\leo\Documents\个人网站\`
- **GitHub 远程**：[https://github.com/kivithink-pop/sea-radar](https://github.com/kivithink-pop/sea-radar)
- **线上网站**：[https://kivithink-pop.github.io/sea-radar/](https://kivithink-pop.github.io/sea-radar/)

随时可以回来继续推进。如有任何问题或想调整的细节，请告诉我。

---

*汇报完毕（v1.1，已修复 i18n bug）。审阅完成后请告知下一步方向。* 🚀
