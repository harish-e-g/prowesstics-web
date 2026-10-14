"use client";
import { useEffect, useState } from "react";
import { companyFilm } from "@/content/images";
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
        <div className="video-modal" role="dialog" aria-modal="true" aria-label="Company film" onClick={(e) => e.target === e.currentTarget && setOpen(false)}>
          <button type="button" onClick={() => setOpen(false)}>Close</button>
          {companyFilm ? (
            <video src={companyFilm} controls autoPlay playsInline style={{ width: "min(960px,100%)", borderRadius: 18 }} />
          ) : (
            <div className="ph"><span className="tag">VIDEO-01 · 2 min company film<span>Add the file to /public/video and set companyFilm in content/images.ts</span></span></div>
          )}
        </div>
      )}
    </>
  );
}
