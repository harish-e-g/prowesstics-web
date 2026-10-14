import Image from "next/image";
import { footerCols, site } from "@/content/site";

export default function Footer() {
  return (
    <footer>
      <div className="wrap">
        <div className="fgrid">
          <div>
            <Image src="/brand/wordmark.png" alt="Prowesstics" width={198} height={26} />
            <p>Data engineering, AI and factory automation that deliver measurable business impact.</p>
          </div>
          {footerCols.map((c) => (
            <div key={c.title}>
              <b>{c.title}</b>
              {c.links.map(([label, href]) => <a key={label} href={href}>{label}</a>)}
            </div>
          ))}
        </div>
        <div className="fbot">
          <span>© {new Date().getFullYear()} {site.legalName} All rights reserved.</span>
          <span>{site.locations}</span>
        </div>
      </div>
    </footer>
  );
}
