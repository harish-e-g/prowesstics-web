// Renders render.html in headless Chromium (WebGL via SwiftShader) and saves the PNG and the
// projected zero contours. Serve this folder first (python3 -m http.server 8822), with three@0.169.0
// installed here (npm i three@0.169.0). Usage: node shot.mjs "<query>" render.png
import { chromium } from "playwright";
import fs from "fs";
const q = process.argv[2] || ""; const out = process.argv[3] || "render.png";
const b = await chromium.launch({ args: ["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"] });
const p = await b.newPage({ viewport: { width: 400, height: 300 } });
await p.goto("http://localhost:8822/render.html?" + q);
await p.waitForFunction(() => window.__done || false, null, { timeout: 120000 });
const data = await p.evaluate(() => document.querySelector("canvas").toDataURL("image/png"));
fs.writeFileSync(out, Buffer.from(data.split(",")[1], "base64"));
fs.writeFileSync(out.replace(".png", ".json").replace("render", "contours"), JSON.stringify(await p.evaluate(() => window.__contours)));
await b.close();
