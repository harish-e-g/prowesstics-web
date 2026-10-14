import Image from "next/image";
import { images } from "@/content/images";

type Props = {
  id: string;
  label?: string;
  note?: string;
  light?: boolean;
  className?: string;
  sizes?: string;
  priority?: boolean;
  zoom?: boolean;
};

// Renders the real image once its "src" is set in content/images.ts, otherwise a labelled placeholder.
// When zoom is on, clicking opens the slot's "detail" image (or the image itself) in the lightbox.
export default function ImageSlot({ id, label, note, light, className = "", sizes = "100vw", priority, zoom }: Props) {
  const slot = images[id];
  const filled = Boolean(slot?.src);
  const canZoom = filled && zoom;
  const cls = ["ph", light ? "light" : "", filled ? "filled" : "", slot?.cutout ? "cut" : "", canZoom ? "zoomable" : "", className].filter(Boolean).join(" ");
  return (
    <div
      className={cls}
      {...(canZoom
        ? { "data-zoom": slot.detail || slot.src, "data-zoom-alt": slot.alt, role: "button", tabIndex: 0, "aria-label": `Enlarge: ${slot.alt}` }
        : {})}
    >
      {filled ? (
        <>
          <Image src={slot.src as string} alt={slot.alt} fill sizes={sizes} priority={priority} />
          {canZoom && <span className="zoom-hint" aria-hidden="true">View detail</span>}
        </>
      ) : (
        <span className="tag">
          {id}
          {label ? ` · ${label}` : ""}
          {note ? <span>{note}</span> : null}
        </span>
      )}
    </div>
  );
}
