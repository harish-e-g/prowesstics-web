"""Shared technical-overlay toolkit for corporate website imagery.
Coordinates are given in 'design units' (the grid image pixels); K scales them to output pixels."""
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

CYAN = (46, 230, 240)
GREEN = (60, 230, 140)
AMBER = (255, 184, 64)
RED = (255, 82, 82)
VIOLET = (180, 140, 255)
WHITE = (240, 248, 255)
SOFT = (159, 180, 211)
NAVY = (6, 19, 48)

_F = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
_FB = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
_FM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


class HUD:
    def __init__(self, src, design_width, out_width, fs=1.0):
        im = Image.open(src).convert("RGB")
        self.fs = fs
        self.K = out_width / design_width
        h = int(im.height * out_width / im.width)
        self.base = im.resize((out_width, h), Image.LANCZOS)
        self.ov = Image.new("RGBA", self.base.size, (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.ov)

    # ---- helpers ----
    def s(self, *v):
        return tuple(int(x * self.K) for x in v)

    def k(self, v):
        return int(v * self.K)

    def font(self, kind, size):
        p = {"r": _F, "b": _FB, "m": _FM}[kind]
        return ImageFont.truetype(p, max(8, int(size * self.K)))

    # ---- primitives ----
    def chip(self, x, y, text, color=CYAN, sub=None, size=12.5, solid=False, anchor="tl"):
        d, K = self.d, self.K
        size = size * self.fs
        f1 = self.font("b", size)
        f2 = self.font("m", size - 1.5)
        tw = d.textlength(text, font=f1)
        sw = d.textlength(sub, font=f2) if sub else 0
        cw = max(tw, sw) + self.k(20)
        ch = self.k(size * 1.9 + (size * 1.45 if sub else 0))
        a, b = self.s(x, y)
        if anchor == "bl":
            b -= ch
        elif anchor == "tr":
            a -= cw
        elif anchor == "br":
            a -= cw
            b -= ch
        fill = color + (255,) if solid else NAVY + (228,)
        d.rounded_rectangle((a, b, a + cw, b + ch), radius=self.k(6), fill=fill, outline=color + (255,), width=max(1, self.k(1.4)))
        d.text((a + self.k(10), b + self.k(size * 0.42)), text, font=f1, fill=(NAVY if solid else color) + (255,))
        if sub:
            d.text((a + self.k(10), b + self.k(size * 1.85)), sub, font=f2, fill=WHITE + (238,))
        return (a, b, a + cw, b + ch)

    def box(self, xy, color=GREEN, label=None, sub=None, conf=None, corner=24, w=3, pos="top"):
        d = self.d
        a, b, c, e = self.s(*xy)
        L = self.k(min(corner, (xy[2] - xy[0]) / 2.5, (xy[3] - xy[1]) / 2.5))
        lw = max(2, self.k(w))
        for (px, py, dx, dy) in [(a, b, 1, 1), (c, b, -1, 1), (a, e, 1, -1), (c, e, -1, -1)]:
            d.line([(px, py), (px + dx * L, py)], fill=color + (255,), width=lw)
            d.line([(px, py), (px, py + dy * L)], fill=color + (255,), width=lw)
        d.rectangle((a, b, c, e), outline=color + (90,), width=max(1, self.k(1)))
        if label:
            txt = label + (f"  {conf:.2f}" if conf is not None else "")
            if pos == "top":
                self.chip(xy[0], xy[1] - 6, txt, color, sub, anchor="bl")
            elif pos == "bottom":
                self.chip(xy[0], xy[3] + 6, txt, color, sub)
            elif pos == "right":
                self.chip(xy[2] + 8, xy[1], txt, color, sub)
            elif pos == "left":
                self.chip(xy[0] - 8, xy[1], txt, color, sub, anchor="tr")

    def poly(self, pts, color=CYAN, alpha=40, outline=True):
        P = [self.s(*p) for p in pts]
        self.d.polygon(P, fill=color + (alpha,))
        if outline:
            self.d.line(P + [P[0]], fill=color + (230,), width=max(2, self.k(2)))

    def line(self, pts, color=CYAN, w=2, alpha=255):
        self.d.line([self.s(*p) for p in pts], fill=color + (alpha,), width=max(1, self.k(w)), joint="curve")

    def dashed(self, p, q, color=CYAN, alpha=190, dash=9, gap=7, w=1.6):
        (xa, ya), (xb, yb) = self.s(*p), self.s(*q)
        n = max(1.0, np.hypot(xb - xa, yb - ya))
        step = (dash + gap) * self.K
        i = 0
        while i * step < n:
            t0 = i * step / n
            t1 = min(1, t0 + dash * self.K / n)
            self.d.line([(xa + (xb - xa) * t0, ya + (yb - ya) * t0), (xa + (xb - xa) * t1, ya + (yb - ya) * t1)], fill=color + (alpha,), width=max(1, self.k(w)))
            i += 1

    def dot(self, x, y, r=5, color=CYAN, ring=False):
        a, b = self.s(x, y)
        R = self.k(r)
        if ring:
            self.d.ellipse((a - R, b - R, a + R, b + R), outline=color + (255,), width=max(2, self.k(2.4)))
            r2 = max(2, R // 3)
            self.d.ellipse((a - r2, b - r2, a + r2, b + r2), fill=color + (255,))
        else:
            self.d.ellipse((a - R, b - R, a + R, b + R), fill=color + (255,), outline=WHITE + (255,), width=max(1, self.k(1.2)))

    def crosshair(self, x, y, r=34, color=CYAN):
        a, b = self.s(x, y)
        R = self.k(r)
        self.d.ellipse((a - R, b - R, a + R, b + R), outline=color + (255,), width=max(2, self.k(2)))
        self.d.ellipse((a - R // 2, b - R // 2, a + R // 2, b + R // 2), outline=color + (200,), width=max(1, self.k(1.5)))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            self.d.line([(a + dx * R * 0.6, b + dy * R * 0.6), (a + dx * R * 1.35, b + dy * R * 1.35)], fill=color + (255,), width=max(2, self.k(2)))

    def dim(self, p, q, text, color=CYAN, off=0):
        (xa, ya), (xb, yb) = self.s(*p), self.s(*q)
        d = self.d
        lw = max(1, self.k(1.5))
        d.line([(xa, ya), (xb, yb)], fill=color + (255,), width=lw)
        ang = np.arctan2(yb - ya, xb - xa) + np.pi / 2
        t = self.k(6)
        for (x, y) in [(xa, ya), (xb, yb)]:
            d.line([(x - np.cos(ang) * t, y - np.sin(ang) * t), (x + np.cos(ang) * t, y + np.sin(ang) * t)], fill=color + (255,), width=lw)
        f = self.font("m", 11 * self.fs)
        tw = d.textlength(text, font=f)
        mx, my = (xa + xb) / 2, (ya + yb) / 2 + self.k(off)
        d.rectangle((mx - tw / 2 - self.k(6), my - self.k(9), mx + tw / 2 + self.k(6), my + self.k(9)), fill=NAVY + (232,))
        d.text((mx - tw / 2, my - self.k(7)), text, font=f, fill=color + (255,))

    def panel(self, x, y, w, title, rows, color=CYAN, live=True, subtitle=None, spark=None, bars=None):
        d, f = self.d, self.fs
        w = w * f
        rowh = 21 * f
        h = (52 + (18 if subtitle else 0)) * f + len(rows) * rowh + (30 * f if spark or bars else 0) + 8 * f
        a, b = self.s(x, y)
        W, H = self.k(w), self.k(h)
        d.rounded_rectangle((a, b, a + W, b + H), radius=self.k(13 * f), fill=NAVY + (222,), outline=color + (185,), width=max(1, self.k(1.4 * f)))
        tx = a + self.k(18 * f)
        if live:
            d.ellipse((tx, b + self.k(21 * f), tx + self.k(9 * f), b + self.k(30 * f)), fill=RED + (255,))
            tx += self.k(17 * f)
        d.text((tx, b + self.k(14 * f)), title, font=self.font("b", 14.5 * f), fill=WHITE + (255,))
        yy = b + self.k(42 * f)
        if subtitle:
            d.text((a + self.k(18 * f), yy), subtitle, font=self.font("r", 11.5 * f), fill=SOFT + (255,))
            yy += self.k(20 * f)
        fm = self.font("m", 11.5 * f)
        for k_, v, *c in rows:
            col = c[0] if c else WHITE
            d.text((a + self.k(18 * f), yy), k_, font=fm, fill=SOFT + (255,))
            vw = d.textlength(v, font=fm)
            d.text((a + W - self.k(18 * f) - vw, yy), v, font=fm, fill=col + (255,))
            yy += self.k(rowh)
        if spark:
            vals, col = spark
            sx, sw, sh = a + self.k(18 * f), W - self.k(36 * f), self.k(18 * f)
            lo, hi = min(vals), max(vals)
            pts = [(sx + i * sw / (len(vals) - 1), yy + sh - (v - lo) / ((hi - lo) or 1) * sh) for i, v in enumerate(vals)]
            d.line(pts, fill=col + (255,), width=max(2, self.k(2 * f)))
        if bars:
            vals, col = bars
            sx, sw, sh = a + self.k(18 * f), W - self.k(36 * f), self.k(20 * f)
            bw = sw / len(vals)
            for i, v in enumerate(vals):
                bh = sh * v / max(vals)
                d.rectangle((sx + i * bw + self.k(1.5), yy + sh - bh, sx + (i + 1) * bw - self.k(1.5), yy + sh), fill=col + (230,))
        return (x, y, x + w, y + h)

    def flow(self, pts, color=CYAN, w=2.2, arrow=True, alpha=235):
        P = [self.s(*p) for p in pts]
        self.d.line(P, fill=color + (alpha,), width=max(2, self.k(w)))
        for p in P[1:-1]:
            r = self.k(3)
            self.d.ellipse((p[0] - r, p[1] - r, p[0] + r, p[1] + r), fill=color + (255,))
        if arrow:
            (x1, y1), (x2, y2) = P[-2], P[-1]
            ang = np.arctan2(y2 - y1, x2 - x1)
            L = self.k(11)
            for da in (2.6, -2.6):
                self.d.line([(x2, y2), (x2 + np.cos(ang + da) * L, y2 + np.sin(ang + da) * L)], fill=color + (255,), width=max(2, self.k(w)))

    def heat(self, blobs, alpha=0.55, region=None):
        """blobs: list of (x, y, radius, intensity 0..1). Draws a thermal-style heat map."""
        Wd, Hd = self.base.size
        hm = np.zeros((Hd, Wd), np.float32)
        yy, xx = np.mgrid[0:Hd, 0:Wd]
        for (x, y, r, it) in blobs:
            cx, cy = x * self.K, y * self.K
            R = r * self.K
            hm += it * np.exp(-(((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * (R / 2) ** 2)))
        hm = np.clip(hm, 0, 1)
        cm = cv2.applyColorMap((hm * 255).astype(np.uint8), cv2.COLORMAP_TURBO)[:, :, ::-1]
        a = (np.clip(hm * 1.6, 0, 1) * alpha * 255).astype(np.uint8)
        if region is not None:
            m = np.zeros_like(a)
            x0, y0, x1, y1 = self.s(*region)
            m[y0:y1, x0:x1] = 1
            a = a * m
        layer = Image.fromarray(np.dstack([cm, a]).astype(np.uint8), "RGBA")
        self.base = Image.alpha_composite(self.base.convert("RGBA"), layer).convert("RGB")

    def wireframe(self, xy, lo=50, hi=140, radius=16):
        x0, y0, x1, y1 = self.s(*xy)
        crop = np.asarray(self.base.crop((x0, y0, x1, y1)))
        g = cv2.GaussianBlur(cv2.cvtColor(crop, cv2.COLOR_RGB2GRAY), (5, 5), 0)
        e = cv2.dilate(cv2.Canny(g, lo, hi), np.ones((2, 2), np.uint8))
        dark = (crop * 0.28 + np.array(NAVY) * 0.55).astype(np.uint8)
        dark[e > 0] = CYAN
        wf = Image.fromarray(dark)
        m = Image.new("L", wf.size, 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, wf.width, wf.height), radius=self.k(radius), fill=255)
        m = m.filter(ImageFilter.GaussianBlur(self.k(3)))
        self.base.paste(wf, (x0, y0), m)
        self.d.rounded_rectangle((x0, y0, x1, y1), radius=self.k(radius), outline=CYAN + (255,), width=max(2, self.k(2)))

    def tint(self, xy, color, alpha=70):
        a, b, c, e = self.s(*xy)
        self.d.rectangle((a, b, c, e), fill=color + (alpha,))

    def note(self, text="Illustrative visualisation"):
        f = self.font("r", 10.5 * self.fs)
        tw = self.d.textlength(text, font=f)
        W, H = self.base.size
        a, b = self.k(18), H - self.k(34 * self.fs)
        self.d.rounded_rectangle((a, b, a + tw + self.k(16), b + self.k(22 * self.fs)), radius=self.k(5), fill=NAVY + (205,))
        self.d.text((a + self.k(8), b + self.k(4 * self.fs)), text, font=f, fill=(205, 218, 236, 235))

    def save(self, out, max_w=2400, q=88):
        img = Image.alpha_composite(self.base.convert("RGBA"), self.ov).convert("RGB")
        img.thumbnail((max_w, max_w), Image.LANCZOS)
        img.save(out, quality=q, optimize=True, progressive=True)
        return img
