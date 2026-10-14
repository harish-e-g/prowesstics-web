import Image from "next/image";
import { hero, stats } from "@/content/site";
import { images } from "@/content/images";
import ImageSlot from "./ImageSlot";
import WaveCanvas from "./WaveCanvas";
import FilmButton from "./FilmButton";
import TenBadge from "./TenBadge";
import { Arrow, StatGlyph } from "./icons";

export default function Hero() {
  const badge = images["IMG-16"];
  return (
    <>
      <section className="hero">
        <ImageSlot id="IMG-01" label="Hero background" note="Leadership team, glass boardroom, city at dusk" className="hero-bg" priority sizes="(max-width: 960px) 100vw, 54vw" />
        <WaveCanvas />
        <div className="vert v1" aria-hidden="true">{hero.sideTop.map((w) => <span key={w}>{w}<br /></span>)}</div>
        <div className="vert v2" aria-hidden="true">{hero.sideBottom.map((w) => <span key={w}>{w}<br /></span>)}</div>
        <div className="wrap">
          <div>
            <div className="kick">
              {hero.kicker.map((k, i) => (
                <span key={k}>{i > 0 && <i>| </i>}{k}</span>
              ))}
            </div>
            <div className="kick-rule" />
            <h1>{hero.title}<span className="c">{hero.highlight}</span></h1>
            <p className="lede">{hero.lede}</p>
            <div className="hero-cta">
              <a className="btn btn-grad" href="#solutions">Explore Our Solutions <Arrow size={20} /></a>
              <FilmButton />
            </div>
          </div>
          <div className="badge">
            {badge?.src ? (
              <Image src={badge.src} alt="" width={260} height={260} />
            ) : (
              <TenBadge />
            )}
            <div className="badge-t">{hero.badgeText.map((l) => <span key={l}>{l}<br /></span>)}</div>
          </div>
        </div>
      </section>

      <div className="stats" aria-label="Track record">
        <div className="wrap">
          {stats.map((s) => (
            <div className="st" key={s.value}>
              <StatGlyph name={s.icon} />
              <div className="st-t">
                <b>{s.value}</b>
                <span>{s.label[0]} {s.label[1]}</span>
              </div>
            </div>
          ))}
        </div>
      </div>

    </>
  );
}
