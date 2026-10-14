"use client";
import { useEffect, useState } from "react";
import { companyFilm, companyFilmPoster } from "@/content/images";
import { asset } from "@/lib/image-loader";
import { Play } from "./icons";

export default function FilmButton() {
  const [open, setOpen] = useState(false);

  useEffect(() => {
    if (!open) return;
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && setOpen(false);
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [open]);

  return (
    <>
      <button className="play" type="button" onClick={() => setOpen(true)}>
        <span className="ring"><Play /></span>
        <span><b>See How We Create Impact</b><span>2 min video</span></span>
      </button>
      {open && (
        <div className="video-modal" role="dialog" aria-modal="true" aria-label="Smart Assembly and Packing Line film" onClick={(e) => e.target === e.currentTarget && setOpen(false)}>
          <button type="button" onClick={() => setOpen(false)}>Close</button>
          {companyFilm ? (
            <video src={asset(companyFilm)} poster={companyFilmPoster ? asset(companyFilmPoster) : undefined} controls autoPlay playsInline preload="metadata" style={{ width: "min(1100px,100%)", maxHeight: "82vh", borderRadius: 18, background: "#000" }} />
          ) : (
            <div className="ph"><span className="tag">VIDEO-01 · 2 min company film<span>Add the file to /public/video and set companyFilm in content/images.ts</span></span></div>
          )}
        </div>
      )}
    </>
  );
}
