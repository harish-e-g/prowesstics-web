// Image slots. When an image is ready:
//   1. Save it in /public/images using the slot name, e.g. /public/images/IMG-01.jpg
//   2. Set "src" for that slot below, e.g. src: "/images/IMG-01.jpg"
// Until "src" is set, the site shows a labelled placeholder in that position.

export type Slot = { src?: string; alt: string; cutout?: boolean };

export const images: Record<string, Slot> = {
  "IMG-01": { alt: "Prowesstics leadership team in a boardroom at dusk" },
  "IMG-02": { alt: "Data engineering hardware", cutout: true },
  "IMG-03": { alt: "Business intelligence dashboard on a laptop", cutout: true },
  "IMG-04": { alt: "Cloud rack server", cutout: true },
  "IMG-05": { alt: "AI accelerator card", cutout: true },
  "IMG-06": { alt: "Industrial vision camera", cutout: true },
  "IMG-07": { alt: "Industrial robot arm", cutout: true },
  "IMG-08": { alt: "Network switch with patched cables", cutout: true },
  "IMG-09": { alt: "Engineer workstation essentials", cutout: true },
  "IMG-10": { alt: "Quality engineer at a vision inspection station" },
  "IMG-11": { alt: "Insurance retention team reviewing analytics" },
  "IMG-12": { alt: "Logistics warehouse loading dock" },
  "IMG-13": { alt: "Supermarket aisle with a ceiling camera" },
  "IMG-14": { alt: "Barcode scanner on an assembly station" },
  "IMG-15": { alt: "Prowesstics consultant with a plant manager" },
  "IMG-16": { alt: "10 years", cutout: true },
  "IND-01": { alt: "Manufacturing plant production line" },
  "IND-02": { alt: "Automotive components assembly line" },
  "IND-03": { alt: "Insurance and banking team at work" },
  "IND-04": { alt: "Logistics warehouse and trucks" },
  "IND-05": { alt: "Modern retail store" },
  "IND-06": { alt: "Cardiology care team with patient data" },
  "IND-07": { alt: "Solar and power utility site" },
  "IND-08": { alt: "Construction site with concrete batching plant" },
  "IND-09": { alt: "Travel and hospitality operations" },
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
