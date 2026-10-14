"use client";
import Image from "next/image";
import { useRef } from "react";
import { testimonials } from "@/content/site";
import { Chevron } from "./icons";

export default function Testimonials() {
  const track = useRef<HTMLDivElement>(null);
  const step = (dir: number) => {
    const el = track.current;
    if (!el) return;
    const card = el.querySelector<HTMLElement>(".tm");
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    el.scrollBy({ left: dir * ((card?.getBoundingClientRect().width ?? 400) + 18), behavior: reduce ? "auto" : "smooth" });
  };

  return (
    <section className="sec dark" id="voices">
      <div className="wrap">
        <div className="sec-head">
          <div>
            <span className="eyebrow">Client voices</span>
            <h2>What our clients say</h2>
            <p>Stakeholder references available for verification on request.</p>
          </div>
          <div className="tm-ctrl">
            <button type="button" onClick={() => step(-1)} aria-label="Previous testimonial"><Chevron dir="left" size={18} /></button>
            <button type="button" onClick={() => step(1)} aria-label="Next testimonial"><Chevron size={18} /></button>
          </div>
        </div>
        <div className="tm-track" ref={track} tabIndex={0} aria-label="Testimonials">
          {testimonials.map((t) => (
            <figure className="tm" key={t.role}>
              <div className="stars" aria-label="Five stars">★★★★★</div>
              <blockquote>{t.quote}</blockquote>
              <figcaption>
                {t.logo ? (
                  <span className="lgm"><Image src={t.logo} alt="" width={76} height={34} /></span>
                ) : (
                  <span className="lgm word">{t.badge}</span>
                )}
                <div><b>{t.name}</b><span>{t.role}</span></div>
              </figcaption>
            </figure>
          ))}
        </div>
      </div>
    </section>
  );
}
