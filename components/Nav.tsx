import Image from "next/image";
import { nav } from "@/content/site";
import { Arrow, Search } from "./icons";

export default function Nav() {
  return (
    <header className="nav">
      <div className="wrap">
        <a className="logo" href="#top" aria-label="Prowesstics home">
          <Image src="/brand/wordmark.png" alt="Prowesstics" width={229} height={30} priority />
        </a>
        <ul>
          {nav.map((n) => (
            <li key={n.href}><a href={n.href}>{n.label}</a></li>
          ))}
        </ul>
        <div className="nav-r">
          <a className="srch" href="#services" aria-label="Search services"><Search /></a>
          <a className="btn btn-cyan" href="#contact">Contact Us <Arrow /></a>
        </div>
      </div>
    </header>
  );
}
