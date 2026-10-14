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

# IMG-12 DEO Suite: card and detail are drawn by make_deo.py

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
