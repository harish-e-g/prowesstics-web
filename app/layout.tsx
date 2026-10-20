import type { Metadata, Viewport } from "next";
import localFont from "next/font/local";
import { site } from "@/content/site";
import "./globals.css";

// Self-hosted Nunito Sans (variable weight), served from your own domain for speed and privacy.
const nunito = localFont({
  src: "../node_modules/@fontsource-variable/nunito-sans/files/nunito-sans-latin-wght-normal.woff2",
  variable: "--font-nunito",
  weight: "200 1000",
  display: "swap",
});

export const metadata: Metadata = {
  metadataBase: new URL(site.url),
  title: {
    default: "Prowesstics | Data Engineering, AI & Factory Automation",
    template: "%s | Prowesstics",
  },
  description: site.description,
  keywords: [
    "data engineering services", "computer vision for manufacturing", "churn prediction insurance",
    "Microsoft Fabric migration", "Power BI consulting", "factory automation India",
    "AI quality inspection", "staff augmentation data engineers",
  ],
  alternates: { canonical: "/" },
  openGraph: {
    type: "website",
    url: site.url,
    siteName: site.name,
    title: "Prowesstics | Data. People. Real Business Impact.",
    description: site.description,
    images: [{ url: "/brand/wordmark.png", width: 1600, height: 210, alt: "Prowesstics" }],
  },
  twitter: { card: "summary_large_image", title: "Prowesstics", description: site.description },
  robots: { index: true, follow: true },
};

export const viewport: Viewport = {
  themeColor: "#061330",
  width: "device-width",
  initialScale: 1,
  viewportFit: "cover",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={nunito.variable}>
      <body>{children}</body>
    </html>
  );
}
