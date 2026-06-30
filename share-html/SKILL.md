---
name: share-html
description: >-
  Use when the user asks to create a single-file HTML document intended to be
  shared with other people — research reports, comparison pages, decision
  documents, status updates, weekly reports, kanban-style trackers, one-pagers.
  Produces a self-contained .html file that opens with a double-click and
  renders with CDN-loaded Tailwind / Alpine.js. Five template styles available:
  editorial (default), briefing, dashboard, docs, minimal.
metadata:
  author: ggwhite
  version: "1.0.0"
---

# share-html

## What this skill does

依場景選模板 → 讀對應 template → 挑出需要的元件、刪掉用不到的、把示範資料替換成真實資料，最後輸出一個雙擊可開的單檔 `.html`。

## 模板選擇

| 模板 | 檔案 | 適合場景 |
|---|---|---|
| editorial | `template.html` | 研究報告、審查報告、對照分析（預設） |
| briefing | `template-briefing.html` | 週報/月報、給主管的摘要 |
| dashboard | `template-dashboard.html` | 數據看板、監控報告 |
| docs | `template-docs.html` | RFC、技術文件、操作手冊 |
| minimal | `template-minimal.html` | 快速分享一個結論或對照 |

使用者沒指定時，依內容性質自動選：
- 數據多 → dashboard
- 長文/步驟多 → docs
- 只有 1-2 個重點 → minimal
- 給主管/非技術人看 → briefing
- 其他 → editorial（預設）

## Style rules — editorial

| 角色 | Token | Hex |
|---|---|---|
| 背景 | `#0b1020` + radial gradient | 比 slate-950 再深一點 |
| 卡片 | `bg-slate-900/60 border border-slate-800` | 半透明深色 + 細邊 |
| 主文字 | `text-slate-100` / `text-slate-200` | |
| 次文字 | `text-slate-400` / `text-slate-500` | |
| 主色 | `cyan-400` | `#22d3ee` |
| 紫色 | `violet-400` | `#a78bfa` |
| 粉色 | `pink-400` | `#f472b6` |
| 漸層 | `from-cyan-400 via-violet-400 to-pink-400` | 標題、徽章、進度條 |
| 警告 | `amber-400` | `#facc15` |
| 警示 | `red-400` | `#f87171` |
| 成功 | `emerald-400` | `#34d399` |
| 字體 | `-apple-system, BlinkMacSystemFont, "Inter", "PingFang TC", "Microsoft JhengHei", sans-serif` | |
| 圓角 | `rounded-lg`（卡片、徽章）、`rounded-full`（pill badge） | |
| 寬度 | TOC 260px + 內容 max-w-3xl，整體 max-w-6xl 置中 | |

**不做**：玻璃擬態、shimmer 動畫、pastel 配色、emoji icon 堆疊、generic AI 漸變 hover。

漸層只在「明確強調」處用：頂部進度條、HERO 關鍵字 highlight、SECTION_HEADER 編號徽章、CHECKLIST 進度條。其餘該用單色就用單色。

## Available components

| 名稱 | 用途 |
|---|---|
| TOP_BAR | 頂部 2px 漸層條（fixed） |
| STICKY_TOC | 左側目錄，IntersectionObserver 高亮當前章節 |
| HERO | 標籤 chip + 大標（漸層 highlight 關鍵字）+ 副標 + meta |
| SECTION_HEADER | 編號徽章（漸層方塊）+ 標題 + 副標 |
| QUOTE_BLOCK | 大引號 + 紫左 border + 引述 + 出處 |
| CALLOUT_CARD | 卡片頂端細色條 + 標題 badge + 列表內容 |
| TABS | 切換式面板（active tab cyan-300 + cyan-400 底線）；panel 可放任何內容，2~4 個 tab 最合適 |
| STATS_ROW | 4 個大彩色數字 + 標籤 |
| RADAR_CHART | Chart.js 雷達圖（多 dataset 對照）+ 右側自訂 legend；配色用 cyan/pink 主色 |
| DATA_TABLE | 搜尋 + 分類 chip 篩選 + 列項目（嚴重度 badge + 位置 + 描述） |
| KANBAN | 三欄 drag-and-drop（待辦 / 進行中 / 已完成） |
| CHECKLIST | 漸層進度條 + 完成度 + 勾選 strikethrough |
| IMG_GALLERY | 截圖 / 圖示，單欄展示；點圖整個 figure 進全螢幕 zoom（含 markers 與步驟列表）；圖以 base64 inline。支援兩種樣板：含 STEP markers / 純圖 |
| SVG_FLOW | 手刻 SVG 流程圖；節點 = 圓角 rect、強調用 cyan / red 邊、連線用 cubic bezier + arrow marker。同套設計語言，比 mermaid 更貼合 editorial 風格 |
| TIMELINE | 縱向時間軸：左 dot（cyan / amber / emerald 區分階段）+ 時間 + 標題 + 描述 |
| DIFF_VIEW | 左右兩欄 before / after，紅 / 綠標 + 行內背景色 |
| COMPARISON_TABLE | 多方案 × 多功能對照表；推薦欄整欄 cyan-500/5 高亮 |
| METRIC_TREND | 大數字 + delta % + Chart.js sparkline 折線；多卡用 grid-cols-3 並排 |
| COLLAPSIBLE | 原生 details/summary 自訂樣式；group-open 旋轉 › 符號 |
| CODE_BLOCK | highlight.js atom-one-dark 上色 + 檔名 header + 右上複製按鈕 |
| NOTE_BOX | 一行式提示條：INFO / WARN / OK / DANGER；左 2px 邊條 + badge |
| SOURCES | 編號 + 標題 + 出處的參考資料列表 |

template 內每個元件以 `<!-- COMPONENT: NAME -->` 與 `<!-- /COMPONENT: NAME -->` 包夾。

## Style rules — briefing

| 角色 | Token | Hex |
|---|---|---|
| 背景 | `#0b1020` + 暖色 radial gradient | |
| 主色 | `amber-400` | `#fbbf24` |
| 漸層 | `from-amber-400 via-orange-400 to-rose-400` | 標題、徽章、進度條 |
| 其他 | 同 editorial | |

Layout：全寬單欄，每個 section `min-h-screen` 佔滿一頁。無 STICKY_TOC，改用底部 DOT_NAV（圓點列）。

## Style rules — dashboard

同 editorial 配色（主色 cyan-400）。Layout 改為頂部 tab 切換（概覽/細節/趨勢）+ 密集 grid（`grid-cols-2` / `grid-cols-3`）。

## Style rules — docs

| 角色 | Token | Hex |
|---|---|---|
| 背景 | `#f8fafc`（slate-50） | 淺色 |
| 卡片 | `bg-white border border-slate-200` | |
| 主文字 | `text-slate-700` | `#334155` |
| 次文字 | `text-slate-500` | |
| 主色 | `cyan-600` | `#0891b2` |
| 漸層 | `from-cyan-500 via-blue-500 to-violet-500` | |
| Code 主題 | highlight.js `github`（淺色） | |

Layout 同 editorial（TOC + 內容雙欄）。

## Style rules — minimal

同 editorial 配色但無漸層。主色 `slate-300`。SECTION_HEADER 編號徽章 `bg-slate-700`。Layout：無 TOC、無 TOP_BAR，單欄 `max-w-2xl` 置中。

## Scroll 進場動畫

- **fade-in**：任何區塊加 `data-reveal`，scroll 進視窗時加 `.is-visible`（opacity 0→1、translateY 8px→0，0.7s ease）
- **count-up 數字**：數字 div 加 `data-counter="<target>"`、可選 `data-format="comma|percent|ms|int"`，textContent 初始 "0"；進場後 1.2s ease-out 跑到 target
- **chart lazy 渲染**：圖表卡片加 `data-chart="radar"` 或 `data-chart="trend"`，第一次 scroll 進場才 `new Chart()`，自帶 Chart.js 內建動畫
- **進度條 lazy fill**：CHECKLIST 進度條卡 `data-progress="checklist"` + Alpine state `progressVisible`，進場前 width 0，進場後動畫拉到當前值
- 已尊重 `prefers-reduced-motion`，使用者關閉動畫時自動 disable

新增需要 reveal / counter / lazy chart 的元件時依此約定加 attribute 即可，不用改 JS。

## Canvas 特效（可選）

預設不加。使用者說「加特效」「要酷一點」或場景是展示/demo 時才貼入。
貼入位置：`<body>` 開頭，所有內容之前。

### 輕量級

| 特效 | 檔案 | 效果 |
|---|---|---|
| gradient-flow | `effects/gradient-flow.html` | 大色塊緩慢流動背景（CSS div + blur） |
| cursor-glow | `effects/cursor-glow.html` | 滑鼠跟隨光暈（CSS div） |

### 中量級

| 特效 | 檔案 | 效果 |
|---|---|---|
| particles | `effects/particles.html` | 漂浮粒子 + 連線 + 滑鼠斥力 |
| parallax-depth | `effects/parallax-depth.html` | 捲動景深粒子（三層） |
| matrix-rain | `effects/matrix-rain.html` | 數字雨（適合資安/技術主題） |
| morphing-blobs | `effects/morphing-blobs.html` | 有機變形色塊 |

### 重量級（行動裝置慎用）

| 特效 | 檔案 | 效果 |
|---|---|---|
| flow-field | `effects/flow-field.html` | Perlin noise 流場粒子 |
| aurora | `effects/aurora.html` | 北極光色帶波動 |
| metaballs | `effects/metaballs.html` | 融合色球 |

深色模板全部適用；淺色 docs 模板只適合 cursor-glow。
特效片段以 `<!-- EFFECT: NAME -->` / `<!-- /EFFECT: NAME -->` 標記。
所有特效 `position: fixed; z-index: 0; pointer-events: none`，尊重 `prefers-reduced-motion`。

## Process

1. 依場景選模板（見「模板選擇」段落）→ 用 Read 讀對應 template 檔案
2. 依使用者需求挑用的元件、刪不要的
3. 把示範資料替換成真實資料；TOC 列表跟著實際章節調整
4. 保持 style rules 一致；不另創配色
5. 輸出單檔 `.html` 至使用者指定位置，或預設 `~/projects/<topic>/<name>.html`
6. 跑 `open <path>` 幫使用者開啟

## 引用與截圖規範（重要）

**MR / Issue / Commit / URL 必加 `<a>` 連結**：
- GitLab MR `!570` 等 → `<a href="https://git.tyche-tech.io/<group>/<repo>/-/merge_requests/570" target="_blank" rel="noopener" class="text-cyan-300 hover:text-cyan-200 underline decoration-cyan-700">!570</a>`
- GitLab Issue `#30954` → 同樣加 `target="_blank"` 與 cyan-300 樣式
- 純粹的 URL 一律包成可點連結，不要當文字顯示
- 在 hero meta、SOURCES、文中提及處**都要**處理

**涉及後台操作的章節必須附截圖**：
- 描述「在 BI 後台怎麼操作」「點哪裡」「設定在哪頁」這類內容時，主動詢問使用者要不要附截圖
- 使用者可直接 Cmd+V 貼到對話，clipboard 暫存路徑 `/var/folders/.../clipboard-*.png` Claude 能直接讀
- 用 python `base64.b64encode(open(path,'rb').read())` 取得字串嵌進 `<img src="data:image/png;base64,...">`
- 用 IMG_GALLERY 元件嵌入；每張圖要有 `figcaption` 寫清楚對應到哪一步
- 截圖大小注意：若超過 1MB 提醒使用者壓縮（線上工具如 tinypng）；過大會讓 HTML 檔肥到難以分享
- 圖要點得到放大（figure-level zoom）— 元件已內建

**STEP markers（截圖內步驟標註）**：
- 描述操作流程時，主動在截圖內標 `1`/`2`/`3` 圓徽章對應到 UI 元素位置
- 座標用 `%`（`style="left: X%; top: Y%;"`），看圖**目測估**——位置偏 5-10% 是正常，使用者會回饋微調
- 徽章 hover 時對應步驟列表項目高亮 cyan（用 `hoveredStep` state + `:class`）
- 用兩種樣板擇一：含 markers / 純圖；不要每張都加 markers，看內容必要性決定
- 圖點下去後 zoom 到全螢幕，markers 跟著放大、位置維持對齊（座標是 % 相對圖本身）

## Output expectations

- 單一 `.html`，雙擊可開、可直接傳給別人
- CDN 全用 `cdn.tailwindcss.com` 與 `cdn.jsdelivr.net`
- 不留 demo 留下來的 fake data（PR、Kanban cards、todos、嚴重度項目）
- 標題、副標、章節文字符合使用者描述的真實場景
- TOC 章節數量與實際內容對得上
