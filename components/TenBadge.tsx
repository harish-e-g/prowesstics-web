// Graphical "10" for the hero: a sculpted, glossy "1" and a glass ring "0" with a gold rim.
// Pure SVG + CSS animation (no JavaScript per frame): a one-time reveal, then a slow gold orbit,
// a periodic light sweep, a breathing halo and soft anniversary sparkles.
// prefers-reduced-motion shows the finished still design.
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
        <linearGradient id="tSweep" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0" stopColor="#FFFFFF" stopOpacity="0" />
          <stop offset="0.5" stopColor="#FFFFFF" stopOpacity="0.55" />
          <stop offset="1" stopColor="#FFFFFF" stopOpacity="0" />
        </linearGradient>
        <radialGradient id="tSpark" cx="0.5" cy="0.5" r="0.5">
          <stop offset="0" stopColor="#FFF8E6" />
          <stop offset="0.35" stopColor="#FFE3A3" stopOpacity="0.85" />
          <stop offset="1" stopColor="#E8B452" stopOpacity="0" />
        </radialGradient>
        <filter id="tGlow" x="-30%" y="-30%" width="160%" height="160%">
          <feGaussianBlur stdDeviation="14" />
        </filter>
        {/* the numerals' faces, for the light sweep */}
        <clipPath id="tFaces">
          <path d="M30 60 L104 18 L104 236 L60 236 L60 92 L30 108 Z" />
          <path clipRule="evenodd" d="M214 16a116 116 0 1 0 0.01 0ZM214 56a76 76 0 1 1 -0.01 0Z" />
        </clipPath>
        {/* everything except the "1", so the orbiting gold passes behind it */}
        <clipPath id="tBehindOne">
          <path clipRule="evenodd" d="M-60 -60H420V330H-60ZM30 60L104 18L110 22L118 30L118 240L60 240L60 92L30 108Z" />
        </clipPath>
      </defs>

      {/* Glow behind */}
      <g className="ten-halo" filter="url(#tGlow)" opacity="0.75">
        <circle cx="214" cy="132" r="96" fill="none" stroke="#2EC5DC" strokeWidth="30" />
        <rect x="44" y="26" width="58" height="208" rx="10" fill="#2EC5DC" />
      </g>

      {/* The "1": side face for depth, then front face, then edge highlight */}
      <g className="ten-one">
        <path d="M44 62 L110 22 L118 30 L118 240 L110 236 Z" fill="url(#tOneSide)" />
        <path d="M30 60 L104 18 L104 236 L60 236 L60 92 L30 108 Z" fill="url(#tOne)" />
        <path d="M30 60 L104 18 L104 34 L36 72 Z" fill="#FFFFFF" opacity="0.35" />
        <path d="M60 92 L64 92 L64 236 L60 236 Z" fill="#FFFFFF" opacity="0.18" />
      </g>

      {/* The "0": glass ring */}
      <g className="ten-ring">
        <circle cx="214" cy="132" r="80" fill="url(#tCore)" />
        <circle cx="214" cy="132" r="96" fill="none" stroke="url(#tRing)" strokeWidth="40" />
        {/* inner bevel */}
        <circle cx="214" cy="132" r="76" fill="none" stroke="#9BF6FF" strokeOpacity="0.55" strokeWidth="2" />
        {/* top-left sheen */}
        <path d="M140 92 A96 96 0 0 1 238 38" fill="none" stroke="url(#tSheen)" strokeWidth="14" strokeLinecap="round" opacity="0.7" />
      </g>

      {/* light sweep across both numerals, every few seconds */}
      <g clipPath="url(#tFaces)" className="ten-sweepwrap">
        <rect className="ten-sweep" x="-90" y="-20" width="70" height="300" fill="url(#tSweep)" transform="skewX(-18)" />
      </g>

      {/* gold rim on the lower right: draws in, then orbits slowly with a bright leading glint */}
      <g clipPath="url(#tBehindOne)">
      <g className="ten-orbit">
        <circle className="ten-gold" cx="214" cy="132" r="116" fill="none" stroke="url(#tGold)" strokeWidth="5" strokeLinecap="round"
          strokeDasharray="250 480" strokeDashoffset="-40" />
        <g className="ten-lead">
          <circle cx="121.4" cy="201.8" r="13" fill="url(#tSpark)" />
          <circle cx="121.4" cy="201.8" r="2.6" fill="#FFF8E6" />
        </g>
      </g>
      </g>

      {/* anniversary sparkles */}
      <g className="ten-sparks">
        <path className="ten-spark" style={{ animationDelay: "2.4s", transformOrigin: "312px 34px" }} d="M312 27Q313.5 32.5 319 34Q313.5 35.5 312 41Q310.5 35.5 305 34Q310.5 32.5 312 27Z" fill="#FFE3A3" />
        <path className="ten-spark" style={{ animationDelay: "3.7s", transformOrigin: "338px 168px" }} d="M338 163Q339.1 166.9 343 168Q339.1 169.1 338 173Q336.9 169.1 333 168Q336.9 166.9 338 163Z" fill="#FFE3A3" />
        <path className="ten-spark" style={{ animationDelay: "5.0s", transformOrigin: "150px 14px" }} d="M150 9Q151.1 12.9 155 14Q151.1 15.1 150 19Q148.9 15.1 145 14Q148.9 12.9 150 9Z" fill="#FFE3A3" />
        <path className="ten-spark" style={{ animationDelay: "6.3s", transformOrigin: "318px 250px" }} d="M318 244Q319.3 248.7 324 250Q319.3 251.3 318 256Q316.7 251.3 312 250Q316.7 248.7 318 244Z" fill="#FFE3A3" />
        <path className="ten-spark" style={{ animationDelay: "7.6s", transformOrigin: "16px 40px" }} d="M16 35Q17.1 38.9 21 40Q17.1 41.1 16 45Q14.9 41.1 11 40Q14.9 38.9 16 35Z" fill="#FFE3A3" />
        <path className="ten-spark" style={{ animationDelay: "8.9s", transformOrigin: "260px 8px" }} d="M260 4Q260.9 7.1 264 8Q260.9 8.9 260 12Q259.1 8.9 256 8Q259.1 7.1 260 4Z" fill="#FFE3A3" />
      </g>
    </svg>
  );
}
