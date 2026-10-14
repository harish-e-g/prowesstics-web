import os, sys
V = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, V)
from hud import *
SRC = os.path.join(V, "src", "GAMMA_IMG-12_DEO.jpg")
OUT = os.path.join(V, "..", "..", "public", "images") + "/"
# design space 1376 x 768. DAG on left monitor ~ (681-915, 340-471); slow node ~ (801-833, 380-394)
# card (big)
h = HUD(SRC, 1376, 2752, fs=1.9)
h.box((672, 326, 924, 482), CYAN, corner=22)
h.box((794, 372, 840, 400), AMBER, corner=10, w=3)
h.chip(18, 18, "PIPELINE HEALTH  ·  214 JOBS", CYAN, "3 slow  ·  1 schema drift")
h.chip(18, 196, "stg_orders  47 min", AMBER, "rebuilt  →  6 min")
h.chip(1358, 18, "ETL 8–12 h → <90 min", GREEN, "freshness SLA met", anchor="tr")
h.note("Illustrative visualisation")
h.save(OUT + "IMG-12.jpg")
# detail
h = HUD(SRC, 1376, 2752)
h.box((672, 326, 924, 482), CYAN, "DAG  daily_sales_load", "214 tasks  ·  run 06:00 IST", None, corner=18, pos="top")
h.box((794, 372, 840, 400), AMBER, None, None, None, corner=8, w=2)
h.box((966, 300, 1262, 568), GREEN, "RUNTIME + COST TREND", "last 30 runs", None, corner=18, pos="top")
h.panel(18, 18, 330, "DEO SUITE  ·  PIPELINE PROFILER", [
    ("stg_orders", "47 min → 6 min", AMBER),
    ("dim_customer", "12 min → 3 min", GREEN),
    ("fact_shipments", "38 min → 9 min", GREEN),
    ("Schema drift", "1 column renamed", AMBER),
    ("Daily ETL window", "8–12 h → <90 min", GREEN),
    ("Pipeline uptime", "99.5%+", GREEN),
], subtitle="Profile  ·  re-engineer  ·  monitor")
h.panel(1030, 610, 330, "FRESHNESS & QUALITY", [
    ("Sources monitored", "30+ feeds"),
    ("Rows validated today", "18.4 M", GREEN),
    ("Late sources", "0", GREEN),
    ("Lineage", "report → source", CYAN),
], live=True)
h.note("Illustrative visualisation of DEO Suite data engineering optimization")
h.save(OUT + "IMG-12-detail.jpg")
print("ok")
