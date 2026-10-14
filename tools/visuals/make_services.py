import os
HERE = os.path.dirname(os.path.abspath(__file__))
SRCDIR = os.path.join(HERE, "src") + "/"   # place the untouched source photos here (see README.md)
OUT = os.path.join(HERE, "..", "..", "public", "images") + "/"
"""Service card visuals: real product cut-out + data callouts + flow line, on a transparent 1200 x 640 canvas."""
from PIL import Image, ImageDraw, ImageFont
import numpy as np



SRC = SRCDIR
FB = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
FM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
NAVY = (6, 19, 48)
W, H = 1200, 640

def chip(d, x, y, title, sub, col, anchor="l"):
    f1 = ImageFont.truetype(FB, 46)
    f2 = ImageFont.truetype(FM, 32)
    tw = d.textlength(title, font=f1)
    sw = d.textlength(sub, font=f2) if sub else 0
    cw = max(tw, sw) + 44
    ch = 72 + (46 if sub else 0)
    if anchor == "r":
        x -= cw
    d.rounded_rectangle((x + 6, y + 8, x + cw + 6, y + ch + 8), radius=18, fill=(6, 19, 48, 60))
    d.rounded_rectangle((x, y, x + cw, y + ch), radius=18, fill=NAVY + (238,), outline=col + (255,), width=3)
    d.text((x + 22, y + 12), title, font=f1, fill=col + (255,))
    if sub:
        d.text((x + 22, y + 70), sub, font=f2, fill=(232, 242, 255, 240))
    return (x, y, x + cw, y + ch)

def flow(d, pts, col):
    d.line(pts, fill=col + (230,), width=4, joint="curve")
    for p in pts:
        d.ellipse((p[0] - 7, p[1] - 7, p[0] + 7, p[1] + 7), fill=col + (255,), outline=(255, 255, 255, 255), width=2)

def make(slot, obj, color, chips, obj_box=(40, 70, 640, 600)):
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    o = Image.open(obj).convert("RGBA")
    bw, bh = obj_box[2] - obj_box[0], obj_box[3] - obj_box[1]
    o.thumbnail((bw, bh), Image.LANCZOS)
    ox = obj_box[0] + (bw - o.width) // 2
    oy = obj_box[1] + (bh - o.height) // 2
    canvas.alpha_composite(o, (ox, oy))
    d = ImageDraw.Draw(canvas)
    anchor_pt = (ox + o.width - 20, oy + o.height // 2)
    boxes = []
    for i, (t, s, c) in enumerate(chips):
        y = 40 + i * 190
        boxes.append(chip(d, W - 20, y, t, s, c, anchor="r"))
    for b in boxes:
        flow(d, [anchor_pt, (b[0] - 40, (b[1] + b[3]) // 2), (b[0], (b[1] + b[3]) // 2)], color)
    canvas.save(OUT + slot + ".png", optimize=True)

CY = (16, 160, 184)
BL = (37, 99, 235)
OR = (232, 137, 43)
VI = (124, 58, 237)
GR = (20, 150, 94)
RD = (217, 54, 74)
SB = (26, 127, 224)
GD = (183, 134, 26)

make("IMG-02", SRC + "IMG-02.png", CY, [("ETL 1.2M rows/min", "Bronze → Silver → Gold", CY), ("QUALITY 99.6% pass", "drift checks on 30+ feeds", GR), ("ETL < 90 min", "down from 8 to 12 h", CY)])
make("IMG-03", SRC + "IMG-03.png", BL, [("30+ DASHBOARDS", "Power BI · Direct Lake", BL), ("REFRESH < 20 min", "one trusted KPI model", GR), ("CXO SCORECARD", "role-based access", BL)])
make("IMG-04", SRC + "IMG-04.png", OR, [("MATILLION → GLUE", "zero-downtime cut-over", OR), ("RUNTIME −40%", "licence cost removed", GR), ("AZURE · AWS · GCP", "cloud-native", OR)])
make("IMG-05", SRC + "IMG-05.png", VI, [("ROC AUC 0.92", "churn model in production", VI), ("INFERENCE 42 ms", "edge GPU", GR), ("GenAI · RAG · AGENTS", "grounded on your data", VI)])
make("IMG-06", SRC + "IMG-06.png", GR, [("DEFECT 0.97", "porosity 0.6 mm", (232, 137, 43)), ("PPE  ✓ 0.98", "zone B compliant", GR), ("64 USE CASES", "< 100 ms alerts", GR)])
make("IMG-07", SRC + "IMG-07.png", RD, [("POKA-YOKE ARMED", "variant B confirmed", GR), ("CYCLE 4 h → 15 min", "automated station", RD), ("PLC · SCADA · MES", "wired to SAP", RD)])
make("IMG-08", SRC + "IMG-08.png", SB, [("UPTIME 99.5%+", "pipelines across mills", GR), ("ALERT → ON-CALL", "ack in minutes", SB), ("SLA 24 × 7", "monitored runs", SB)])
make("IMG-09", SRC + "IMG-09.png", GD, [("60+ CERTIFIED", "data · BI · ML · QA", GD), ("JOINS YOUR SPRINT", "your stack, your cadence", GR), ("SNOWFLAKE · POWER BI", "Python · Azure · AWS", GD)])
print("services ok")
