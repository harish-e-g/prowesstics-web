# Changelog

All notable changes to the Prowesstics website are recorded here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- GitHub Pages publishing: `.github/workflows/deploy-pages.yml` builds and deploys on every push to `main`; live at https://harish-e-g.github.io/prowesstics-web/.
- `NEXT_PUBLIC_BASE_PATH` support and a static image loader (`lib/image-loader.ts`) so every image, logo and lightbox view works when the site is served from a sub-folder.
- Technical, data-driven visuals across every image slot: detection boxes with confidence, 2D-to-wireframe conversion, measurements, thermal and footfall heat maps, data panels, event streams and part genealogy.
- Service card visuals combining real hardware cut-outs with live data callouts.
- Card and detail versions of product images; click any product, industry or contact image to open the full technical view in a lightbox (keyboard and Escape supported).
- `tools/visuals/` generators that reproduce every overlay from the source photos.
- Complete repository documentation: README, licence, contributing guide, security policy, issue and pull request templates, repository settings.

### Changed
- IND-03 BFSI image replaced with a full-colour scene with a clear desk.
- IND-05 retail image replaced with a sharp-focus scene; IMG-13 ProSight AI image replaced with a clean full-frame hypermarket.
- Image frames now match the 16:9 images exactly so no callout is cropped.

## [1.0.0] - 2026-10-14

### Added
- Next.js 15 App Router homepage with TypeScript and self-hosted Nunito Sans.
- Hero with headline "Trusted Data. Working AI. Real Business Impact.", animated data wave, 3D "10 years" badge and company film dialog.
- Track record bar, eight service cards with outcome metrics, nine-industry grid, six client commitments.
- Product cards for ProVision AI, ProChurn AI, DEO Suite, ProSight AI and ProTrace AI.
- Four-step engagement model, client logo marquee, eight before-and-after results.
- Two-row technology marquee with 27 platform logos.
- Ten client testimonials in a keyboard-operable carousel.
- Consultation form with validation and sales email copy button.
- SEO: metadata, Open Graph, Organization and SoftwareApplication JSON-LD, sitemap.xml and robots.txt.
- Image slot system with labelled placeholders and a central image register.
- Static export mode for previews.

### Security
- Next.js pinned to 15.5.27 and postcss overridden to 8.5.28; `npm audit` reports 0 vulnerabilities.
