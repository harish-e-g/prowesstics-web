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
};

// Renders the real image once its "src" is set in content/images.ts, otherwise a labelled placeholder.
export default function ImageSlot({ id, label, note, light, className = "", sizes = "100vw", priority }: Props) {
  const slot = images[id];
  const filled = Boolean(slot?.src);
  const cls = ["ph", light ? "light" : "", filled ? "filled" : "", slot?.cutout ? "cut" : "", className].filter(Boolean).join(" ");
  return (
    <div className={cls}>
      {filled ? (
        <Image src={slot.src as string} alt={slot.alt} fill sizes={sizes} priority={priority} />
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
