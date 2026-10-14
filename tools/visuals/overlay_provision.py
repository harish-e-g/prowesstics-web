import os
HERE = os.path.dirname(os.path.abspath(__file__))
SRCDIR = os.path.join(HERE, "src") + "/"   # place the untouched source photos here (see README.md)
OUT = os.path.join(HERE, "..", "..", "public", "images") + "/"
"""Technical overlay for the ProVision AI image: detections, defect callout, PPE checks,
2D-to-wireframe conversion of the handheld part, camera field of view, live inspection HUD."""
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = SRCDIR + "SRC_IMG-10.png"
DEST = OUT + "IMG-10-detail.jpg"
K = 2  # work at 2x for crisp lines

CYAN = (46, 230, 240)
GREEN = (60, 230, 140)
AMBER = (255, 184, 64)
RED = (255, 82, 82)
WHITE = (240, 248, 255)
NAVY = (6, 19, 48)

F = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
FB = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
FM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
def font(p, s): return ImageFont.truetype(p, int(s * K))

base = Image.open(SRC).convert("RGB")
base = base.resize((base.width * K, base.height * K), Image.LANCZOS)
W, H = base.size
s = lambda *v: tuple(int(x * K) for x in v)

# ---------- 1. 2D to wireframe on the handheld part ----------
x0, y0, x1, y1 = s(588, 500, 762, 672)
crop = np.asarray(base.crop((x0, y0, x1, y1)))
gray = cv2.cvtColor(crop, cv2.COLOR_RGB2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(gray, 50, 140)
edges = cv2.dilate(edges, np.ones((2, 2), np.uint8))
dark = (crop * 0.28 + np.array(NAVY) * 0.55).astype(np.uint8)
dark[edges > 0] = CYAN
wf = Image.fromarray(dark)
# soft mask so the wireframe blends into the photo
mask = Image.new("L", wf.size, 0)
ImageDraw.Draw(mask).rounded_rectangle((0, 0, wf.width, wf.height), radius=int(18 * K), fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(4 * K))
base.paste(wf, (x0, y0), mask)

ov = Image.new("RGBA", base.size, (0, 0, 0, 0))
d = ImageDraw.Draw(ov)

def box(xy, color, label, sub=None, conf=None, w=3, corner=26, pos="top"):
    a, b, c, e = s(*xy)
    # corner brackets instead of a full rectangle, like a real vision HUD
    L = int(corner * K)
    for (px, py, dx, dy) in [(a, b, 1, 1), (c, b, -1, 1), (a, e, 1, -1), (c, e, -1, -1)]:
        d.line([(px, py), (px + dx * L, py)], fill=color + (255,), width=int(w * K))
        d.line([(px, py), (px, py + dy * L)], fill=color + (255,), width=int(w * K))
    d.rectangle((a, b, c, e), outline=color + (110,), width=int(1 * K))
    # label chip
    f1 = font(FB, 13); f2 = font(FM, 11.5)
    txt = label + (f"  {conf:.2f}" if conf is not None else "")
    tw = d.textlength(txt, font=f1)
    sw = d.textlength(sub, font=f2) if sub else 0
    cw = max(tw, sw) + 20 * K
    ch = (24 if not sub else 42) * K
    ly = b - ch - 6 * K if pos == "top" else e + 6 * K
    if pos == "none": return
    d.rounded_rectangle((a, ly, a + cw, ly + ch), radius=int(6 * K), fill=NAVY + (225,), outline=color + (255,), width=int(1.5 * K))
    d.text((a + 10 * K, ly + 5 * K), txt, font=f1, fill=color + (255,))
    if sub:
        d.text((a + 10 * K, ly + 23 * K), sub, font=f2, fill=WHITE + (235,))

def dashed(p, q, color, alpha=160, dash=10, gap=8, width=1.5):
    (xa, ya), (xb, yb) = s(*p), s(*q)
    n = np.hypot(xb - xa, yb - ya); steps = int(n // ((dash + gap) * K))
    for i in range(steps + 1):
        t0 = i * (dash + gap) * K / n; t1 = min(1, t0 + dash * K / n)
        d.line([(xa + (xb - xa) * t0, ya + (yb - ya) * t0), (xa + (xb - xa) * t1, ya + (yb - ya) * t1)], fill=color + (alpha,), width=int(width * K))

# ---------- 2. Camera fields of view ----------
for cam, tgt in [((1070, 262), [(812, 640), (1010, 640)]), ((1340, 232), [(985, 585), (1225, 585)])]:
    poly = [s(*cam), s(*tgt[1]), s(*tgt[0])]
    d.polygon(poly, fill=CYAN + (22,))
    dashed(cam, tgt[0], CYAN); dashed(cam, tgt[1], CYAN)
for (tx, ty, tl) in [(1122, 140, "CAM-07  4K  30 fps"), (1395, 110, "CAM-08  4K  30 fps")]:
    fx = font(FM, 11.5); tw = d.textlength(tl, font=fx); a_, b_ = s(tx, ty)
    d.rounded_rectangle((a_, b_, a_ + tw + 16 * K, b_ + 22 * K), radius=int(5 * K), fill=NAVY + (225,), outline=CYAN + (255,), width=int(1.2 * K))
    d.text((a_ + 8 * K, b_ + 4 * K), tl, font=fx, fill=CYAN + (255,))

# ---------- 3. Detections on the conveyor ----------
box((812, 622, 1006, 752), GREEN, "HOUSING  OK", "EH-48213  bore Ø62.04 mm  ±0.02", 0.99, pos="bottom")
box((986, 578, 1138, 668), AMBER, "SURFACE DEFECT", "porosity 0.6 mm  reject gate 2", 0.97)
# defect pinpoint
cx, cy = s(1078, 612)
r = int(11 * K)
d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=RED + (255,), width=int(2.5 * K))
d.ellipse((cx - 3 * K, cy - 3 * K, cx + 3 * K, cy + 3 * K), fill=RED + (255,))

# ---------- 4. PPE checks on the operator ----------
box((380, 238, 590, 420), GREEN, "PPE  SAFETY GLASSES", "zone B  compliant", 0.98, pos="bottom")
box((462, 548, 586, 690), GREEN, "PPE  GLOVES", None, 0.96, corner=18, pos="bottom")

# ---------- 5. Wireframe annotations on the handheld part ----------
a, b, c, e = s(588, 500, 762, 672)
d.rounded_rectangle((a, b, c, e), radius=int(18 * K), outline=CYAN + (255,), width=int(2 * K))
f_s = font(FM, 11)
# width dimension line
yy = e + 16 * K
d.line([(a, yy), (c, yy)], fill=CYAN + (255,), width=int(1.5 * K))
for xx in (a, c): d.line([(xx, yy - 6 * K), (xx, yy + 6 * K)], fill=CYAN + (255,), width=int(1.5 * K))
lbl = "84.2 mm"; tw = d.textlength(lbl, font=f_s)
d.rectangle(((a + c) / 2 - tw / 2 - 6 * K, yy - 9 * K, (a + c) / 2 + tw / 2 + 6 * K, yy + 9 * K), fill=NAVY + (230,))
d.text(((a + c) / 2 - tw / 2, yy - 7 * K), lbl, font=f_s, fill=CYAN + (255,))
# keypoints
for kx, ky in [(612, 528), (735, 535), (742, 640), (620, 650), (668, 585)]:
    px, py = s(kx, ky); rr = int(4 * K)
    d.ellipse((px - rr, py - rr, px + rr, py + rr), fill=CYAN + (255,), outline=WHITE + (255,))
# chip
chip = "2D → EDGE WIREFRAME  ·  214 features  ·  CAD match 99.1%"
f_c = font(FB, 12)
tw = d.textlength(chip, font=f_c)
d.rounded_rectangle((a, b - 34 * K, a + tw + 20 * K, b - 8 * K), radius=int(6 * K), fill=NAVY + (230,), outline=CYAN + (255,), width=int(1.5 * K))
d.text((a + 10 * K, b - 30 * K), chip, font=f_c, fill=CYAN + (255,))

# ---------- 6. Live inspection HUD (top left) ----------
px0, py0 = s(22, 22)
pw, ph = int(340 * K), int(236 * K)
d.rounded_rectangle((px0, py0, px0 + pw, py0 + ph), radius=int(14 * K), fill=NAVY + (215,), outline=CYAN + (180,), width=int(1.5 * K))
d.ellipse((px0 + 18 * K, py0 + 22 * K, px0 + 28 * K, py0 + 32 * K), fill=RED + (255,))
d.text((px0 + 36 * K, py0 + 15 * K), "PROVISION AI  ·  LIVE", font=font(FB, 16), fill=WHITE + (255,))
d.text((px0 + 18 * K, py0 + 44 * K), "Line 3  ·  Station QC-02  ·  Shift B", font=font(F, 12), fill=(159, 180, 211, 255))
rows = [("Inference", "42 ms  edge GPU"), ("Inspected today", "1,284"), ("OK / NG", "1,277 / 7"), ("First-pass yield", "99.45 %"), ("PPE compliance", "100 %"), ("Trace ID", "PT-20261014-0482")]
fm = font(FM, 12)
for i, (k_, v) in enumerate(rows):
    yy = py0 + (72 + i * 22) * K
    d.text((px0 + 18 * K, yy), k_, font=fm, fill=(159, 180, 211, 255))
    vw = d.textlength(v, font=fm)
    col = AMBER if k_ == "OK / NG" else (GREEN if "%" in v else WHITE)
    d.text((px0 + pw - 18 * K - vw, yy), v, font=fm, fill=col + (255,))
# yield sparkline
sx, sy, sw, sh = px0 + 18 * K, py0 + 210 * K, pw - 36 * K, 16 * K
vals = [99.1, 99.3, 99.2, 99.5, 99.4, 99.6, 99.3, 99.5, 99.45]
pts = [(sx + i * sw / (len(vals) - 1), sy + sh - (v - 99.0) / 0.7 * sh) for i, v in enumerate(vals)]
d.line(pts, fill=GREEN + (255,), width=int(2 * K))

# ---------- 7. Event stream (bottom right) ----------
ex0, ey0 = s(1262, 742)
ew, eh = int(392 * K), int(178 * K)
d.rounded_rectangle((ex0, ey0, ex0 + ew, ey0 + eh), radius=int(14 * K), fill=NAVY + (215,), outline=CYAN + (180,), width=int(1.5 * K))
d.text((ex0 + 18 * K, ey0 + 14 * K), "EVENT STREAM  →  MES · SAP QM · WhatsApp", font=font(FB, 12.5), fill=WHITE + (255,))
ev = [("14:32:07", "NG", "porosity  EH-48214  → reject gate 2", AMBER),
      ("14:32:05", "OK", "EH-48213  dims within tolerance", GREEN),
      ("14:31:58", "PPE", "zone B  glasses + gloves verified", GREEN),
      ("14:31:52", "ALERT", "QC lead notified  ·  ack 6 s", CYAN)]
for i, (t, tag, msg, col) in enumerate(ev):
    yy = ey0 + (44 + i * 30) * K
    d.text((ex0 + 18 * K, yy), t, font=font(FM, 11.5), fill=(159, 180, 211, 255))
    d.rounded_rectangle((ex0 + 92 * K, yy - 2 * K, ex0 + 142 * K, yy + 17 * K), radius=int(4 * K), fill=col + (255,))
    tw = d.textlength(tag, font=font(FB, 10))
    d.text((ex0 + 117 * K - tw / 2, yy + 1 * K), tag, font=font(FB, 10), fill=NAVY + (255,))
    d.text((ex0 + 152 * K, yy), msg, font=font(FM, 11), fill=WHITE + (235,))

# ---------- 8. Honesty note ----------
nt = "Illustrative visualisation of ProVision AI inspection output"; fn = font(F, 10.5); tw = d.textlength(nt, font=fn)
d.rounded_rectangle(s(20, 904) + (int(20*K + tw + 16*K), int(926*K)), radius=int(5*K), fill=NAVY + (200,))
d.text(s(28, 908), nt, font=fn, fill=(200, 215, 235, 230))

out = Image.alpha_composite(base.convert("RGBA"), ov).convert("RGB")
out.thumbnail((2400, 2400), Image.LANCZOS)
out.save(DEST, quality=88, optimize=True, progressive=True)
print(out.size)
