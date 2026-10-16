import Image from "next/image";
import Link from "next/link";
import { nav, services, products, slug } from "@/content/site";
import { Arrow, Search, ServiceGlyph } from "./icons";

// Drop-down panels for the top bar. Services link to their section on /services/,
// solutions to the products block on the homepage.
function ServicesMenu() {
  return (
    <div className="mega" role="menu">
      <div className="mega-grid">
        {services.map((s) => (
          <Link role="menuitem" className="mega-item" href={`/services/#${slug(s.title)}`} key={s.title}>
            <span className="mega-ic"><ServiceGlyph name={s.icon} /></span>
            <span><b>{s.title}</b><small>{s.body}</small></span>
          </Link>
        ))}
      </div>
      <Link className="mega-foot" href="/services/">All services <Arrow size={16} /></Link>
    </div>
  );
}

function SolutionsMenu() {
  return (
    <div className="mega narrow" role="menu">
      <div className="mega-grid one">
        {products.map((p) => (
          <Link role="menuitem" className="mega-item" href="/#solutions" key={p.name}>
            <span><b>{p.name}</b><small>{p.kind}</small></span>
          </Link>
        ))}
      </div>
      <Link className="mega-foot" href="/#contact">Book a demo <Arrow size={16} /></Link>
    </div>
  );
}

export default function Nav() {
  return (
    <header className="nav">
      <div className="wrap">
        <Link className="logo" href="/" aria-label="Home">
          <Image src="/brand/wordmark.png" alt="Company wordmark" width={229} height={30} priority />
        </Link>
        <ul>
          {nav.map((n) => (
            <li key={n.href} className={n.menu ? "has-menu" : undefined}>
              <Link href={n.href}>{n.label}{n.menu && <span className="caret" aria-hidden="true" />}</Link>
              {n.menu === "services" && <ServicesMenu />}
              {n.menu === "solutions" && <SolutionsMenu />}
            </li>
          ))}
        </ul>
        <div className="nav-r">
          <Link className="srch" href="/services/" aria-label="Browse services"><Search /></Link>
          <Link className="btn btn-cyan" href="/#contact">Contact Us <Arrow /></Link>
          <details className="mnav">
            <summary aria-label="Open menu"><span /><span /><span /></summary>
            <div className="mnav-panel">
              {nav.map((n) => <Link key={n.href} href={n.href}>{n.label}</Link>)}
              <Link href="/#contact">Contact</Link>
            </div>
          </details>
        </div>
      </div>
    </header>
  );
}
