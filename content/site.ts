// All homepage copy and data lives here. Edit this file to change text, stats, logos or testimonials.

export const site = {
  name: "Prowesstics",
  legalName: "Prowesstics IT Services Pvt. Ltd.",
  url: "https://www.prowesstics.com",
  email: "sales@prowesstics.com",
  description:
    "Prowesstics partners with enterprises to turn data, AI and factory automation into measurable business impact, on the systems and cameras they already own.",
  locations: "Plano · Chennai",
  founded: "2017",
};

export const nav = [
  { label: "Services", href: "#services" },
  { label: "Industries", href: "#industries" },
  { label: "Solutions", href: "#solutions" },
  { label: "Clients", href: "#clients" },
  { label: "Technology", href: "#stack" },
  { label: "Insights", href: "#voices" },
];

export const hero = {
  kicker: ["DATA", "ANALYTICS", "AI", "CLOUD", "AUTOMATION"],
  title: "Trusted Data. Working AI.",
  highlight: "Real Business Impact.",
  lede:
    "We help enterprises trust their numbers, predict what happens next and automate the work in between, on the systems they already run.",
  badgeNumber: "10",
  badgeText: ["Years of", "building trusted", "data solutions"],
  sideTop: ["PEOPLE", "INSIGHTS", "TECHNOLOGY", "IMPACT"],
  sideBottom: ["FROM", "DATA", "TO", "ACTION"],
};

export type StatIcon = "team" | "spark" | "experts" | "db" | "globe";
export const stats: { value: string; label: [string, string]; icon: StatIcon }[] = [
  { value: "10+", label: ["Years of", "Expertise"], icon: "team" },
  { value: "370+", label: ["Projects", "Delivered"], icon: "spark" },
  { value: "60+", label: ["Certified", "Experts"], icon: "experts" },
  { value: "5+ PB", label: ["Data", "Processed"], icon: "db" },
  { value: "95%", label: ["Client", "Satisfaction"], icon: "globe" },
];

export type IndustryIcon = "factory" | "car" | "bank" | "network" | "bag" | "heart" | "bolt" | "crane" | "plane";
export const industries: { name: string; line: string; uses: string[]; icon: IndustryIcon; color: string; slot: string }[] = [
  { name: "Manufacturing", line: "Zero-defect lines and safer plants, on the cameras you already own.", uses: ["Vision quality control", "Safety compliance", "OEE analytics"], icon: "factory", color: "#1A7FE0", slot: "IND-01" },
  { name: "Automotive & Components", line: "Every checkpoint on every unit, covered at line speed.", uses: ["Assembly verification", "Traceability", "Poka-yoke"], icon: "car", color: "#0FA3B8", slot: "IND-02" },
  { name: "BFSI & Insurance", line: "Keep the customers you are about to lose, weeks before they go.", uses: ["Churn prediction", "AML reporting", "Customer 360"], icon: "bank", color: "#0B1B3A", slot: "IND-03" },
  { name: "Logistics & Supply Chain", line: "One trusted view across warehouse, transport, customs and finance.", uses: ["Control tower", "OTIF and SLA alerts", "Cost leakage"], icon: "network", color: "#E8892B", slot: "IND-04" },
  { name: "Retail & FMCG", line: "Smarter shelves and loyal shoppers, read from store behaviour.", uses: ["Footfall heatmaps", "Basket analysis", "Embedded BI"], icon: "bag", color: "#7C3AED", slot: "IND-05" },
  { name: "Healthcare", line: "One trusted view of clinical activity and care operations.", uses: ["Care data unification", "HIPAA-ready BI", "Ops dashboards"], icon: "heart", color: "#14965E", slot: "IND-06" },
  { name: "Energy & Utilities", line: "Spot leaks, corrosion and faults before they become outages.", uses: ["Leak and corrosion detection", "Gauge reading", "Asset monitoring"], icon: "bolt", color: "#E8B452", slot: "IND-07" },
  { name: "Construction & Infrastructure", line: "Faster cycles and safer crews on every site and plant.", uses: ["Equipment alignment", "PPE detection", "Site monitoring"], icon: "crane", color: "#D9364A", slot: "IND-08" },
  { name: "Travel & Hospitality", line: "Bookings, revenue and operations live in one place.", uses: ["Booking intelligence", "Agentic AI", "Revenue dashboards"], icon: "plane", color: "#1A9FD8", slot: "IND-09" },
];

export type ServiceIcon = "db" | "bars" | "cloud" | "chip" | "eye" | "gear" | "trend" | "userplus";
export const services: {
  title: string; body: string; points: string[]; icon: ServiceIcon; tone: string; slot: string;
  outcome: { v: string; l: string }; tech: string[];
}[] = [
  { title: "Data Engineering", body: "A strong, secure and scalable data foundation your whole business can report from.", points: ["Pipelines and ETL", "Data warehousing", "Data quality firewall"], icon: "db", tone: "c1", slot: "IMG-02", outcome: { v: "<90 min", l: "ETL cycle, down from 8 to 12 hours" }, tech: ["Snowflake", "Fabric", "Glue"] },
  { title: "Business Intelligence", body: "Interactive dashboards and KPIs that leadership finally trusts.", points: ["Power BI and Fabric", "CXO scorecards", "Embedded analytics"], icon: "bars", tone: "c2", slot: "IMG-03", outcome: { v: "30+", l: "live dashboards across 14 branches" }, tech: ["Power BI", "Direct Lake", "Yellowfin"] },
  { title: "Cloud & Migration", body: "Move legacy ETL and warehouses to cloud-native platforms that cost less to run.", points: ["Azure, AWS, GCP", "Legacy ETL migration", "Cost optimisation"], icon: "cloud", tone: "c3", slot: "IMG-04", outcome: { v: "~40%", l: "faster runs, licence cost eliminated" }, tech: ["Azure", "AWS", "GCP"] },
  { title: "AI & Advanced Analytics", body: "Predictive and generative AI built for production, not slideware.", points: ["Predictive models", "GenAI and RAG", "Agentic AI"], icon: "chip", tone: "c4", slot: "IMG-05", outcome: { v: "0.92", l: "ROC AUC on live churn scoring" }, tech: ["Python", "MLOps", "RAG"] },
  { title: "Computer Vision", body: "Your existing CCTV becomes a quality and safety layer across the plant.", points: ["Defect detection", "PPE and zone safety", "Edge inference"], icon: "eye", tone: "c5", slot: "IMG-06", outcome: { v: "<100 ms", l: "from deviation to alert" }, tech: ["Edge AI", "NVIDIA", "WhatsApp"] },
  { title: "Factory Automation", body: "Traceability and error-proofing wired into the systems that run your line.", points: ["ProTrace AI", "Poka-yoke", "Assembly verification"], icon: "gear", tone: "c6", slot: "IMG-07", outcome: { v: "4 h → 15 min", l: "cycle time on an automated station" }, tech: ["PLC", "SCADA", "MES", "SAP"] },
  { title: "Data Ops & Managed Services", body: "Pipelines and models that stay healthy long after go-live.", points: ["Monitoring and SLAs", "DataOps", "Continuous tuning"], icon: "trend", tone: "c7", slot: "IMG-08", outcome: { v: "99.5%+", l: "pipeline uptime across mills" }, tech: ["DataOps", "Alerts", "SLAs"] },
  { title: "Staff Augmentation", body: "Vetted engineers who join your sprints on your stack, in days.", points: ["Data and BI engineers", "ML and GenAI", "QA and DBAs"], icon: "userplus", tone: "c8", slot: "IMG-09", outcome: { v: "60+", l: "certified experts on the bench" }, tech: ["Snowflake", "Power BI", "Python"] },
];

export const commitments = [
  { num: "2 wks", title: "A working pilot, fast", body: "A 2-week assessment or a pilot on three cameras, on your data, so you see value before you commit." },
  { num: "0", title: "No rip-and-replace", body: "We work on the cameras, systems and licences you already pay for. No new logins for your floor teams." },
  { num: "1", title: "One team, end to end", body: "Data, AI and physical automation from one partner, with no hand-offs between vendors." },
  { num: "KPI", title: "Measured on your numbers", body: "Every engagement is tied to the metric you report on: refresh time, defect rate, renewal rate or cost." },
  { num: "DPDP", title: "Compliance built in", body: "DPDP, GDPR and HIPAA-ready platforms, role-based access and audit-ready logs as standard." },
  { num: "Bench", title: "Support that scales", body: "Managed services and a delivery bench in Chennai that grows with your programme." },
];

export const products: {
  name: string; kind: string; body: string; kpis: { v: string; l: string }[];
  cta?: string; big?: boolean; slot: string; slotLabel: string;
}[] = [
  { name: "ProVision AI", kind: "Computer vision", body: "Turn the CCTV you already own into a thinking layer that flags the deviation before the defect and the near-miss before the incident.", kpis: [{ v: "64", l: "use cases" }, { v: "<100 ms", l: "edge alerts" }, { v: "3–4×", l: "ROI" }], cta: "Book a 2-week pilot", big: true, slot: "IMG-10", slotLabel: "Quality station on a production line" },
  { name: "ProChurn AI", kind: "Retention intelligence", body: "Know which customers are about to leave, why, and the save action most likely to keep them, 10 to 45 days ahead.", kpis: [{ v: "85%", l: "accuracy" }, { v: "0.92", l: "ROC AUC" }, { v: "+11 pts", l: "renewal lift" }], cta: "Run my payback", big: true, slot: "IMG-11", slotLabel: "Retention team at an insurer" },
  { name: "DEO Suite", kind: "Data engineering", body: "Ten logistics systems, one governed data layer, refreshed continuously.", kpis: [{ v: "10", l: "systems unified" }, { v: "81%", l: "faster refresh" }], slot: "IMG-12", slotLabel: "Logistics loading dock" },
  { name: "ProSight AI", kind: "Retail analytics", body: "Footfall, heatmaps, dwell time and basket analysis from your store cameras.", kpis: [{ v: "FMCG", l: "and warehousing" }], slot: "IMG-13", slotLabel: "Supermarket aisle" },
  { name: "ProTrace AI", kind: "Factory automation", body: "Station-level traceability and poka-yoke wired into PLC, SCADA, MES and SAP.", kpis: [{ v: "Full", l: "factory automation" }], slot: "IMG-14", slotLabel: "Barcode traceability station" },
];

export const steps = [
  { n: "1", when: "Weeks 1–2", title: "Assess", body: "We map your data, systems and KPIs and pick the one use case with visible value." },
  { n: "2", when: "Days 30–60", title: "Pilot", body: "A focused pilot on your real data, ending with measured KPI impact." },
  { n: "3", when: "Quarter 1–2", title: "Scale", body: "Production roll-out across sites and teams, with governance and change support." },
  { n: "4", when: "Ongoing", title: "Run", body: "Managed analytics and AI operations, retraining and continuous improvement." },
];

// Client logos: add a PNG to /public/logos and a line here. Entries without "logo" render as a clean wordmark.
export const clients: { name: string; logo?: string; sub?: string }[] = [
  { name: "Metsä Group", logo: "/logos/metsa.png" },
  { name: "NIFCO", logo: "/logos/nifco.png" },
  { name: "LendingUSA", logo: "/logos/lendingusa.png" },
  { name: "Schwing Stetter", logo: "/logos/schwing.png" },
  { name: "WEH", logo: "/logos/weh.png" },
  { name: "Bayada", logo: "/logos/bayada.png" },
  { name: "Alice Blue", logo: "/logos/aliceblue.png" },
  { name: "ZING", logo: "/logos/zing.png" },
  { name: "K-Indev Logistics", logo: "/logos/kindev.png" },
  { name: "TripFactory", logo: "/logos/tripfactory.png" },
  { name: "Excel Die Castings", logo: "/logos/excel.png" },
  { name: "A2C", logo: "/logos/a2c.png" },
  { name: "Sujan ContiTech", sub: "AVS" },
  { name: "Rane", sub: "STEERING SYSTEMS" },
  { name: "RRTS", sub: "USA" },
];

export const results = [
  { who: "Pulp & forestry · Metsä", before: "8–12 h", after: "<90 min", note: "Daily ETL across 30+ vendor feeds, 99.5%+ uptime." },
  { who: "Construction equipment · Schwing Stetter", before: "4 h", after: "15 min", note: "Vehicle alignment automated with vision." },
  { who: "Insurance · ProChurn AI", before: "27%", after: "38%", note: "Renewal rate in one quarter on 62,624 policies." },
  { who: "Lending · LendingUSA", before: "3 h", after: "1.5 h", note: "ETL runtime, with licence costs eliminated." },
  { who: "Logistics · K-Indev", before: "7 systems", after: "1", note: "One platform across 14 branches." },
  { who: "Logistics · RRTS USA", before: "4–6 h", after: "<20 min", note: "Refresh cycle on Microsoft Fabric." },
  { who: "Auto components · Sujan ContiTech", before: "1 pilot", after: "4 plants", note: "Safety vision scaled across sites." },
  { who: "Supply chain · Metsä APAC", before: "Baseline", after: "+50%", note: "Team work efficiency from unified reporting." },
];

// Tech logos: "logo" points to /public/tech. Entries with "mono" show a coloured badge until an official PNG is added.
type Tech = { name: string; logo?: string; mono?: string; color?: string };
export const techRow1: Tech[] = [
  { name: "Microsoft Azure", logo: "/tech/azure.png" },
  { name: "AWS", logo: "/tech/aws.png" },
  { name: "Google Cloud", logo: "/tech/gcp.png" },
  { name: "Snowflake", logo: "/tech/snowflake.png" },
  { name: "Microsoft Fabric", mono: "Fab", color: "linear-gradient(135deg,#0F9D58,#1E88E5)" },
  { name: "Power BI", mono: "BI", color: "#E8A400" },
  { name: "BigQuery", logo: "/tech/googlebigquery.png" },
  { name: "ClickHouse", logo: "/tech/clickhouse.png" },
  { name: "PostgreSQL", logo: "/tech/postgresql.png" },
  { name: "Oracle", logo: "/tech/oracle.png" },
  { name: "SQL Server", logo: "/tech/sqlserver.png" },
  { name: "AWS Glue", mono: "Glue", color: "#8C4FFF" },
];
export const techRow2: Tech[] = [
  { name: "Matillion", logo: "/tech/matillion.png" },
  { name: "Talend", logo: "/tech/talend.png" },
  { name: "Informatica", mono: "Inf", color: "#FF4D00" },
  { name: "Pentaho", mono: "Pdi", color: "#005D9E" },
  { name: "Yellowfin BI", mono: "YF", color: "#1C9AD6" },
  { name: "Python", logo: "/tech/python.png" },
  { name: "pandas", logo: "/tech/pandas.png" },
  { name: "Django", logo: "/tech/django.png" },
  { name: "NVIDIA", logo: "/tech/nvidia.png" },
  { name: "SAP", logo: "/tech/sap.png" },
  { name: "Siemens", logo: "/tech/siemens.png" },
  { name: "MQTT", logo: "/tech/mqtt.png" },
  { name: "WhatsApp Business", logo: "/tech/whatsapp.png" },
  { name: "Honeywell", mono: "HW", color: "#DC1E35" },
  { name: "Rockwell", mono: "RA", color: "#CD163F" },
];

export const testimonials: { name: string; role: string; logo?: string; badge?: string; quote: string }[] = [
  { name: "Grace", role: "Head of Data & Automation, Metsä Group", logo: "/logos/metsa.png", quote: "Prowesstics data analysts have proven their capability to design powerful analytical reports for the Metsä APAC supply chain. The meaningful insights and ease of visualising the entire supply chain activity have increased our company's work efficiency by 50%." },
  { name: "Phil Abernathy", role: "CTO, ZING", logo: "/logos/zing.png", quote: "A very big thanks to the Prowesstics team for implementing our Yellowfin analytics solution within ZING. The team ramped up quickly and delivered the reports and visualisations we needed with strong collaboration and high delivery quality throughout our Agile way of working." },
  { name: "Plant Head", role: "Schwing Stetter India", logo: "/logos/schwing.png", quote: "Prowesstics replaced a four-hour alignment ritual with a fifteen-minute one. We're taking it to every batch plant we build." },
  { name: "Leadership Team", role: "K-Indev Ocean (India) Pvt. Ltd.", logo: "/logos/kindev.png", quote: "Bringing seven separate systems under one roof was something we thought would take years. Prowesstics delivered a working, unified platform that gave us visibility we never had before. The team understood our logistics domain deeply and built something our branch teams actually use every day." },
  { name: "Data Team", role: "LendingUSA", logo: "/logos/lendingusa.png", quote: "Prowesstics played a key role in modernising our ETL pipelines and stabilising critical analytics and AML workloads. The team executed the migration efficiently, reduced operational overhead and ensured data accuracy throughout the transition." },
  { name: "Plant Director", role: "Sujan ContiTech AVS", badge: "Sujan ContiTech", quote: "The Tamil Nadu pilot proved itself in months. We're extending to Pune and Bilaspur, and our global clients have noticed the difference." },
  { name: "Leadership Team", role: "TripFactory Travel, Bengaluru", logo: "/logos/tripfactory.png", quote: "We had six different systems telling six different stories. Prowesstics gave us one platform that finally spoke the truth. Our operations team stopped chasing spreadsheets and our leadership started making faster decisions." },
  { name: "Management Team", role: "WEH, Germany", logo: "/logos/weh.png", quote: "The move from Excel-based reporting to a centralised data and BI platform has significantly improved how our teams access and use information. The Prowesstics team executed the implementation smoothly and provided strong support throughout." },
  { name: "Data & Analytics Team", role: "NIFCO", logo: "/logos/nifco.png", quote: "The Power BI gateway implementation lets us reliably refresh cloud reports from our on-premises Oracle data without manual intervention. It improved reporting consistency, strengthened security controls and gave us better visibility into refresh operations." },
  { name: "Cardiology Provider", role: "United States, name withheld", badge: "US Healthcare", quote: "The need was never just dashboards. It was a consistent, trusted view of healthcare operations across every system." },
];

export const interests = [
  "Data engineering and DEO Suite",
  "BI and analytics",
  "Cloud and migration",
  "ProVision AI",
  "ProChurn AI",
  "ProSight AI",
  "ProTrace AI and factory automation",
  "Staff augmentation",
];

export const footerCols = [
  { title: "Services", links: [["Data Engineering", "#services"], ["Business Intelligence", "#services"], ["Cloud & Migration", "#services"], ["AI & Analytics", "#services"], ["Staff Augmentation", "#services"]] },
  { title: "Solutions", links: [["ProVision AI", "#solutions"], ["ProChurn AI", "#solutions"], ["DEO Suite", "#solutions"], ["ProSight AI", "#solutions"], ["ProTrace AI", "#solutions"]] },
  { title: "Industries", links: [["Manufacturing", "#industries"], ["BFSI & Insurance", "#industries"], ["Logistics", "#industries"], ["Retail & FMCG", "#industries"], ["Healthcare", "#industries"]] },
  { title: "Company", links: [["Clients", "#clients"], ["Testimonials", "#voices"], ["Technology", "#stack"], ["Contact", "#contact"]] },
] as const;
