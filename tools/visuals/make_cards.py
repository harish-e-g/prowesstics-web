import os
HERE = os.path.dirname(os.path.abspath(__file__))
SRCDIR = os.path.join(HERE, "src") + "/"   # place the untouched source photos here (see README.md)
OUT = os.path.join(HERE, "..", "..", "public", "images") + "/"
"""Card-size versions of product images: few callouts, large text. The full technical overlay is kept as IMG-xx-detail.jpg."""
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hud import *




SRC10 = SRCDIR + "SRC_IMG-10.png"

# IMG-10 ProVision AI (big card)
h = HUD(SRC10, 1672, 2752, fs=1.9)
h.wireframe((588, 500, 762, 672), radius=16)
h.box((812, 622, 1006, 752), GREEN, corner=24)
h.box((986, 578, 1138, 668), AMBER, corner=20)
h.dot(1078, 612, 12, RED, ring=True)
h.box((380, 238, 590, 420), GREEN, corner=22)
h.chip(20, 20, "SURFACE DEFECT  0.97", AMBER, "porosity 0.6 mm  ·  reject gate 2")
h.chip(20, 200, "2D → WIREFRAME", CYAN, "CAD match 99.1%")
h.chip(1650, 800, "HOUSING OK  0.99", GREEN, "bore Ø62.04 mm", anchor="tr")
h.chip(620, 250, "PPE  ✓", GREEN)
h.note("Illustrative visualisation")
h.save(OUT + "IMG-10.jpg")

# IMG-11 ProChurn AI (big card)
h = HUD(SRCDIR + "GAMMA_IMG-11.jpg", 1376, 2752, fs=1.9)
h.box((276, 262, 472, 532), CYAN, corner=24)
h.chip(1360, 20, "CHURN RISK  0.82", RED, "policy AU-20419", anchor="tr")
h.chip(1360, 190, "TOP DRIVER", AMBER, "claim delay 21 days", anchor="tr")
h.chip(20, 20, "RENEWALS 27% → 38%", GREEN, "62,624 policies")
h.note("Illustrative visualisation")
h.save(OUT + "IMG-11.jpg")

# IMG-12 DEO Suite: card and detail are drawn by make_deo.py

# IMG-13 ProSight AI (small card)
h = HUD(SRCDIR + "GAMMA_IMG-13.jpg", 1376, 2752, fs=2.4)
h.heat([(700, 470, 180, 0.95), (560, 560, 130, 0.75), (900, 560, 130, 0.8), (470, 330, 110, 0.55), (990, 400, 110, 0.6)], alpha=0.45, region=(340, 120, 1180, 768))
h.box((496, 300, 582, 600), GREEN, corner=18)
h.box((815, 420, 912, 700), GREEN, corner=18)
h.chip(20, 20, "FOOTFALL 4,812", CYAN, "heat map  ·  zone dwell")
h.chip(1360, 560, "OUT OF STOCK", AMBER, anchor="tr")
h.note("Illustrative visualisation")
h.save(OUT + "IMG-13.jpg")

# IMG-14 ProTrace AI (small card)
h = HUD(SRCDIR + "GAMMA_IMG-14.jpg", 1376, 2752, fs=2.4)
h.wireframe((640, 318, 818, 640), lo=40, hi=120, radius=14)
h.box((440, 305, 818, 692), GREEN, corner=26)
h.dashed((560, 168), (600, 380), RED, alpha=220, w=2.5)
h.chip(860, 20, "DMC READ  12 ms", CYAN, "PT-48213-0731")
h.chip(860, 260, "VARIANT B  ✓", GREEN, "poka-yoke armed")
h.note("Illustrative visualisation")
h.save(OUT + "IMG-14.jpg")

# IMG-15 Contact (wide strip)
h = HUD(SRCDIR + "GAMMA_IMG-15.jpg", 1376, 2752, fs=2.0)
h.box((618, 474, 848, 632), CYAN, corner=20)
h.chip(20, 20, "2-WEEK PILOT  ·  3 CAMERAS", CYAN, "your site  ·  your data")
h.chip(20, 220, "PAYBACK  2.7 months", GREEN, "indicative ProVision AI scenario")
h.note("Illustrative visualisation")
h.save(OUT + "IMG-15.jpg")
print("cards ok")
