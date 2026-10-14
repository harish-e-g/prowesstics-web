"use client";
import { useState, type FormEvent } from "react";
import { site, interests } from "@/content/site";
import ImageSlot from "./ImageSlot";
import { Arrow } from "./icons";

// The form currently validates and confirms on the page.
// To receive leads, point handleSubmit at your CRM, a form service or a Next.js route handler (see README, step 7).
export default function Contact() {
  const [error, setError] = useState("");
  const [done, setDone] = useState("");
  const [copied, setCopied] = useState(false);

  function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const f = new FormData(e.currentTarget);
    const name = String(f.get("name") || "").trim();
    const email = String(f.get("email") || "").trim();
    if (!name) return setError("Add your name so we know who to reply to.");
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return setError("Enter a work email such as name@company.com.");
    setError("");
    setDone(`Thanks, ${name.split(" ")[0]}. We have your request about ${f.get("interest")}. A solution lead will be in touch shortly.`);
  }

  async function copy() {
    try { await navigator.clipboard.writeText(site.email); setCopied(true); } catch { /* user can select the text */ }
  }

  return (
    <section className="sec dark" id="contact" style={{ background: "linear-gradient(180deg,#061330,#0A1F44)" }}>
      <div className="wrap cta">
        <div>
          <span className="eyebrow">Let&apos;s talk</span>
          <h2>Two weeks. Your data.<span className="c"> Your numbers.</span></h2>
          <p className="lede">Tell us the problem. A solution lead who knows your industry will reply with a starting point and an honest view of fit.</p>
          <div className="mail">
            <span>{site.email}</span>
            <button className="copy" type="button" onClick={copy}>{copied ? "Copied" : "Copy"}</button>
          </div>
          <ImageSlot id="IMG-15" label="Contact visual" note="Consultant with a plant manager" sizes="(max-width: 900px) 100vw, 50vw" zoom />
        </div>
        <form onSubmit={handleSubmit} noValidate>
          <h3>Request a consultation</h3>
          <div className="row2">
            <label htmlFor="f-n">Full name<input id="f-n" name="name" autoComplete="name" /></label>
            <label htmlFor="f-e">Work email<input id="f-e" name="email" type="email" autoComplete="email" /></label>
          </div>
          <div className="row2">
            <label htmlFor="f-c">Company<input id="f-c" name="company" autoComplete="organization" /></label>
            <label htmlFor="f-a">I&apos;m interested in
              <select id="f-a" name="interest">{interests.map((i) => <option key={i}>{i}</option>)}</select>
            </label>
          </div>
          <label htmlFor="f-m">What would you like to solve?
            <textarea id="f-m" name="message" placeholder="For example: our reports take 6 hours to refresh and leadership doesn't trust the numbers" />
          </label>
          <p className="err" role="alert">{error}</p>
          <div><button className="btn btn-grad" type="submit">Send request <Arrow /></button></div>
          {done && <div className="done">{done}</div>}
        </form>
      </div>
    </section>
  );
}
