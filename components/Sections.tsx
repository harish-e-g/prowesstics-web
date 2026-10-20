import Image from "next/image";
import Link from "next/link";
import { services, slug, industries, commitments, products, steps, clients, results, tech_platforms, tech_data, tech_ai } from "@/content/site";
import ImageSlot from "./ImageSlot";
import { asset } from "@/lib/image-loader";
import { Arrow, ServiceGlyph, IndustryGlyph } from "./icons";

function Head({ eyebrow, title, body, link }: { eyebrow: string; title: string; body?: string; link?: { label: string; href: string } }) {
  return (
    <div className="sec-head">
      <div>
        <span className="eyebrow">{eyebrow}</span>
        <h2>{title}</h2>
        {body && <p>{body}</p>}
      </div>
      {link && <Link className="tlink" href={link.href}>{link.label} <Arrow /></Link>}
    </div>
  );
}

// Full services list, shown on /services/: an index, then one editorial chapter per service.
export function Services() {
  return (
    <section className="sec svc" id="services">
      <div className="wrap">
        <nav className="svc-index" aria-label="Services on this page">
          {services.map((s, i) => (
            <a href={`#${slug(s.title)}`} key={s.title}><span>{String(i + 1).padStart(2, "0")}</span>{s.title}</a>
          ))}
        </nav>
        <div className="svc-list">
          {services.map((s, i) => (
            <article className="svc-row" id={slug(s.title)} key={s.title}>
              <div className="svc-vis">
                <ImageSlot id={s.slot} sizes="(max-width: 860px) 92vw, 640px" zoom />
              </div>
              <div className="svc-txt">
                <span className="svc-n">{String(i + 1).padStart(2, "0")} / {String(services.length).padStart(2, "0")}</span>
                <h2>{s.title}</h2>
                <p className="svc-lead">{s.body}</p>
                <dl className="svc-ca">
                  <div><dt>The challenge</dt><dd>{s.problem}</dd></div>
                  <div><dt>Our approach</dt><dd>{s.approach}</dd></div>
                </dl>
                <ul>{s.points.map((p) => <li key={p}>{p}</li>)}</ul>
                <div className="svc-foot">
                  <div className="svc-out"><b>{s.outcome.v}</b><span>{s.outcome.l}</span></div>
                  <div className="svc-tech">{s.tech.map((t) => <span key={t}>{t}</span>)}</div>
                </div>
                <Link className="tlink" href="/#contact">Discuss {s.title.toLowerCase()} <Arrow size={16} /></Link>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

export function Industries() {
  return (
    <section className="sec" id="industries">
      <div className="wrap">
        <Head eyebrow="Industries we serve" title="Built for the industries that run on data" body="Nine sectors where our data platforms, AI and vision systems are already in production." link={{ label: "Talk to an industry lead", href: "/#contact" }} />
        <div className="ind-grid">
          {industries.map((d) => (
            <article className="ind-card" key={d.name}>
              <ImageSlot id={d.slot} label={d.name} sizes="(max-width: 640px) 100vw, (max-width: 1000px) 50vw, 400px" zoom />
              <div className="ind-body">
                <div className="ind-h"><span className="ind-ic"><IndustryGlyph name={d.icon} color={d.color} /></span><h3>{d.name}</h3></div>
                <p>{d.line}</p>
                <div className="ind-uses">{d.uses.map((u) => <span key={u}>{u}</span>)}</div>
                <Link className="tlink" href="/#contact">See use cases <Arrow size={16} /></Link>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

export function Commitments() {
  return (
    <section className="sec" style={{ paddingTop: 0 }}>
      <div className="wrap">
        <Head eyebrow="What you can expect" title="Working with Prowesstics" body="Six commitments every client gets, from the first call to managed operations." />
        <div className="expect">
          {commitments.map((c) => (
            <div className="ex" key={c.title}><span className="num">{c.num}</span><h3>{c.title}</h3><p>{c.body}</p></div>
          ))}
        </div>
      </div>
    </section>
  );
}

export function Solutions() {
  return (
    <section className="sec dark" id="solutions">
      <div className="wrap">
        <Head eyebrow="Our solutions" title="Products built for outcomes" body="Proven platforms you can deploy in weeks, trained on your data and running on your stack." link={{ label: "Book a demo", href: "/#contact" }} />
        <div className="prods">
          {products.map((p) => (
            <article className={`prod${p.big ? " big" : ""}`} key={p.name}>
              <ImageSlot id={p.slot} label={p.name} note={p.slotLabel} sizes="(max-width: 640px) 100vw, 50vw" zoom />
              <div className="prod-b">
                <span className="prod-k">{p.kind}</span>
                <h3>{p.name}</h3>
                <p>{p.body}</p>
                {p.kpis.length > 0 && <div className="kpis">{p.kpis.map((k) => <div key={k.l}><b>{k.v}</b><span>{k.l}</span></div>)}</div>}
                {p.tags && <div className="prod-tags">{p.tags.map((t) => <span key={t}>{t}</span>)}</div>}
                {p.cta && <Link className="tlink" href="/#contact">{p.cta} <Arrow /></Link>}
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

export function Engage() {
  return (
    <section className="sec">
      <div className="wrap">
        <Head eyebrow="How we engage" title="From first call to measurable value" body="A clear path with a deliverable at every stage, so you are never asked to commit blind." />
        <div className="steps">
          {steps.map((s) => (
            <div className="step" key={s.n}><span className="n">{s.n}</span><span className="when">{s.when}</span><h3>{s.title}</h3><p>{s.body}</p></div>
          ))}
        </div>
      </div>
    </section>
  );
}

function ClientTile({ c }: { c: (typeof clients)[number] }) {
  return c.logo ? (
    <div className="lg"><Image src={c.logo} alt={c.name} width={170} height={56} /></div>
  ) : (
    <div className="lg word">{c.name}<small>{c.sub}</small></div>
  );
}

export function Clients() {
  return (
    <section className="sec" id="clients" style={{ background: "var(--mist)" }}>
      <div className="wrap">
        <Head eyebrow="Trusted by" title="Enterprises that run on Prowesstics" body="Manufacturers, lenders, logistics networks and platforms across India, Europe and the United States." />
      </div>
      <div className="marquee" style={{ ["--dur" as string]: "55s" }}>
        <div className="marquee-track">
          {[...clients, ...clients].map((c, i) => <ClientTile c={c} key={c.name + i} />)}
        </div>
      </div>
    </section>
  );
}

export function Results() {
  return (
    <section className="sec" style={{ background: "var(--mist)", paddingTop: 0 }}>
      <div className="wrap">
        <Head eyebrow="Results you can expect" title="Before and after, measured" link={{ label: "Read client stories", href: "/#voices" }} />
        <div className="res-grid">
          {results.map((r) => (
            <div className="res" key={r.who}>
              <span className="who">{r.who}</span>
              <div className="ba"><s>{r.before}</s><b>{r.after}</b></div>
              <p>{r.note}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function TechTile({ t }: { t: (typeof tech_ai)[number] }) {
  return (
    <div className="lg">
      <img src={asset(`/tech/${t.id}.webp`)} alt={t.name} title={t.name} loading="lazy" decoding="async" />
    </div>
  );
}

const techRows = [
  { items: tech_platforms, dur: "70s", rev: false },
  { items: tech_data, dur: "78s", rev: true },
  { items: tech_ai, dur: "84s", rev: false },
];

export function TechStack() {
  return (
    <section className="sec tech" id="stack">
      <div className="wrap">
        <Head eyebrow="Technology" title="Fluent in your stack" body="Cloud, data, AI and industrial platforms our engineers certify on and deliver with every day. We plug into what you run instead of replacing it." />
      </div>
      {techRows.map((r, k) => (
        <div className={`marquee${r.rev ? " rev" : ""}`} style={{ ["--dur" as string]: r.dur }} key={k}>
          <div className="marquee-track">{[...r.items, ...r.items].map((t, i) => <TechTile t={t} key={t.id + i} />)}</div>
        </div>
      ))}
    </section>
  );
}
