import { chromium } from "playwright";
import fs from "fs";
const rows = JSON.parse(fs.readFileSync("rows.json","utf8")); fs.mkdirSync("png",{recursive:true});
const b = await chromium.launch(); const p = await b.newPage({ deviceScaleFactor: 1 });
const out = [];
for (const r of Object.values(rows)) for (const { id } of r) {
  const svg = fs.readFileSync("svg/"+id+".svg","utf8");
  await p.setContent('<html><body style="margin:0;background:transparent"><div id="w" style="display:inline-block;height:120px">'+svg.replace(/<\?xml[^>]*>/,"")+'</div></body></html>');
  await p.evaluate(() => { const s = document.querySelector("#w svg"); const vb = s.viewBox.baseVal; let w = vb && vb.width ? vb.width : s.getBBox().width, h = vb && vb.height ? vb.height : s.getBBox().height; s.setAttribute("height", 120); s.setAttribute("width", Math.round(120 * w / h)); s.style.display = "block"; });
  const el = await p.$("#w svg"); await el.screenshot({ path: "png/"+id+".png", omitBackground: true });
  out.push(id);
}
console.log(out.length); await b.close();
