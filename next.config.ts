import type { NextConfig } from "next";

// STATIC_EXPORT=1 builds a plain static copy of the site (used for GitHub Pages and quick previews).
// NEXT_PUBLIC_BASE_PATH serves the site from a sub-folder, e.g. "/prowesstics-web" on
// harish-e-g.github.io. Leave it empty once a custom domain points at the site.
// Normal builds (next build / next start) keep full image optimisation.
const staticExport = process.env.STATIC_EXPORT === "1";
const basePath = process.env.NEXT_PUBLIC_BASE_PATH || "";

const nextConfig: NextConfig = {
  ...(staticExport ? { output: "export" as const, trailingSlash: true } : {}),
  ...(basePath ? { basePath } : {}),
  images: staticExport
    ? { loader: "custom", loaderFile: "./lib/image-loader.ts" }
    : {
        formats: ["image/avif", "image/webp"],
        deviceSizes: [640, 828, 1080, 1440, 1920, 2560, 3840],
      },
  poweredByHeader: false,
};

export default nextConfig;
