// Image loader for static builds (GitHub Pages): serves files as they are and adds the
// site's base path, which next/image does not add on its own.
export default function imageLoader({ src }: { src: string; width: number; quality?: number }) {
  return asset(src);
}

// Prefixes a /public asset path with the base path. Use for any plain URL to a file in /public.
export function asset(src: string) {
  const base = process.env.NEXT_PUBLIC_BASE_PATH || "";
  return src.startsWith("/") ? `${base}${src}` : src;
}
