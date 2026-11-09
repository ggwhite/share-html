#!/usr/bin/env python3
"""Record the README clips (animated WebP) from the real templates and effects.

Requirements:
  - Python Playwright with Chromium (`pip install playwright && playwright install chromium`)
  - ffmpeg (frame scaling / tiling) and img2webp from libwebp (`brew install webp`)
  - network access: templates load Tailwind / Alpine / Chart.js / fonts from CDNs

Usage:
    python3 scripts/record-clips.py              # every clip
    python3 scripts/record-clips.py tour light   # only the named clips

Clips (written to assets/):
    tour.webp       hero: every template in turn, then three effects   (~25 s)
    editorial.webp  scroll, filter the findings table, tick the checklist
    briefing.webp   slide-by-slide scroll-snap deck
    dashboard.webp  tab switching across the three panels
    light.webp      docs (light theme) then minimal (single column)
    handdrawn.webp  notebook layout, sticky notes, checklist
    effects.webp    3x3 mosaic of all nine canvas effects

Frames are screenshots taken after the page has loaded (no blank/loading
frames). Scroll clips return to the top at the end so the loop is clean.
"""
import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "share-html"
OUT = ROOT / "assets"

VIEWPORT = {"width": 1280, "height": 800}
FPS = 10
WIDTH = 900          # output width of every clip
QUALITY = 70         # img2webp lossy quality

EFFECTS = [
    "gradient-flow", "cursor-glow", "particles",
    "parallax-depth", "matrix-rain", "morphing-blobs",
    "flow-field", "aurora", "metaballs",
]

LABEL_JS = """(name) => {
  const el = document.createElement('div');
  el.textContent = name;
  el.style.cssText = 'position:fixed;right:24px;bottom:24px;z-index:2147483647;'
    + 'padding:10px 20px;border-radius:999px;font:600 22px/1 -apple-system,Inter,sans-serif;'
    + 'letter-spacing:.02em;color:#fff;background:rgba(15,23,42,.85);'
    + 'box-shadow:0 4px 18px rgba(0,0,0,.35);border:1px solid rgba(148,163,184,.35);';
  document.body.appendChild(el);
}"""


def ease(t):
    return 0.5 - 0.5 * math.cos(math.pi * t)


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


class Clip:
    """Collects numbered PNG frames for one clip."""

    def __init__(self, tmp, name):
        self.name = name
        self.dir = tmp / name
        self.dir.mkdir()
        self.n = 0
        self.page = None

    def open(self, browser, url, label=None, viewport=VIEWPORT):
        self.close()
        page = browser.new_page(viewport=viewport, device_scale_factor=1)
        page.goto(url, wait_until="networkidle")
        page.evaluate("document.fonts.ready")
        page.evaluate("document.documentElement.style.scrollBehavior = 'auto'")
        page.wait_for_timeout(1500)  # reveal animations, counters, charts settle
        if label:
            page.evaluate(LABEL_JS, label)
        self.page = page
        return page

    def close(self):
        if self.page:
            self.page.close()
            self.page = None

    def shot(self):
        self.page.screenshot(path=str(self.dir / f"{self.n:05d}.png"))
        self.n += 1

    def hold(self, seconds):
        for _ in range(round(seconds * FPS)):
            self.page.wait_for_timeout(1000 // FPS // 2)
            self.shot()

    def max_y(self):
        return self.page.evaluate("document.documentElement.scrollHeight - innerHeight")

    def y_of(self, selector, offset=80):
        return self.page.evaluate(
            "([s, o]) => document.querySelector(s).getBoundingClientRect().top + scrollY - o",
            [selector, offset])

    def scroll_to(self, y, seconds):
        start = self.page.evaluate("window.scrollY")
        y = max(0, min(y, self.max_y()))
        steps = max(1, round(seconds * FPS))
        for i in range(1, steps + 1):
            cur = start + (y - start) * ease(i / steps)
            self.page.evaluate(f"window.scrollTo({{top: {cur}, behavior: 'instant'}})")
            self.page.wait_for_timeout(30)
            self.shot()

    def click(self, locator, settle=0.6):
        locator.click()
        self.hold(settle)


# ── clip scripts ──────────────────────────────────────────────

def tpl(file):
    return (SKILL / file).as_uri()


def fx(name):
    return (SKILL / "effects" / f"{name}.html").as_uri()


def seg_scroll(c, browser, file, label=None, depth=1300, down=1.8, hold_top=0.8, hold_end=0.5):
    c.open(browser, tpl(file), label)
    c.hold(hold_top)
    c.scroll_to(depth, down)
    c.hold(hold_end)


def seg_effect(c, browser, name, seconds, viewport=VIEWPORT, label=None):
    w, h = viewport["width"], viewport["height"]
    page = c.open(browser, fx(name), label, viewport)
    page.mouse.move(w / 2, h / 2)
    frames = round(seconds * FPS)
    for i in range(frames):
        t = i / frames
        if name in ("cursor-glow", "particles"):
            # Lissajous path so mouse-driven effects visibly react; returns to start
            page.mouse.move(w / 2 + w * 0.32 * math.sin(2 * math.pi * t),
                            h / 2 + h * 0.28 * math.sin(4 * math.pi * t))
        elif name == "parallax-depth":
            page.evaluate(f"window.scrollTo(0, {1200 * math.sin(math.pi * t)})")
        page.wait_for_timeout(1000 // FPS)
        c.shot()


def clip_tour(c, browser):
    seg_scroll(c, browser, "template.html", "editorial")
    seg_scroll(c, browser, "template-briefing.html", "briefing", depth=1600)
    c.open(browser, tpl("template-dashboard.html"), "dashboard")
    c.hold(0.8)
    c.click(c.page.locator("button", has_text="細節").first, 1.0)
    c.click(c.page.locator("button", has_text="趨勢").first, 1.0)
    seg_scroll(c, browser, "template-docs.html", "docs")
    seg_scroll(c, browser, "template-minimal.html", "minimal")
    seg_scroll(c, browser, "template-handdrawn.html", "handdrawn")
    for name in ("aurora", "particles", "metaballs"):
        seg_effect(c, browser, name, 1.6, label=f"effect · {name}")


def clip_editorial(c, browser):
    page = c.open(browser, tpl("template.html"))
    c.hold(0.8)
    c.scroll_to(c.y_of("#section-3"), 1.4)
    c.hold(0.4)
    c.scroll_to(c.y_of("input[placeholder^='搜尋']", 120), 0.6)
    c.click(page.locator("button", has_text="嚴重").first, 1.0)
    c.click(page.locator("button", has_text="全部").first, 0.6)
    c.scroll_to(c.y_of("#section-5"), 1.4)
    items = page.locator("#section-5 li.cursor-pointer")
    c.click(items.nth(2), 0.5)   # first two items start ticked; tick the next two
    c.click(items.nth(3), 0.9)
    # restore state so the loop is seamless
    items.nth(2).click()
    items.nth(3).click()
    c.scroll_to(0, 1.4)
    c.hold(0.3)


def clip_briefing(c, browser):
    c.open(browser, tpl("template-briefing.html"))
    c.hold(1.0)
    for i in range(1, 5):
        c.scroll_to(c.y_of(f"#slide-{i}", 0), 0.8)
        c.hold(0.9)
    c.scroll_to(0, 1.2)
    c.hold(0.3)


def clip_dashboard(c, browser):
    page = c.open(browser, tpl("template-dashboard.html"))
    c.hold(1.2)
    for tab in ("細節", "趨勢", "概覽"):
        c.click(page.locator("button", has_text=tab).first, 1.6)
    c.scroll_to(500, 1.0)
    c.hold(0.6)
    c.scroll_to(0, 1.0)


def clip_light(c, browser):
    c.open(browser, tpl("template-docs.html"), "docs")
    c.hold(0.8)
    c.scroll_to(c.y_of("#section-2"), 1.2)
    c.hold(0.6)
    c.scroll_to(c.y_of("#section-4"), 1.2)
    c.hold(0.6)
    c.open(browser, tpl("template-minimal.html"), "minimal")
    c.hold(0.8)
    c.scroll_to(1400, 2.0)
    c.hold(0.5)
    c.scroll_to(0, 1.0)


def clip_handdrawn(c, browser):
    page = c.open(browser, tpl("template-handdrawn.html"))
    c.hold(1.0)
    c.scroll_to(c.y_of("#section-2"), 1.4)
    c.hold(0.7)
    c.scroll_to(c.y_of("#section-4"), 1.4)
    items = page.locator("#section-4 li.cursor-pointer")
    c.click(items.nth(2), 0.5)   # first two items start ticked; tick the last two
    c.click(items.nth(3), 0.9)
    items.nth(2).click()
    items.nth(3).click()
    c.scroll_to(0, 1.4)
    c.hold(0.3)


CLIPS = {
    "tour": clip_tour,
    "editorial": clip_editorial,
    "briefing": clip_briefing,
    "dashboard": clip_dashboard,
    "light": clip_light,
    "handdrawn": clip_handdrawn,
}


# ── encoding ──────────────────────────────────────────────────

def encode(frames, out):
    run(["img2webp", "-loop", "0", "-min_size", "-lossy", "-q", str(QUALITY), "-m", "4",
         "-d", str(1000 // FPS), *frames, "-o", str(out)])


def to_webp(frames_dir, out):
    """Scale PNG frames to WIDTH with ffmpeg, then encode with img2webp."""
    scaled = frames_dir.parent / f"{frames_dir.name}-scaled"
    scaled.mkdir()
    run(["ffmpeg", "-y", "-i", str(frames_dir / "%05d.png"),
         "-vf", f"scale={WIDTH}:-2:flags=lanczos", str(scaled / "%05d.png")])
    encode(sorted(str(p) for p in scaled.glob("*.png")), out)


def record_effects(browser, tmp):
    tile_w = WIDTH // 3
    tile_h = round(tile_w * 10 / 16)
    vp = {"width": 640, "height": 400}
    inputs = []
    for name in EFFECTS:
        c = Clip(tmp, f"fx-{name}")
        seg_effect(c, browser, name, 8, viewport=vp)
        c.close()
        inputs += ["-framerate", str(FPS), "-i", str(c.dir / "%05d.png")]
    mosaic = tmp / "effects"
    mosaic.mkdir()
    scaled = "".join(f"[{i}:v]scale={tile_w}:{tile_h}:flags=lanczos[v{i}];" for i in range(9))
    layout = "|".join(f"{(i % 3) * tile_w}_{(i // 3) * tile_h}" for i in range(9))
    stack = "".join(f"[v{i}]" for i in range(9)) + f"xstack=inputs=9:layout={layout}"
    run(["ffmpeg", "-y", *inputs, "-filter_complex", scaled + stack, str(mosaic / "%05d.png")])
    out = OUT / "effects.webp"
    encode(sorted(str(p) for p in mosaic.glob("*.png")), out)
    return out


def main():
    which = sys.argv[1:] or [*CLIPS, "effects"]
    for tool in ("ffmpeg", "img2webp"):
        if not shutil.which(tool):
            sys.exit(f"{tool} not found on PATH")
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="share-html-clips-") as tmp, sync_playwright() as p:
        tmp = Path(tmp)
        browser = p.chromium.launch()
        try:
            for name in which:
                if name == "effects":
                    print("wrote", record_effects(browser, tmp))
                    continue
                c = Clip(tmp, name)
                CLIPS[name](c, browser)
                c.close()
                out = OUT / f"{name}.webp"
                to_webp(c.dir, out)
                print(f"wrote {out} ({c.n} frames, {c.n / FPS:.1f}s)")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
