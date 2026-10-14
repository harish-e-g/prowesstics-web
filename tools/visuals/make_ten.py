"""Generates components/TenBadge.tsx: the sculpted SVG "10" with a golden ray on the zero's contour.

Geometry is computed here so the ray path is the zero's real outer contour (a superellipse),
and the star glints sit exactly on that contour, timed to the moment the ray passes them.
Run: python3 tools/visuals/make_ten.py
"""
import math, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "components", "TenBadge.tsx")

CX, CY = 246, 134          # zero centre
A, B, T = 78, 104, 34      # outer semi-axes and wall thickness
N = 2.5                    # superellipse exponent: squarer than an ellipse, softer than a rectangle
DX, DY = 7, 9              # extrusion depth (towards bottom right)
PERIOD = 9                 # seconds per lap of the golden ray
START = 1.4                # seconds before the ray appears (after the reveal)

def sgn(v): return (v > 0) - (v < 0)

def superellipse(a, b, n, cx, cy, steps=720, start=-math.pi / 2):
    pts = []
    for i in range(steps):
        t = start + 2 * math.pi * i / steps
        c, s = math.cos(t), math.sin(t)
        pts.append((cx + a * sgn(c) * abs(c) ** (2 / n), cy + b * sgn(s) * abs(s) ** (2 / n)))
    return pts

def resample(pts, count):
    """Even spacing by arc length, so path length fractions match the visible position."""
    closed = pts + [pts[0]]
    seg = [math.dist(closed[i], closed[i + 1]) for i in range(len(pts))]
    total = sum(seg)
    out, acc, j = [], 0.0, 0
    for k in range(count):
        target = total * k / count
        while acc + seg[j] < target:
            acc += seg[j]; j += 1
        f = (target - acc) / seg[j]
        (x0, y0), (x1, y1) = closed[j], closed[j + 1]
        out.append((x0 + (x1 - x0) * f, y0 + (y1 - y0) * f))
    return out, total

def smooth_path(pts):
    """Closed Catmull-Rom spline through the points, written as cubic Beziers."""
    n = len(pts)
    d = [f"M{pts[0][0]:.2f} {pts[0][1]:.2f}"]
    for i in range(n):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d.append(f"C{c1[0]:.2f} {c1[1]:.2f} {c2[0]:.2f} {c2[1]:.2f} {p2[0]:.2f} {p2[1]:.2f}")
    return "".join(d) + "Z"

def contour(a, b, dx=0, dy=0, count=96):
    pts, _ = resample(superellipse(a, b, N, CX + dx, CY + dy), count)
    return pts

outer = contour(A, B)
inner = contour(A - T, B - T)
# the counter is drawn in the opposite direction so the zero is one closed ring (nonzero fill)
ZERO = smooth_path(outer) + smooth_path(inner[::-1])
ZERO_BACK = smooth_path(contour(A, B, DX, DY)) + smooth_path(contour(A - T, B - T, DX, DY)[::-1])
OUTER = smooth_path(outer)
INNER = smooth_path(inner)
RAY = smooth_path(contour(A + 0.4, B + 0.4))  # the light rides on the outer rim

# numeral 1: a tapered flag and a straight stem, the same height as the zero
TOP, BOT = CY - B, CY + B
ONE_PTS = [(147, TOP), (147, BOT), (93, BOT), (93, TOP + 72), (59, TOP + 86), (59, TOP + 44), (106, TOP)]
ONE = "M" + "L".join(f"{x} {y}" for x, y in ONE_PTS) + "Z"
ONE_BACK = "M" + "L".join(f"{x + DX} {y + DY}" for x, y in ONE_PTS) + "Z"

# true extrusion: one quad per edge between the front face and the face pushed back by (DX, DY),
# shaded by which way the wall faces (light from the upper left), grouped into a few tones
def walls(poly):
    """Union of the visible side quads for one closed outline, as a single path."""
    out, n = [], len(poly)
    for i in range(n):
        (x0, y0), (x1, y1) = poly[i], poly[(i + 1) % n]
        ex, ey = x1 - x0, y1 - y0
        nx, ny = ey, -ex                          # outward normal for a clockwise-on-screen loop
        if nx * DX + ny * DY <= 0:                # wall turned away from the viewer: hidden
            continue
        out.append(f"M{x0:.2f} {y0:.2f}L{x1:.2f} {y1:.2f}L{x1 + DX:.2f} {y1 + DY:.2f}L{x0 + DX:.2f} {y0 + DY:.2f}Z")
    return "".join(out)

# glints at chosen fractions of the lap, delayed so each fires as the ray head passes
ray_pts, _ = resample(superellipse(A + 0.4, B + 0.4, N, CX, CY), 1000)
GLINTS = [0.12, 0.47, 0.71]
STILL = 0.13  # where the light rests when motion is reduced (upper right shoulder)

def star(x, y, r):
    k = r * 0.22
    return (f"M{x:.1f} {y - r:.1f}Q{x + k:.1f} {y - k:.1f} {x + r:.1f} {y:.1f}"
            f"Q{x + k:.1f} {y + k:.1f} {x:.1f} {y + r:.1f}Q{x - k:.1f} {y + k:.1f} {x - r:.1f} {y:.1f}"
            f"Q{x - k:.1f} {y - k:.1f} {x:.1f} {y - r:.1f}Z")

glint_svg = []
for f in GLINTS:
    x, y = ray_pts[int(f * 1000) % 1000]
    glint_svg.append(
        f'          <g className="ten-glint" style={{{{ animationDelay: "{START + f * PERIOD:.2f}s", transformOrigin: "{x:.1f}px {y:.1f}px" }}}}>\n'
        f'            <path d="{star(x, y, 11)}" fill="#FFF3D6" />\n'
        f'            <circle cx="{x:.1f}" cy="{y:.1f}" r="2.2" fill="#FFFFFF" />\n'
        f'          </g>')
sx, sy = ray_pts[int(STILL * 1000)]

# trail layers: [dash length, width, colour, opacity]; every head sits at the same point
LAYERS = [(160, 2.0, "#E8B452", 0.45), (70, 2.6, "#F2BC55", 0.75), (24, 3.2, "#FFD27A", 1), (2.5, 6, "#FFF4D6", 1)]
layer_svg = "\n".join(
    f'          <path className="ten-ray" d={{RAY}} pathLength={{1000}} strokeDasharray="0 {1000 - l:g} {l:g} 0" stroke="{c}" strokeWidth="{w}" strokeOpacity="{o}" />'
    for l, w, c, o in LAYERS)

dense_outer = contour(A, B, count=240)
dense_inner = contour(A - T, B - T, count=240)[::-1]   # counter walls face inward
walls_svg = "\n".join([
    f'        <path d="{walls(ONE_PTS)}" fill="url(#tnWall)" stroke="url(#tnWall)" strokeWidth="0.5" />',
    f'        <path d="{walls(dense_outer)}" fill="url(#tnWall)" stroke="url(#tnWall)" strokeWidth="0.5" />',
    f'        <path d="{walls(dense_inner)}" fill="url(#tnWallIn)" stroke="url(#tnWallIn)" strokeWidth="0.5" />',
])

tsx = f'''// Prowesstics 10-year mark: a sculpted "1" and a closed superellipse "0" in cyan-blue,
// with one golden ray travelling the zero's real outer contour. Generated by tools/visuals/make_ten.py.
// Pure SVG + CSS: no JavaScript runs per frame, the numerals never move after the reveal,
// and prefers-reduced-motion shows the finished still composition with the light at rest.

const ZERO = "{ZERO}";
const ZERO_BACK = "{ZERO_BACK}";
const OUTER = "{OUTER}";
const INNER = "{INNER}";
const RAY = "{RAY}";
const ONE = "{ONE}";
const ONE_BACK = "{ONE_BACK}";

export default function TenBadge() {{
  return (
    <svg className="ten-svg" viewBox="0 0 360 290" role="img" aria-label="10 years">
      <defs>
        <radialGradient id="tnStage" cx="0.5" cy="0.5" r="0.5">
          <stop offset="0" stopColor="#0E2A66" stopOpacity="0.85" />
          <stop offset="0.55" stopColor="#061330" stopOpacity="0.6" />
          <stop offset="1" stopColor="#061330" stopOpacity="0" />
        </radialGradient>
        <linearGradient id="tnFace" x1="0" y1="0" x2="0.35" y2="1">
          <stop offset="0" stopColor="#8FEAF5" />
          <stop offset="0.28" stopColor="#3CCBE0" />
          <stop offset="0.62" stopColor="#1A8FD8" />
          <stop offset="1" stopColor="#1546B8" />
        </linearGradient>
        <linearGradient id="tnWall" x1="0" y1="1" x2="1" y2="0.2">
          <stop offset="0" stopColor="#081F57" />
          <stop offset="0.55" stopColor="#123E95" />
          <stop offset="1" stopColor="#2A74D2" />
        </linearGradient>
        <linearGradient id="tnWallIn" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stopColor="#041030" />
          <stop offset="1" stopColor="#0B2A70" />
        </linearGradient>
        <linearGradient id="tnSheen" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0.18" stopColor="#FFFFFF" stopOpacity="0" />
          <stop offset="0.3" stopColor="#FFFFFF" stopOpacity="0.32" />
          <stop offset="0.36" stopColor="#FFFFFF" stopOpacity="0.06" />
          <stop offset="0.62" stopColor="#FFFFFF" stopOpacity="0" />
          <stop offset="0.7" stopColor="#BFF6FF" stopOpacity="0.14" />
          <stop offset="0.78" stopColor="#FFFFFF" stopOpacity="0" />
        </linearGradient>
        <linearGradient id="tnRimLit" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stopColor="#E9FDFF" stopOpacity="0.95" />
          <stop offset="0.45" stopColor="#9BEFFA" stopOpacity="0.35" />
          <stop offset="1" stopColor="#0B2C7A" stopOpacity="0.6" />
        </linearGradient>
        <linearGradient id="tnRimIn" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stopColor="#06205E" stopOpacity="0.9" />
          <stop offset="0.6" stopColor="#3FB8E0" stopOpacity="0.3" />
          <stop offset="1" stopColor="#D8FBFF" stopOpacity="0.85" />
        </linearGradient>
        <radialGradient id="tnCounter" cx="0.42" cy="0.38" r="0.7">
          <stop offset="0" stopColor="#0C2F7A" />
          <stop offset="1" stopColor="#051235" />
        </radialGradient>
        <radialGradient id="tnFloor" cx="0.5" cy="0.5" r="0.5">
          <stop offset="0" stopColor="#000814" stopOpacity="0.55" />
          <stop offset="1" stopColor="#000814" stopOpacity="0" />
        </radialGradient>
        <radialGradient id="tnWarm" cx="0.5" cy="0.5" r="0.5">
          <stop offset="0" stopColor="#E8B452" stopOpacity="0.35" />
          <stop offset="1" stopColor="#E8B452" stopOpacity="0" />
        </radialGradient>
        <clipPath id="tnFaces">
          <path d={{ZERO}} />
          <path d={{ONE}} />
        </clipPath>
        <clipPath id="tnZeroFace">
          <path d={{ZERO}} />
        </clipPath>
      </defs>

      {{/* environment: a quiet navy stage and a soft floor shadow */}}
      <ellipse cx="200" cy="140" rx="190" ry="150" fill="url(#tnStage)" />
      <ellipse cx="205" cy="258" rx="150" ry="14" fill="url(#tnFloor)" />

      <g className="ten-num">
        {{/* extruded depth: side walls shaded by the direction they face */}}
        <path d={{ONE_BACK}} fill="#071C4E" />
        <path d={{ZERO_BACK}} fill="#071C4E" />
{walls_svg}
        {{/* counter of the zero */}}
        <path d={{INNER}} fill="url(#tnCounter)" />
        {{/* front faces */}}
        <path d={{ONE}} fill="url(#tnFace)" />
        <path d={{ZERO}} fill="url(#tnFace)" />
        {{/* restrained metallic sheen across both numerals */}}
        <g clipPath="url(#tnFaces)" className="ten-sheen">
          <rect x="40" y="20" width="300" height="230" fill="url(#tnSheen)" />
        </g>
        {{/* bevel edges: lit from the top left */}}
        <path d={{ONE}} fill="none" stroke="url(#tnRimLit)" strokeWidth="1.6" strokeLinejoin="round" />
        <path d={{OUTER}} fill="none" stroke="url(#tnRimLit)" strokeWidth="1.6" />
        <path d={{INNER}} fill="none" stroke="url(#tnRimIn)" strokeWidth="1.6" />
      </g>

      {{/* golden ray on the zero's outer contour */}}
      <g className="ten-light">
        <circle cx="{sx:.1f}" cy="{sy:.1f}" r="38" fill="url(#tnWarm)" className="ten-warm-still" />
        <g clipPath="url(#tnZeroFace)">
          <path className="ten-ray" d={{RAY}} pathLength={{1000}} strokeDasharray="0 940 60 0" fill="none" stroke="#E8B452" strokeWidth="12" strokeOpacity="0.2" strokeLinecap="round" />
        </g>
        <g fill="none" strokeLinecap="round">
{layer_svg}
        </g>
{chr(10).join(glint_svg)}
        <g className="ten-glint-still" style={{{{ transformOrigin: "{sx:.1f}px {sy:.1f}px" }}}}>
          <path d="{star(sx, sy, 10)}" fill="#FFF3D6" />
          <circle cx="{sx:.1f}" cy="{sy:.1f}" r="2.2" fill="#FFFFFF" />
        </g>
      </g>
    </svg>
  );
}}
'''
open(OUT, "w").write(tsx)
print("wrote", os.path.normpath(OUT), "still head at", round(sx, 1), round(sy, 1))
