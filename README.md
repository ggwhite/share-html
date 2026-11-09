<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg" />
  <img src="assets/banner-dark.svg" alt="share-html" width="720" />
</picture>

**Self-contained HTML templates for shareable reports — double-click to open, drag to share.**

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skill that generates single-file `.html`
reports with **interactive components**, **data visualization**, and optional **canvas effects**.
No build step, no server.

[![Claude Code skill](https://img.shields.io/badge/Claude%20Code-skill-D97757)](https://docs.anthropic.com/en/docs/claude-code)
[![Templates](https://img.shields.io/badge/templates-6-22d3ee)](#-templates)
[![Effects](https://img.shields.io/badge/canvas%20effects-9-818cf8)](#-canvas-effects)
[![Zero build](https://img.shields.io/badge/build%20step-none-34d399)](#-tech-stack)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

[Install](#-install) · [Features](#-features) · [Templates](#-templates) · [Canvas Effects](#-canvas-effects) · [Usage](#-usage) · [Tech Stack](#-tech-stack) · [License](#-license)

</div>

---

<div align="center">
  <img src="assets/tour.webp" alt="share-html tour — the editorial report scrolls past its sticky TOC and stat cards; the briefing deck snaps from slide to slide; the dashboard switches from overview to detail to trend tabs; the light docs page and the single-column minimal page scroll by; the handdrawn notebook shows sketchy borders and sticky notes; then the aurora, particles and metaballs canvas effects animate" width="900" />
</div>

## 📦 Install

```bash
npx skills add ggwhite/share-html
```

## ✨ Features

<table>
<tr>
<td width="42%" valign="middle">

### editorial — the default report

A deep dark theme with a **sticky TOC** that tracks your scroll, gradient accents, and
**18 interactive components**. Filter a **searchable findings table**, drag **Kanban**
cards, read **Chart.js radar charts**, and tick off a **checklist with a progress bar**.
Best for research reports, code reviews, and comparative analysis.

</td>
<td><img src="assets/editorial.webp" alt="editorial — scroll past the hero to the stats and findings table, filter the table to 嚴重 (critical) and back to 全部 (all), scroll to the action checklist and tick two items, scroll back to the top" /></td>
</tr>
<tr>
<td width="42%" valign="middle">

### briefing — one idea per screen

Full-page **slides** with warm amber tones. Each section fills the viewport with large
text and **animated stat counters**, glued together with **scroll snap** and bottom dot
navigation. Built for weekly reports and executive summaries.

</td>
<td><img src="assets/briefing.webp" alt="briefing — the title slide, then four slides snap into place one after another, then back to the first slide" /></td>
</tr>
<tr>
<td width="42%" valign="middle">

### dashboard — dense, tabbed data

Three **tab panels** — overview, detail, and trends — packed with metrics, sparklines,
radar charts, and tables in **2–3 column grids**. Charts initialize **lazily** the first
time their tab opens.

</td>
<td><img src="assets/dashboard.webp" alt="dashboard — switch from 概覽 (overview) to 細節 (detail) to 趨勢 (trend) and back to overview, then scroll down the overview grid and back up" /></td>
</tr>
<tr>
<td width="42%" valign="middle">

### docs & minimal — light and lean

**docs** is a clean white theme for technical documentation, with the same two-column
TOC layout as editorial and **GitHub-style code highlighting**. **minimal** drops the
TOC and progress bar entirely: one centered `max-w-2xl` column for sharing **one
conclusion fast**.

</td>
<td><img src="assets/light.webp" alt="docs then minimal — the docs page scrolls from the overview to the install guide and API reference; then the minimal single-column page scrolls down and back to the top" /></td>
</tr>
<tr>
<td width="42%" valign="middle">

### handdrawn — notebook & whiteboard

For meeting notes, decision records, and workshop summaries. **Rough.js** draws sketchy
borders, marker underlines, and **sticky notes**; **JasonHandwriting** sets Traditional
Chinese headings and labels while long paragraphs stay in readable system fonts.

</td>
<td><img src="assets/handdrawn.webp" alt="handdrawn — the notebook hero, scroll to the sticky-note section, then to the checklist and tick two items, then back to the top" /></td>
</tr>
<tr>
<td width="42%" valign="middle">

### Nine canvas effects

Drop an optional background effect into any template — from **light** CSS glows to
**heavy** Perlin-noise flow fields. All of them respect **`prefers-reduced-motion`**
and pause when the tab is hidden.

</td>
<td><img src="assets/effects.webp" alt="All nine effects animating in a 3 by 3 grid — gradient-flow, cursor-glow and particles (reacting to a moving cursor); parallax-depth (scrolling), matrix-rain and morphing-blobs; flow-field, aurora and metaballs" /></td>
</tr>
</table>

## 🖼 Templates

Six templates. Claude picks the one that fits your content, or you can name one directly.
Click a thumbnail for the full-size screenshot.

<table>
<tr>
<td align="center" width="33%"><a href="screenshots/editorial.png"><img src="screenshots/editorial.png" alt="editorial template" /></a><br/><b>editorial</b> (default)<br/><sub>research reports · code reviews</sub></td>
<td align="center" width="33%"><a href="screenshots/briefing.png"><img src="screenshots/briefing.png" alt="briefing template" /></a><br/><b>briefing</b><br/><sub>weekly reports · exec summaries</sub></td>
<td align="center" width="33%"><a href="screenshots/dashboard.png"><img src="screenshots/dashboard.png" alt="dashboard template" /></a><br/><b>dashboard</b><br/><sub>metrics · monitoring</sub></td>
</tr>
<tr>
<td align="center" width="33%"><a href="screenshots/docs.png"><img src="screenshots/docs.png" alt="docs template" /></a><br/><b>docs</b><br/><sub>technical documentation</sub></td>
<td align="center" width="33%"><a href="screenshots/minimal.png"><img src="screenshots/minimal.png" alt="minimal template" /></a><br/><b>minimal</b><br/><sub>one conclusion, fast</sub></td>
<td align="center" width="33%"><a href="screenshots/handdrawn.png"><img src="screenshots/handdrawn.png" alt="handdrawn template" /></a><br/><b>handdrawn</b><br/><sub>meeting notes · decisions</sub></td>
</tr>
</table>

| Template | File | Highlights |
|----------|------|------------|
| editorial (default) | `template.html` | Sticky TOC with scroll tracking, searchable tables, drag-and-drop Kanban, radar charts & sparklines, checklists |
| briefing | `template-briefing.html` | One section per screen with scroll snap, dot navigation, animated counters, amber/orange/rose accents |
| dashboard | `template-dashboard.html` | Tab switching with lazy chart init, dense 2–3 column grids, real-time-style timestamp |
| docs | `template-docs.html` | Light background (`#f8fafc`), GitHub code highlighting, collapsible FAQ, cyan/blue/violet accents |
| minimal | `template-minimal.html` | `max-w-2xl` centered column, no gradients, muted slate palette, minimal JavaScript |
| handdrawn | `template-handdrawn.html` | Handwriting headings & labels, Rough.js sketch borders, sticky notes, whiteboard flow blocks |

## 🌌 Canvas Effects

Nine optional visual effects you can drop into any template. Add them to `<body>` before your content.

| Effect | File | Weight | Description |
|--------|------|--------|-------------|
| gradient-flow | `effects/gradient-flow.html` | Light | Drifting color blobs with CSS blur |
| cursor-glow | `effects/cursor-glow.html` | Light | Mouse-following radial glow |
| particles | `effects/particles.html` | Medium | Floating particles with connecting lines |
| parallax-depth | `effects/parallax-depth.html` | Medium | Three-layer scroll parallax |
| matrix-rain | `effects/matrix-rain.html` | Medium | Katakana/number rain effect |
| morphing-blobs | `effects/morphing-blobs.html` | Medium | Organic shape-shifting blobs |
| flow-field | `effects/flow-field.html` | Heavy | Perlin noise particle flow |
| aurora | `effects/aurora.html` | Heavy | Northern lights wave bands |
| metaballs | `effects/metaballs.html` | Heavy | Merging color spheres |

All effects respect `prefers-reduced-motion` and pause when the tab is hidden.
Every dark template works with all of them; the light docs template only suits cursor-glow.

## 🚀 Usage

Once installed, trigger the skill in Claude Code with:

- 「做 HTML 給別人看」
- 「產一份報告」
- 「套我的 template」
- 「用 share-html」

Claude will pick the best template based on your content, or you can specify one directly.

## 🧰 Tech Stack

- [Tailwind CSS](https://tailwindcss.com/) (CDN)
- [Alpine.js](https://alpinejs.dev/) (CDN)
- [Chart.js](https://www.chartjs.org/) (CDN, only when needed)
- [highlight.js](https://highlightjs.org/) (CDN, only when needed)
- Canvas 2D API (effects only)

Zero build step. Zero dependencies. Every output is a single `.html` file.

<details>
<summary>Regenerating the README clips</summary>

The animated WebP clips in `assets/` are recorded from the real templates with Playwright:

```bash
pip install playwright && playwright install chromium   # once
brew install ffmpeg webp                                 # ffmpeg + img2webp
python3 scripts/record-clips.py                          # all clips
python3 scripts/record-clips.py tour effects             # just some
```

</details>

## 📄 License

[MIT](LICENSE)
