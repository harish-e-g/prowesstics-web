import os
HERE = os.path.dirname(os.path.abspath(__file__))
SRCDIR = os.path.join(HERE, "src") + "/"   # place the untouched source photos here (see README.md)
OUT = os.path.join(HERE, "..", "..", "public", "images") + "/"
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hud import *



only = sys.argv[1:]
def want(k): return not only or k in only
FS = 2.3  # industry cards render near 400 px wide, so text is scaled up

def H(name):
    return HUD(SRCDIR + name, 1376, 2752, fs=FS)

if want("IND-01"):
    h = H("GAMMA_IND-01.jpg")
    h.wireframe((852, 456, 966, 556), lo=40, hi=120, radius=10)
    h.box((846, 450, 972, 562), CYAN, corner=18)
    h.chip(560, 600, "PART Ø32.00 mm  ✓", CYAN, "CAD match 99.4%")
    h.box((776, 146, 968, 256), GREEN, corner=18)
    h.chip(990, 160, "PPE  ✓ 0.98", GREEN)
    h.chip(20, 20, "CNC-04  OEE 86%", GREEN, "spindle load 78%")
    h.note("Illustrative")
    h.save(OUT + "IND-01.jpg")

if want("IND-02"):
    h = H("GAMMA_IND-02.jpg")
    h.box((370, 370, 530, 510), AMBER, corner=20)
    for (x, y) in [(150, 470), (300, 520), (600, 470), (650, 560), (230, 600)]:
        h.dot(x, y, 8, CYAN, ring=True)
    h.chip(20, 20, "WELD SEAM W-14  ✓", AMBER, "bead 4.2 mm")
    h.chip(20, 520, "212 / 212 SPOT WELDS", CYAN, "gap ±0.5 mm")
    h.box((896, 232, 1012, 304), GREEN, corner=14)
    h.chip(1040, 140, "PPE  ✓", GREEN)
    h.note("Illustrative")
    h.save(OUT + "IND-02.jpg")

if want("IND-03"):
    h = H("GAMMA_IND-03.jpg")
    h.box((912, 160, 1266, 490), CYAN, corner=26)
    h.dot(968, 340, 9, CYAN, ring=True)
    h.chip(20, 20, "CHURN RISK  0.82", RED, "policy AU-20419")
    h.chip(20, 220, "TOP DRIVER", AMBER, "claim delay 21 days")
    h.chip(1360, 540, "SAVE RATE 68%", GREEN, anchor="tr")
    h.note("Illustrative")
    h.save(OUT + "IND-03.jpg")

if want("IND-04"):
    h = H("GAMMA_IND-04.jpg")
    h.box((538, 276, 708, 424), CYAN, corner=18)
    h.box((326, 208, 566, 406), AMBER, corner=20)
    h.box((846, 146, 994, 664), GREEN, corner=22)
    h.chip(20, 20, "DWELL 3 h 40 m", AMBER, "SLA 3 h  ·  detention risk")
    h.chip(560, 440, "FORKLIFT FL-07", CYAN)
    h.chip(1020, 200, "PPE  ✓", GREEN)
    h.chip(20, 600, "DOCK D2  ·  OTIF 96.4%", CYAN)
    h.note("Illustrative")
    h.save(OUT + "IND-04.jpg")

if want("IND-05"):
    h = H("GAMMA_IND-05.jpg")
    h.heat([(560, 640, 150, 0.8), (800, 660, 140, 0.9), (980, 600, 120, 0.6)], alpha=0.4, region=(360, 520, 1100, 768))
    h.box((458, 192, 618, 728), GREEN, corner=22)
    h.box((706, 154, 894, 694), GREEN, corner=22)
    h.box((1078, 372, 1376, 504), AMBER, corner=18)
    h.chip(20, 20, "SHOPPER 0412  ·  2 m 10 s", GREEN)
    h.chip(20, 130, "CONVERSION 31%", CYAN)
    h.chip(1360, 530, "SHELF GAP 12%", AMBER, anchor="tr")
    h.note("Illustrative")
    h.save(OUT + "IND-05.jpg")

if want("IND-06"):
    h = H("GAMMA_IND-06.jpg")
    h.box((1056, 636, 1116, 716), CYAN, corner=12)
    h.chip(1030, 20, "HR 72 bpm  ✓", GREEN, "ECG streaming")
    h.chip(1030, 150, "AF burden 0.4%", CYAN)
    h.chip(560, 560, "RPM PATCH  ·  250 Hz", CYAN)
    h.note("Illustrative")
    h.save(OUT + "IND-06.jpg")

if want("IND-07"):
    h = H("GAMMA_IND-07.jpg")
    h.heat([(640, 470, 80, 0.95), (560, 650, 55, 0.6)], alpha=0.65, region=(440, 300, 900, 768))
    h.box((580, 414, 706, 526), RED, corner=18)
    h.chip(20, 400, "HOTSPOT +18 °C", RED, "string 14  ·  cell crack")
    h.chip(20, 20, "OUTPUT 38.6 MW", GREEN, "PR 81.4%")
    h.chip(20, 590, "SOILING 6%", AMBER)
    h.note("Illustrative")
    h.save(OUT + "IND-07.jpg")

if want("IND-08"):
    h = H("GAMMA_IND-08.jpg")
    h.crosshair(870, 250, 40, CYAN)
    h.line([(870, 110), (870, 640)], CYAN, w=2, alpha=190)
    h.box((736, 176, 1114, 704), CYAN, corner=26)
    h.chip(20, 20, "CHUTE OFFSET 4 mm  ✓", GREEN, "within ±10 mm")
    h.chip(20, 160, "ALIGN 4 h → 15 min", CYAN)
    h.chip(1360, 600, "PPE  ✓", GREEN, anchor="tr")
    h.note("Illustrative")
    h.save(OUT + "IND-08.jpg")

if want("IND-09"):
    h = H("GAMMA_IND-09.jpg")
    h.box((24, 262, 336, 596), CYAN, corner=24)
    h.chip(860, 20, "BOOKINGS 214", CYAN, "conversion 18.2%")
    h.chip(860, 160, "CANCEL RISK 0.08", GREEN)
    h.chip(30, 610, "AGENTIC AI ITINERARY", CYAN)
    h.note("Illustrative")
    h.save(OUT + "IND-09.jpg")
print("ok")
