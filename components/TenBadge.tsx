// Graphical "10" for the hero: a sculpted, glossy "1" and a glass ring "0" with a gold rim.
// Pure SVG, so it stays sharp at any size and never clips.
export default function TenBadge() {
  return (
    <svg className="ten-svg" viewBox="0 0 348 262" role="img" aria-label="10 years">
      <defs>
        <linearGradient id="tOne" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stopColor="#9BF6FF" />
          <stop offset="0.35" stopColor="#2EC5DC" />
          <stop offset="0.75" stopColor="#1A6FE0" />
          <stop offset="1" stopColor="#0B2C7A" />
        </linearGradient>
        <linearGradient id="tOneSide" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0" stopColor="#0B2C7A" />
          <stop offset="1" stopColor="#123F9E" />
        </linearGradient>
        <linearGradient id="tRing" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stopColor="#B8FBFF" />
          <stop offset="0.3" stopColor="#2EC5DC" />
          <stop offset="0.62" stopColor="#1A7FE0" />
          <stop offset="1" stopColor="#0A2A86" />
        </linearGradient>
        <linearGradient id="tGold" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stopColor="#FFE3A3" />
          <stop offset="0.5" stopColor="#E8B452" />
          <stop offset="1" stopColor="#B8801F" />
        </linearGradient>
        <radialGradient id="tCore" cx="0.5" cy="0.5" r="0.5">
          <stop offset="0" stopColor="#0B2C7A" stopOpacity="0.95" />
          <stop offset="0.7" stopColor="#081A4A" stopOpacity="0.9" />
          <stop offset="1" stopColor="#2EC5DC" stopOpacity="0.55" />
        </radialGradient>
        <linearGradient id="tSheen" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stopColor="#FFFFFF" stopOpacity="0.85" />
          <stop offset="0.5" stopColor="#FFFFFF" stopOpacity="0" />
        </linearGradient>
        <filter id="tGlow" x="-30%" y="-30%" width="160%" height="160%">
          <feGaussianBlur stdDeviation="14" />
        </filter>
      </defs>

      {/* Glow behind */}
      <g filter="url(#tGlow)" opacity="0.75">
        <circle cx="214" cy="132" r="96" fill="none" stroke="#2EC5DC" strokeWidth="30" />
        <rect x="44" y="26" width="58" height="208" rx="10" fill="#2EC5DC" />
      </g>

      {/* The "1": side face for depth, then front face, then edge highlight */}
      <path d="M44 62 L110 22 L118 30 L118 240 L110 236 Z" fill="url(#tOneSide)" />
      <path d="M30 60 L104 18 L104 236 L60 236 L60 92 L30 108 Z" fill="url(#tOne)" />
      <path d="M30 60 L104 18 L104 34 L36 72 Z" fill="#FFFFFF" opacity="0.35" />
      <path d="M60 92 L64 92 L64 236 L60 236 Z" fill="#FFFFFF" opacity="0.18" />

      {/* The "0": glass ring */}
      <circle cx="214" cy="132" r="80" fill="url(#tCore)" />
      <circle cx="214" cy="132" r="96" fill="none" stroke="url(#tRing)" strokeWidth="40" />
      {/* inner bevel */}
      <circle cx="214" cy="132" r="76" fill="none" stroke="#9BF6FF" strokeOpacity="0.55" strokeWidth="2" />
      {/* gold rim on the lower right, like a light catching the edge */}
      <circle cx="214" cy="132" r="116" fill="none" stroke="url(#tGold)" strokeWidth="5" strokeLinecap="round"
        strokeDasharray="250 480" strokeDashoffset="-40" transform="rotate(0 214 132)" />
      {/* top-left sheen */}
      <path d="M140 92 A96 96 0 0 1 238 38" fill="none" stroke="url(#tSheen)" strokeWidth="14" strokeLinecap="round" opacity="0.7" />
    </svg>
  );
}
