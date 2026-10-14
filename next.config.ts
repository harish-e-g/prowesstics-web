import type { NextConfig } from "next";

// STATIC_EXPORT=1 builds a plain static copy (used for quick previews); normal builds keep full image optimisation.
const staticExport = process.env.STATIC_EXPORT === "1";

const nextConfig: NextConfig = {
  ...(staticExport ? { output: "export" as const } : {}),
  images: {
    unoptimized: staticExport,
    formats: ["image/avif", "image/webp"],
    deviceSizes: [640, 828, 1080, 1440, 1920, 2560, 3840],
  },
  poweredByHeader: false,
};

export default nextConfig;
