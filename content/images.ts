// Image slots. When an image is ready:
//   1. Save it in /public/images using the slot name, e.g. /public/images/IMG-01.jpg
//   2. Set "src" for that slot below, e.g. src: "/images/IMG-01.jpg"
// Until "src" is set, the site shows a labelled placeholder in that position.

export type Slot = { src?: string; alt: string; cutout?: boolean };

export const images: Record<string, Slot> = {
  "IMG-01": { src: "/images/IMG-01.jpg", alt: "Prowesstics leadership team in a boardroom at dusk" },
  "IMG-02": { src: "/images/IMG-02.png", alt: "Stacked servers with teal network cables", cutout: true },
  "IMG-03": { src: "/images/IMG-03.png", alt: "Business intelligence dashboard on a laptop", cutout: true },
  "IMG-04": { src: "/images/IMG-04.png", alt: "Cloud rack server", cutout: true },
  "IMG-05": { src: "/images/IMG-05.png", alt: "AI accelerator card", cutout: true },
  "IMG-06": { src: "/images/IMG-06.png", alt: "Industrial vision camera", cutout: true },
  "IMG-07": { src: "/images/IMG-07.png", alt: "Industrial robot arm", cutout: true },
  "IMG-08": { src: "/images/IMG-08.png", alt: "Network switch with patched cables", cutout: true },
  "IMG-09": { src: "/images/IMG-09.png", alt: "Engineer workstation essentials", cutout: true },
  "IMG-10": { src: "/images/IMG-10.jpg", alt: "Quality engineer at a vision inspection station" },
  "IMG-11": { src: "/images/IMG-11.jpg", alt: "Insurance retention team reviewing analytics" },
  "IMG-12": { src: "/images/IMG-12.jpg", alt: "Container port and logistics yard at dusk" },
  "IMG-13": { src: "/images/IMG-13.jpg", alt: "Supermarket aisle with a ceiling camera" },
  "IMG-14": { src: "/images/IMG-14.jpg", alt: "Barcode scanner on an assembly station" },
  "IMG-15": { src: "/images/IMG-15.jpg", alt: "Prowesstics consultant with a plant manager" },
  "IMG-16": { alt: "10 years", cutout: true },
  "IND-01": { src: "/images/IND-01.jpg", alt: "Manufacturing plant production line" },
  "IND-02": { src: "/images/IND-02.jpg", alt: "Automotive components assembly line" },
  "IND-03": { src: "/images/IND-03.jpg", alt: "Insurance and banking team at work" },
  "IND-04": { src: "/images/IND-04.jpg", alt: "Logistics warehouse and trucks" },
  "IND-05": { src: "/images/IND-05.jpg", alt: "Modern retail store" },
  "IND-06": { src: "/images/IND-06.jpg", alt: "Cardiology care team with patient data" },
  "IND-07": { src: "/images/IND-07.jpg", alt: "Solar and power utility site" },
  "IND-08": { src: "/images/IND-08.jpg", alt: "Construction site with concrete batching plant" },
  "IND-09": { src: "/images/IND-09.jpg", alt: "Travel and hospitality operations" },
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
