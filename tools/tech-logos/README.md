# Technology logos ("Fluent in your stack")

Logos only: no version numbers, years or separate captions. 78 technologies in three rows
(`content/site.ts`: `tech_platforms`, `tech_data`, `tech_ai`), served from `public/tech/<id>.webp`
at 72 px tall (2x the 34 px display height; 26 px on phones).

## Sources (official marks only)
- `@iconify-json/logos@1.2.4` (gilbarbara/logos): full-colour wordmarks and symbols
- `simple-icons@13.21.0`: brand symbols with official brand colours
- `devicon@2.16.0` / `2.17.0`: SQL Server, scikit-learn, OpenCV, Jupyter, Kubeflow symbols
- Downloaded from the owners or public brand libraries: Microsoft Fabric (Microsoft's official Fabric
  icon pack, `microsoft/fabric-samples`), Fivetran (fivetran.com), Delta Lake (delta.io),
  Honeywell (Wikimedia Commons), Confluent and Apache Iceberg (homarr-labs/dashboard-icons)

Where a brand's official mark is a symbol only, it is locked up with the brand name in Inter Medium,
so every tile reads as one logo.

## Rebuild
1. `npm i @iconify-json/logos@1.2.4 simple-icons@13.21.0 devicon@2.16.0 playwright`
2. `node build.mjs write` (writes `svg/` and `rows.json`)
3. `node render.mjs` (renders transparent PNGs with Chromium), then trim, resize to 72 px tall and
   save as WebP (quality 88) into `public/tech/`.
