// Image slots. When an image is ready:
//   1. Save it in /public/images using the slot name, e.g. /public/images/IMG-01.jpg
//   2. Set "src" for that slot below, e.g. src: "/images/IMG-01.jpg"
//   3. Optional: set "detail" to a larger technical view that opens when the image is clicked
// Until "src" is set, the site shows a labelled placeholder in that position.

export type Slot = { src?: string; detail?: string; alt: string; cutout?: boolean };

export const images: Record<string, Slot> = {
  "IMG-01": { src: "/images/IMG-01.jpg", alt: "Prowesstics leadership team in a boardroom at dusk" },
  "IMG-02": { src: "/images/IMG-02.png", alt: "Data engineering: ETL throughput and data quality readouts", cutout: true },
  "IMG-03": { src: "/images/IMG-03.png", alt: "Business intelligence: dashboards and KPI refresh readouts", cutout: true },
  "IMG-04": { src: "/images/IMG-04.png", alt: "Cloud migration: runtime and platform readouts", cutout: true },
  "IMG-05": { src: "/images/IMG-05.png", alt: "AI and analytics: model accuracy and inference readouts", cutout: true },
  "IMG-06": { src: "/images/IMG-06.png", alt: "Computer vision: defect and PPE detection readouts", cutout: true },
  "IMG-07": { src: "/images/IMG-07.png", alt: "Factory automation: poka-yoke and cycle time readouts", cutout: true },
  "IMG-08": { src: "/images/IMG-08.png", alt: "Data operations: uptime and alerting readouts", cutout: true },
  "IMG-09": { src: "/images/IMG-09.png", alt: "Staff augmentation: certified experts and stack coverage", cutout: true },
  "IMG-10": { src: "/images/IMG-10.jpg", detail: "/images/IMG-10-detail.jpg", alt: "ProVision AI detecting a surface defect, verifying PPE and converting a part to a 2D wireframe on a production line" },
  "IMG-11": { src: "/images/IMG-11.jpg", detail: "/images/IMG-11-detail.jpg", alt: "ProChurn AI scoring customer churn risk with the top drivers for each policy" },
  "IMG-12": { src: "/images/IMG-12.jpg", detail: "/images/IMG-12-detail.jpg", alt: "DEO Suite data engineering optimization: engineers reviewing a pipeline DAG and runtime trends" },
  "IMG-13": { src: "/images/IMG-13.jpg", detail: "/images/IMG-13-detail.jpg", alt: "ProSight AI footfall heat map, shopper dwell tracking and out-of-stock alerts in a supermarket" },
  "IMG-14": { src: "/images/IMG-14.jpg", detail: "/images/IMG-14-detail.jpg", alt: "ProTrace AI reading a part code, confirming the variant and logging its full genealogy" },
  "IMG-15": { src: "/images/IMG-15.jpg", detail: "/images/IMG-15-detail.jpg", alt: "Prowesstics consultant and plant manager reviewing a two-week pilot" },
  "IMG-16": { alt: "10 years", cutout: true },
  "IND-01": { src: "/images/IND-01.jpg", alt: "Manufacturing: part measurement, PPE check and machine OEE" },
  "IND-02": { src: "/images/IND-02.jpg", alt: "Automotive: weld seam and spot weld verification in the body shop" },
  "IND-03": { src: "/images/IND-03.jpg", alt: "BFSI and insurance: churn risk and customer drivers on a risk dashboard" },
  "IND-04": { src: "/images/IND-04.jpg", alt: "Logistics: container dwell, forklift tracking and dock status" },
  "IND-05": { src: "/images/IND-05.jpg", alt: "Retail: shopper dwell, conversion and shelf gap detection" },
  "IND-06": { src: "/images/IND-06.jpg", alt: "Healthcare: remote patient monitoring with live heart data" },
  "IND-07": { src: "/images/IND-07.jpg", alt: "Energy: thermal hotspot and soiling detection on a solar park" },
  "IND-08": { src: "/images/IND-08.jpg", alt: "Construction: transit mixer chute alignment at a batching plant" },
  "IND-09": { src: "/images/IND-09.jpg", alt: "Travel: agentic AI itinerary and booking intelligence" },
  "IMG-17": { alt: "Manufacturing plant production line" },
  "IMG-18": { alt: "Automotive assembly line" },
  "IMG-19": { alt: "Insurance and banking professionals" },
  "IMG-20": { alt: "Logistics port and warehouse operations" },
  "IMG-21": { alt: "Modern retail store" },
  "IMG-22": { alt: "Healthcare remote monitoring" },
  "IMG-23": { alt: "Energy and utilities field inspection" },
  "IMG-24": { alt: "Construction site and ready-mix plant" },
  "IMG-25": { alt: "Travel and hospitality" },
};

// Optional company film. Place the file in /public/video and set the path, e.g. "/video/company-film.mp4"
export const companyFilm: string | undefined = undefined;
