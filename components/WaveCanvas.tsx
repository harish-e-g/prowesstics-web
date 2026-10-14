"use client";
import { useEffect, useRef } from "react";

// Animated dotted data wave in the hero. Respects reduced-motion by drawing one still frame.
export default function WaveCanvas() {
  const ref = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const cv = ref.current;
    if (!cv) return;
    const ctx = cv.getContext("2d");
    if (!ctx) return;
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    let W = 0, H = 0, t = 0, raf = 0;

    const size = () => {
      const d = Math.min(window.devicePixelRatio || 1, 2);
      W = cv.clientWidth; H = cv.clientHeight;
      cv.width = W * d; cv.height = H * d;
      ctx.setTransform(d, 0, 0, d, 0, 0);
    };
    const draw = () => {
      ctx.clearRect(0, 0, W, H);
      const cols = Math.round(W / 7), rows = 26;
      for (let j = 0; j < rows; j++) {
        const z = j / rows;
        for (let i = 0; i < cols; i++) {
          const u = i / cols;
          const y = H * (0.35 + z * 0.6) + Math.sin(u * 7 + t + z * 3) * H * 0.07 * (1 - z * 0.4) + Math.cos(u * 3 - t * 0.6) * H * 0.05;
          const x = u * W * (1 + z * 0.25) - z * W * 0.12;
          const g = Math.min(1, Math.max(0, (u - 0.15) / 0.75));
          const r = Math.round(46 + 186 * g * g), gg = Math.round(197 - 17 * g * g), b = Math.round(220 - 138 * g * g);
          ctx.fillStyle = `rgba(${r},${gg},${b},${(0.15 + 0.75 * z) * (1 - u * 0.25)})`;
          ctx.fillRect(x, y, 1.2 + z * 1.6, 1.2 + z * 1.6);
        }
      }
    };
    const loop = () => { t += 0.012; draw(); raf = requestAnimationFrame(loop); };
    const onResize = () => { size(); draw(); };

    size(); draw();
    window.addEventListener("resize", onResize);
    if (!reduce) raf = requestAnimationFrame(loop);
    return () => { cancelAnimationFrame(raf); window.removeEventListener("resize", onResize); };
  }, []);

  return <canvas id="wave" ref={ref} aria-hidden="true" />;
}
