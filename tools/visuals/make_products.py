import os
HERE = os.path.dirname(os.path.abspath(__file__))
SRCDIR = os.path.join(HERE, "src") + "/"   # place the untouched source photos here (see README.md)
OUT = os.path.join(HERE, "..", "..", "public", "images") + "/"
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hud import *




# ---------------- IMG-11  ProChurn AI ----------------
h = HUD(SRCDIR + "GAMMA_IMG-11.jpg", 1376, 2752)
h.box((276, 262, 472, 532), CYAN, "CHURN SCORING  LIVE", None, None, corner=22, pos="top")
h.panel(1060, 30, 300, "PROCHURN AI  ·  SAVE QUEUE", [
    ("AU-20419  motor", "risk 0.82", RED),
    ("AU-18877  motor", "risk 0.74", AMBER),
    ("HL-21102  health", "risk 0.61", AMBER),
    ("Model ROC AUC", "0.92", GREEN),
    ("Lead time", "10 to 45 days"),
    ("Renewal rate", "27% → 38%", GREEN),
], subtitle="Insurer book  ·  62,624 policies scored", bars=([3, 5, 9, 14, 22, 30, 24, 15, 8, 4], CYAN))
p = h.panel(18, 30, 260, "CUSTOMER 360  ·  AU-20419", [
    ("Claim delay 21 d", "+0.31", RED),
    ("Premium hike 14%", "+0.22", AMBER),
    ("No app login 45 d", "+0.17", AMBER),
    ("Next best action", "RM call + offer"),
    ("Save probability", "0.68", GREEN),
], live=False, subtitle="Top 3 churn drivers (SHAP)")
h.dashed((278, 140), (438, 392), CYAN)
h.dot(438, 392, 6, CYAN, ring=True)
h.flow([(472, 262), (520, 74), (1060, 74)], CYAN, w=1.8)
h.note("Illustrative visualisation of ProChurn AI retention scoring")
h.save(OUT + "IMG-11-detail.jpg")

# ---------------- IMG-12  DEO Suite ----------------
h = HUD(SRCDIR + "SRC_IMG-12.png", 1672, 3344)
h.box((598, 552, 832, 746), GREEN, "TRK TN-09-4821", "gate-in 18:42  ·  OTIF on track", 0.98, pos="top")
h.box((878, 522, 1028, 632), CYAN, "MSKU 4821137", "ETA berth 3  19:05", 0.97, corner=18, pos="top")
h.box((378, 656, 562, 852), AMBER, "DWELL 3 h 40 m", "SLA 3 h  ·  detention risk", 0.96, pos="top")
h.box((1002, 298, 1312, 500), CYAN, "VESSEL  BERTH 3", "1,840 TEU  ·  discharge 62%", None, corner=26, pos="top")
# unified data layer panel with system chips
x0, y0 = 18, 18
h.d.rounded_rectangle(h.s(x0, y0, x0 + 560, y0 + 196), radius=h.k(13), fill=NAVY + (222,), outline=CYAN + (185,), width=h.k(1.4))
h.d.ellipse(h.s(x0 + 18, y0 + 21, x0 + 27, y0 + 30), fill=RED + (255,))
h.d.text(h.s(x0 + 35, y0 + 13), "DEO SUITE  ·  UNIFIED DATA LAYER", font=h.font("b", 14.5), fill=WHITE + (255,))
h.d.text(h.s(x0 + 18, y0 + 40), "10 operational systems  →  one governed model  →  live reporting", font=h.font("r", 11.5), fill=SOFT + (255,))
systems = ["WMS", "TMS", "YMS", "OMS", "LMS", "GTM", "FAP", "FLEET", "TOWER", "ERP"]
for i, sname in enumerate(systems):
    cx = x0 + 18 + (i % 5) * 64
    cy = y0 + 66 + (i // 5) * 34
    h.d.rounded_rectangle(h.s(cx, cy, cx + 56, cy + 26), radius=h.k(5), fill=CYAN + (40,), outline=CYAN + (255,), width=h.k(1.2))
    f = h.font("b", 10.5)
    tw = h.d.textlength(sname, font=f)
    h.d.text((h.k(cx + 28) - tw / 2, h.k(cy + 6)), sname, font=f, fill=WHITE + (255,))
h.flow([(x0 + 338, y0 + 96), (x0 + 372, y0 + 96)], CYAN, w=2)
for j, (lbl, col) in enumerate([("BRONZE", AMBER), ("SILVER", SOFT), ("GOLD", (232, 180, 82))]):
    cx = x0 + 380 + j * 60
    h.d.rounded_rectangle(h.s(cx, y0 + 80, cx + 52, y0 + 112), radius=h.k(5), fill=col + (60,), outline=col + (255,), width=h.k(1.2))
    f = h.font("b", 9.5)
    tw = h.d.textlength(lbl, font=f)
    h.d.text((h.k(cx + 26) - tw / 2, h.k(y0 + 89)), lbl, font=f, fill=WHITE + (255,))
fm = h.font("m", 11.5)
h.d.text(h.s(x0 + 18, y0 + 146), "Refresh  continuous  ·  < 20 min end to end", font=fm, fill=GREEN + (255,))
h.d.text(h.s(x0 + 18, y0 + 168), "Outputs  Power BI · Fabric · SLA alerts", font=fm, fill=WHITE + (235,))
h.panel(1290, 18, 364, "CONTROL TOWER  ·  LIVE", [
    ("OTIF today", "96.4 %", GREEN),
    ("Avg yard dwell", "2 h 12 m"),
    ("Detention risk", "3 trucks", AMBER),
    ("Open exceptions", "7", AMBER),
    ("Data freshness", "4 min ago", GREEN),
], live=False, spark=([92.1, 93.4, 94.0, 95.2, 94.8, 95.9, 96.4], GREEN))
h.flow([(1200, 650), (1236, 600), (1236, 232), (1290, 196)], CYAN, w=1.8)
h.note("Illustrative visualisation of DEO Suite logistics control tower")
h.save(OUT + "IMG-12-detail.jpg")

# ---------------- IMG-13  ProSight AI ----------------
h = HUD(SRCDIR + "GAMMA_IMG-13.jpg", 1376, 2752)
h.heat([(700, 470, 180, 0.95), (560, 560, 130, 0.75), (900, 560, 130, 0.8), (470, 330, 110, 0.55),
        (990, 400, 110, 0.6), (760, 250, 90, 0.45), (620, 680, 120, 0.5), (1060, 620, 120, 0.45)],
       alpha=0.42, region=(340, 120, 1180, 768))
h.poly([(560, 140), (835, 140), (840, 535), (558, 535)], CYAN, alpha=18)
h.chip(845, 150, "ZONE P1  PRODUCE", CYAN, "avg dwell 2 m 48 s  ·  conversion 34%")
for (xy, lbl, sub) in [((496, 300, 582, 600), "ID 0412", "dwell 3 m 12 s"),
                       ((815, 420, 912, 700), "ID 0388", "basket  ·  2 items"),
                       ((226, 395, 330, 668), "ID 0451", "aisle A4"),
                       ((996, 286, 1092, 500), "ID 0397", "trolley  ·  frozen")]:
    h.box(xy, GREEN, lbl, sub, None, corner=16, pos="top")
h.dashed((1150, 55), (560, 140), CYAN)
h.dashed((1150, 55), (1180, 520), CYAN)
h.chip(1180, 80, "CAM-14  ceiling dome", CYAN, anchor="tr")
h.box((1300, 470, 1372, 560), AMBER, "OUT OF STOCK", "SKU 81124  ·  shelf B3", None, corner=12, pos="left")
h.panel(18, 18, 300, "PROSIGHT AI  ·  STORE 14", [
    ("Footfall today", "4,812"),
    ("Peak hour", "18:00 to 19:00"),
    ("Avg store dwell", "11 m 40 s"),
    ("Affinity  bananas → milk", "0.41", GREEN),
    ("Out-of-stock alerts", "3", AMBER),
    ("Identity data stored", "none", GREEN),
], subtitle="Anonymous tracking  ·  heat map", bars=([4, 6, 9, 13, 18, 24, 31, 27, 19], CYAN))
h.note("Illustrative visualisation of ProSight AI footfall and heat map analytics")
h.save(OUT + "IMG-13-detail.jpg")
print("done")

# ---------------- IMG-14  ProTrace AI ----------------
h = HUD(SRCDIR + "GAMMA_IMG-14.jpg", 1376, 2752)
h.wireframe((640, 318, 818, 640), lo=40, hi=120, radius=14)
h.box((440, 305, 818, 692), GREEN, "HOUSING  VARIANT B", "serial PT-48213-0731", 0.99, corner=26, pos="bottom")
h.chip(380, 214, "DMC READ  ·  grade A  ·  12 ms", CYAN, "PT-48213-0731  ·  lot H-3317")
h.dashed((560, 168), (600, 380), RED, alpha=220)
h.chip(830, 600, "2D → WIREFRAME  ·  bore Ø48.02 mm", CYAN, anchor="tl")
h.dim((652, 330), (812, 470), "48.02 mm", CYAN, off=-14)
h.panel(860, 26, 500, "PROTRACE AI  ·  PART GENEALOGY", [
    ("OP10  casting      H-3317", "08:12  ✓", GREEN),
    ("OP20  CNC rough    ST-04", "09:05  ✓", GREEN),
    ("OP30  leak test    0.8 mbar", "09:41  ✓", GREEN),
    ("OP40  torque       24.8 Nm", "10:02  ✓", GREEN),
    ("OP50  vision QC    0 defects", "10:06  ✓", GREEN),
    ("OP60  pack         → SAP", "10:11  ✓", GREEN),
], subtitle="Station ST-07  ·  every operation logged against the serial")
h.chip(860, 340, "POKA-YOKE  ·  variant B confirmed", GREEN, "wrong-part interlock armed  ·  PLC ack 8 ms")
h.panel(18, 26, 300, "TRACEABILITY  ·  LINE 2", [
    ("Parts traced today", "3,412"),
    ("Coverage", "100 %", GREEN),
    ("Mismatch stopped", "2", AMBER),
    ("Recall lookup", "< 1 s", GREEN),
], live=True)
h.note("Illustrative visualisation of ProTrace AI traceability and poka-yoke")
h.save(OUT + "IMG-14-detail.jpg")

# ---------------- IMG-15  Contact / pilot review ----------------
h = HUD(SRCDIR + "GAMMA_IMG-15.jpg", 1376, 2752)
h.box((618, 474, 848, 632), CYAN, "PILOT RESULTS  ·  WEEK 2", None, None, corner=18, pos="top")
h.panel(18, 26, 360, "PILOT REVIEW  ·  LINE 3", [
    ("OEE", "81% → 87%", GREEN),
    ("Defect escapes (ppm)", "420 → 38", GREEN),
    ("Manual inspection h/wk", "96 → 30", GREEN),
    ("Payback", "4.1 months", GREEN),
    ("Decision", "scale to 3 lines", CYAN),
], live=False, subtitle="ProVision AI  ·  2-week pilot on 3 cameras", spark=([78, 79, 81, 82, 84, 85, 87], GREEN))
h.flow([(618, 500), (500, 470), (378, 200)], CYAN, w=1.8)
h.note("Illustrative visualisation of a pilot review")
h.save(OUT + "IMG-15-detail.jpg")
print("done 14 15")
