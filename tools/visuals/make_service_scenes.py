"""Service images for /services/: real work scenes with technical callouts (IMG-02 to IMG-09).
Sources: src/GAMMA_SVC-01.jpg to GAMMA_SVC-08.jpg. Design space is 1376 x 768.
Run: python3 tools/visuals/make_service_scenes.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from hud import *
SRC = os.path.join(HERE, "src") + "/"
OUT = os.path.join(HERE, "..", "..", "public", "images") + "/"
FS = 1.9  # service images render around 560 px wide

def H(n):
    return HUD(SRC + f"GAMMA_SVC-0{n}.jpg", 1376, 2752, fs=FS)

# 01 Data Engineering: architecture on the glass wall, lineage on screen
h = H(1)
h.chip(24, 24, "SOURCE → BRONZE → SILVER → GOLD", CYAN, "ETL 1.2M rows/min")
h.box((1018, 384, 1204, 534), CYAN, corner=16)
h.chip(24, 600, "QUALITY 99.6% PASS", GREEN, "drift checks on 30+ feeds")
h.note("Illustrative visualisation")
h.save(OUT + "IMG-02.jpg")

# 02 Business Intelligence: leadership review on one KPI model
h = H(2)
h.box((918, 132, 1332, 402), CYAN, corner=22)
h.chip(24, 24, "30+ DASHBOARDS · 14 BRANCHES", CYAN, "Power BI · Direct Lake")
h.chip(1352, 430, "REFRESH < 20 min", GREEN, "one trusted KPI model", anchor="tr")
h.note("Illustrative visualisation")
h.save(OUT + "IMG-03.jpg")

# 03 Cloud & Migration: data centre aisle
h = H(3)
h.chip(560, 24, "ON-PREM ETL  →  AZURE · AWS · GCP", AMBER, "wave 3 of 4  ·  zero-downtime cut-over")
h.box((468, 366, 624, 494), CYAN, corner=14)
h.chip(1352, 610, "RUNTIME −40%", GREEN, "licence cost removed", anchor="tr")
h.note("Illustrative visualisation")
h.save(OUT + "IMG-04.jpg")

# 04 AI & Advanced Analytics: model review
h = H(4)
h.box((182, 178, 466, 494), CYAN, corner=20)
h.chip(24, 24, "MODEL v3  ·  ROC AUC 0.92", GREEN, "churn scoring in production")
h.chip(24, 600, "TOP DRIVERS (SHAP)", AMBER, "claim delay · premium change")
h.note("Illustrative visualisation")
h.save(OUT + "IMG-05.jpg")

# 05 Computer Vision: inspection camera over the conveyor
h = H(5)
h.box((704, 208, 886, 310), CYAN, corner=14)
h.box((716, 520, 852, 632), GREEN, corner=14)
h.box((1028, 520, 1178, 632), AMBER, corner=14)
h.chip(1352, 24, "VISION STATION  ·  <100 ms", CYAN, "every part, every shift", anchor="tr")
h.chip(1352, 650, "BURR 0.94  →  REJECT", AMBER, anchor="tr")
h.note("Illustrative visualisation")
h.save(OUT + "IMG-06.jpg")

# 06 Factory Automation: PLC cabinet and HMI
h = H(6)
h.box((150, 80, 330, 428), CYAN, corner=18)
h.box((940, 220, 1088, 498), GREEN, corner=16)
h.chip(1352, 24, "POKA-YOKE ARMED", GREEN, "station 7  ·  variant B", anchor="tr")
h.chip(1352, 610, "TRACE  PT-48213 → SAP", CYAN, "PLC · SCADA · MES", anchor="tr")
h.note("Illustrative visualisation")
h.save(OUT + "IMG-07.jpg")

# 07 Data Ops & Managed Services: operations centre
h = H(7)
h.box((598, 140, 842, 286), CYAN, corner=16)
h.chip(1352, 24, "PIPELINE UPTIME 99.5%+", GREEN, "24 x 7 monitoring", anchor="tr")
h.chip(24, 548, "ALERT P2  ·  ACK 3 min", AMBER, "auto-retry succeeded")
h.note("Illustrative visualisation")
h.save(OUT + "IMG-08.jpg")

# 08 Staff Augmentation: sprint stand-up
h = H(8)
h.box((1136, 20, 1328, 336), CYAN, corner=18)
h.chip(24, 24, "POD ONBOARDED IN DAYS", CYAN, "data · BI · ML · QA")
h.chip(24, 620, "60+ CERTIFIED EXPERTS", GREEN, "Snowflake · Power BI · Python")
h.note("Illustrative visualisation")
h.save(OUT + "IMG-09.jpg")
print("ok")
