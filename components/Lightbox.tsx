"use client";
import { useEffect, useState } from "react";

// Click any element with data-zoom="<image url>" to open the full technical view.
export default function Lightbox() {
  const [src, setSrc] = useState<string | null>(null);
  const [alt, setAlt] = useState("");

  useEffect(() => {
    const onClick = (e: MouseEvent) => {
      const el = (e.target as HTMLElement | null)?.closest<HTMLElement>("[data-zoom]");
      if (!el) return;
      e.preventDefault();
      setSrc(el.dataset.zoom || null);
      setAlt(el.dataset.zoomAlt || "");
    };
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") setSrc(null);
      const el = document.activeElement as HTMLElement | null;
      if ((e.key === "Enter" || e.key === " ") && el?.dataset.zoom) {
        e.preventDefault();
        setSrc(el.dataset.zoom);
        setAlt(el.dataset.zoomAlt || "");
      }
    };
    document.addEventListener("click", onClick);
    document.addEventListener("keydown", onKey);
    return () => {
      document.removeEventListener("click", onClick);
      document.removeEventListener("keydown", onKey);
    };
  }, []);

  if (!src) return null;
  return (
    <div className="lightbox" role="dialog" aria-modal="true" aria-label={alt || "Image detail"} onClick={(e) => e.target === e.currentTarget && setSrc(null)}>
      <button type="button" className="lightbox-close" onClick={() => setSrc(null)}>Close</button>
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img src={src} alt={alt} />
      <p className="lightbox-cap">{alt}</p>
    </div>
  );
}
