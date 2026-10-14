import type { SVGProps } from "react";

type P = SVGProps<SVGSVGElement> & { size?: number };

export function Arrow({ size = 18, ...p }: P) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2.4} aria-hidden="true" {...p}>
      <path d="M5 12h14M13 6l6 6-6 6" />
    </svg>
  );
}
export function Chevron({ size = 16, dir = "right", ...p }: P & { dir?: "left" | "right" }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2.6} aria-hidden="true" {...p}>
      <path d={dir === "right" ? "m9 6 6 6-6 6" : "m15 6-6 6 6 6"} />
    </svg>
  );
}
export function Search(p: P) {
  return (
    <svg width={20} height={20} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2.2} aria-hidden="true" {...p}>
      <circle cx="11" cy="11" r="7" />
      <path d="m20 20-3.5-3.5" />
    </svg>
  );
}
export function Play() {
  return (
    <svg width={20} height={20} viewBox="0 0 24 24" fill="#2EC5DC" aria-hidden="true">
      <path d="M8 5v14l11-7z" />
    </svg>
  );
}

const line = { fill: "none", stroke: "currentColor" } as const;

export function StatGlyph({ name }: { name: string }) {
  const c = { width: 34, height: 34, viewBox: "0 0 24 24", strokeWidth: 1.6, "aria-hidden": true, ...line };
  switch (name) {
    case "team":
      return <svg {...c}><circle cx="12" cy="8" r="3.5" /><path d="M5 20c.8-3.6 3.6-5.5 7-5.5s6.2 1.9 7 5.5" /><circle cx="4.5" cy="10" r="2" /><circle cx="19.5" cy="10" r="2" /></svg>;
    case "spark":
      return <svg {...c}><circle cx="12" cy="12" r="3" /><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1 7 17M17 7l2.1-2.1" /></svg>;
    case "experts":
      return <svg {...c}><circle cx="9" cy="8" r="3.2" /><path d="M3 20c.6-3.4 3-5.2 6-5.2s5.4 1.8 6 5.2" /><path d="M16 4.5a3 3 0 0 1 0 6M18 14.8c1.7.6 2.7 2.4 3 5.2" /></svg>;
    case "db":
      return <svg {...c}><ellipse cx="12" cy="6" rx="7" ry="2.6" /><path d="M5 6v6c0 1.4 3.1 2.6 7 2.6s7-1.2 7-2.6V6M5 12v6c0 1.4 3.1 2.6 7 2.6s7-1.2 7-2.6v-6" /></svg>;
    default:
      return <svg {...c}><circle cx="12" cy="12" r="9" /><path d="M3 12h18M12 3c2.6 2.6 3.8 5.6 3.8 9s-1.2 6.4-3.8 9c-2.6-2.6-3.8-5.6-3.8-9S9.4 5.6 12 3Z" /></svg>;
  }
}

export function IndustryGlyph({ name, color }: { name: string; color: string }) {
  const c = { width: 34, height: 34, viewBox: "0 0 24 24", fill: "none", stroke: color, strokeWidth: 1.7, "aria-hidden": true } as const;
  switch (name) {
    case "factory":
      return <svg {...c}><path d="M3 21V10l5 3V10l5 3V7l8 4v10Z" /><path d="M7 17h2M12 17h2M17 17h2" /></svg>;
    case "bank":
      return <svg {...c}><path d="M3 9 12 4l9 5M5 9v9M9.5 9v9M14.5 9v9M19 9v9M3 20h18" /></svg>;
    case "network":
      return <svg {...c}><circle cx="6" cy="18" r="2.2" /><circle cx="18" cy="18" r="2.2" /><circle cx="12" cy="5" r="2.2" /><path d="M11 7 7 16M13 7l4 9M8.2 18h7.6" /></svg>;
    case "bag":
      return <svg {...c}><path d="M4 8h16l-1.5 11a2 2 0 0 1-2 1.7h-9a2 2 0 0 1-2-1.7Z" /><path d="M9 8V6a3 3 0 0 1 6 0v2" /></svg>;
    case "car":
      return <svg {...c}><path d="M3 16v-3l2-5a2 2 0 0 1 1.9-1.3h10.2A2 2 0 0 1 19 8l2 5v3a1 1 0 0 1-1 1h-1" /><path d="M6 17H4M3 13h18" /><circle cx="7.5" cy="17" r="2" /><circle cx="16.5" cy="17" r="2" /><path d="M9.5 17h5" /></svg>;
    case "bolt":
      return <svg {...c}><path d="M13 2 4 14h7l-1 8 9-12h-7Z" /></svg>;
    case "crane":
      return <svg {...c}><path d="M6 21V4h2v17M3 21h9M8 4h12l-3 3M8 7h9M17 7v5" /><rect x="15" y="12" width="4" height="3" /></svg>;
    case "plane":
      return <svg {...c}><path d="M21 15.5 13.5 11V5a1.5 1.5 0 0 0-3 0v6L3 15.5V17l7.5-2.2V19l-2 1.5V22l3.5-1 3.5 1v-1.5l-2-1.5v-4.2L21 17Z" /></svg>;
    default:
      return <svg {...c}><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10Z" /><path d="M5 12h3l1.5-2.5 2 5 1.5-2.5H19" /></svg>;
  }
}

export function ServiceGlyph({ name }: { name: string }) {
  const c = { className: "ic", width: 32, height: 32, viewBox: "0 0 24 24", strokeWidth: 1.8, "aria-hidden": true, ...line };
  switch (name) {
    case "db":
      return <svg {...c}><ellipse cx="12" cy="6" rx="7" ry="2.6" /><path d="M5 6v6c0 1.4 3.1 2.6 7 2.6s7-1.2 7-2.6V6M5 12v6c0 1.4 3.1 2.6 7 2.6s7-1.2 7-2.6v-6" /></svg>;
    case "bars":
      return <svg className="ic" width={32} height={32} viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><rect x="4" y="12" width="4" height="8" rx="1" /><rect x="10" y="7" width="4" height="13" rx="1" /><rect x="16" y="3" width="4" height="17" rx="1" /></svg>;
    case "cloud":
      return <svg {...c}><path d="M7 18a4.5 4.5 0 0 1-.7-9 6 6 0 0 1 11.4 1.5A3.8 3.8 0 0 1 17.2 18Z" /></svg>;
    case "chip":
      return <svg {...c}><rect x="6" y="6" width="12" height="12" rx="2" /><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4" /><text x="12" y="14.2" fontSize="5.5" fontWeight={800} textAnchor="middle" fill="currentColor" stroke="none" fontFamily="sans-serif">AI</text></svg>;
    case "eye":
      return <svg {...c}><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12Z" /><circle cx="12" cy="12" r="3" /></svg>;
    case "gear":
      return <svg {...c}><circle cx="12" cy="12" r="3" /><path d="M19.4 15a1.6 1.6 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.6 1.6 0 0 0-2.7 1.1v.3a2 2 0 1 1-4 0v-.2a1.6 1.6 0 0 0-2.7-1.1l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1A1.6 1.6 0 0 0 3.6 14h-.3a2 2 0 1 1 0-4h.2a1.6 1.6 0 0 0 1.1-2.7l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1A1.6 1.6 0 0 0 10 3.6v-.3a2 2 0 1 1 4 0v.2a1.6 1.6 0 0 0 2.7 1.1l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.6 1.6 0 0 0-.3 1.8" /></svg>;
    case "trend":
      return <svg {...c}><path d="M3 17l5-5 4 4 8-8" /><path d="M14 8h6v6" /></svg>;
    default:
      return <svg {...c}><circle cx="9" cy="8" r="3.2" /><path d="M3 20c.6-3.4 3-5.2 6-5.2s5.4 1.8 6 5.2" /><path d="M17 8v6M14 11h6" /></svg>;
  }
}
