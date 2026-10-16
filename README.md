<p align="center">
  <img src="public/brand/wordmark.png" alt="Company wordmark" width="360">
</p>

<h3 align="center">Trusted Data. Working AI. Real Business Impact.</h3>

<p align="center">
  Official corporate website of <strong>IT Services Pvt. Ltd.</strong><br>
  Data engineering, AI and advanced analytics, computer vision and full factory automation for enterprises across India, Europe and the United States.
</p>

<p align="center">
  <img alt="Next.js" src="https://img.shields.io/badge/Next.js-15.5.27-000000?logo=nextdotjs">
  <img alt="React" src="https://img.shields.io/badge/React-19.2.8-149ECA?logo=react">
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-5.9.3-3178C6?logo=typescript&logoColor=white">
  <img alt="Node" src="https://img.shields.io/badge/Node-%3E%3D20.9-5FA04E?logo=nodedotjs&logoColor=white">
  <img alt="Licence" src="https://img.shields.io/badge/licence-proprietary-0A1F44">
  <img alt="Vulnerabilities" src="https://img.shields.io/badge/npm%20audit-0%20vulnerabilities-2EC5DC">
</p>

---

## Contents

1. [About the project](#1-about-the-project)
2. [What the homepage contains](#2-what-the-homepage-contains)
3. [Technology stack](#3-technology-stack)
4. [Project structure](#4-project-structure)
5. [Getting started](#5-getting-started)
6. [Editing content](#6-editing-content)
7. [Images and media](#7-images-and-media)
8. [Design system](#8-design-system)
9. [SEO and structured data](#9-seo-and-structured-data)
10. [Accessibility and performance](#10-accessibility-and-performance)
11. [Deployment](#11-deployment)
12. [Contact form and lead capture](#12-contact-form-and-lead-capture)
13. [Scripts reference](#13-scripts-reference)
14. [Quality checklist before every release](#14-quality-checklist-before-every-release)
15. [Roadmap](#15-roadmap)
16. [Ownership, licence and contact](#16-ownership-licence-and-contact)

---

## 1. About the project

| Item | Detail |
|---|---|
| Organisation | IT Services Pvt. Ltd. |
| Founded | 2017 |
| Locations | Plano (USA) and Chennai (India) delivery centre |
| Website | https://www.prowesstics.com |
| Sales contact | sales@prowesstics.com |
| Primary audience | Enterprise decision makers: CXOs, plant heads, heads of data, IT and operations leaders |
| Business goal | Generate qualified inbound enquiries for data, AI, vision and automation engagements |
| Project owner | Harish E G, Head of Sales and Marketing (APAC and EMEA) |
| Build | Next.js App Router, static by default, deployable to Vercel |

The site positions the company as one partner across three capability layers:

- **Data:** data engineering, cloud migration, data warehousing and data quality
- **Intelligence:** AI, machine learning, generative and agentic AI, predictive analytics and BI
- **Action:** computer vision, traceability, poka-yoke and full factory automation

## 2. What the homepage contains

Sections render in this order (see `app/page.tsx`):

| # | Section | Component | Purpose |
|---|---|---|---|
| 1 | Navigation | `components/Nav.tsx` | Wordmark, section links, search, Contact Us |
| 2 | Hero | `components/Hero.tsx` | Headline, value statement, 3D "10 years" badge, animated data wave, company film button |
| 3 | Track record bar | `components/Hero.tsx` | 10+ years, 370+ projects, 60+ certified experts, 5+ PB processed, 95% satisfaction |
| 4 | Services | `components/Sections.tsx` (`Services`) | Eight service cards with outcome metric and technology tags |
| 5 | Industries | `components/Sections.tsx` (`Industries`) | Nine industries in a 3 x 3 grid with use-case tags |
| 6 | Commitments | `components/Sections.tsx` (`Commitments`) | Six client commitments: 2-week pilot, no rip-and-replace and more |
| 7 | Solutions | `components/Sections.tsx` (`Solutions`) | ProVision AI, ProChurn AI, DEO Suite, ProSight AI, ProTrace AI |
| 8 | Engagement model | `components/Sections.tsx` (`Engage`) | Assess, Pilot, Scale, Run |
| 9 | Clients | `components/Sections.tsx` (`Clients`) | Scrolling client logo marquee |
| 10 | Results | `components/Sections.tsx` (`Results`) | Eight before-and-after outcomes |
| 11 | Technology | `components/Sections.tsx` (`TechStack`) | Two-row scrolling marquee of 27 platform logos |
| 12 | Testimonials | `components/Testimonials.tsx` | Ten client quotes in a swipeable carousel |
| 13 | Contact | `components/Contact.tsx` | Consultation form, sales email with copy button |
| 14 | Footer | `components/Footer.tsx` | Sitemap columns, legal line, locations |

## 3. Technology stack

| Layer | Choice | Version |
|---|---|---|
| Framework | Next.js (App Router) | 15.5.27 |
| UI library | React and React DOM | 19.2.8 |
| Language | TypeScript (strict mode) | 5.9.3 |
| Styling | Hand-written CSS with design tokens (`app/globals.css`) | n/a |
| Font | Nunito Sans variable, self-hosted via `@fontsource-variable/nunito-sans`; Avenir used first where installed | 5.2.7 |
| Images | `next/image` with AVIF and WebP output up to 3840 px | built in |
| Runtime | Node.js | 20.9 or newer (22 recommended, see `.nvmrc`) |
| Hosting | Vercel (recommended) | n/a |
| Security | `postcss` pinned to 8.5.28 through `overrides`; `npm audit` reports 0 vulnerabilities | n/a |

No UI framework, CSS framework or tracking script is bundled. The first load of the homepage is about 113 kB of JavaScript.

## 4. Project structure

```
prowesstics-web/
├── app/
│   ├── layout.tsx          Root layout: font, metadata, Open Graph, viewport
│   ├── page.tsx            Homepage section order and Organization structured data
│   ├── globals.css         Design tokens and all component styles
│   ├── icon.png            Favicon (company mark)
│   ├── robots.ts           Generates /robots.txt
│   └── sitemap.ts          Generates /sitemap.xml
├── components/
│   ├── Nav.tsx             Sticky navigation
│   ├── Hero.tsx            Hero, stats bar
│   ├── TenBadge.tsx        3D "10 years" SVG badge
│   ├── WaveCanvas.tsx      Animated particle wave (client component)
│   ├── FilmButton.tsx      Company film modal (client component)
│   ├── Sections.tsx        Services, Industries, Commitments, Solutions, Engage, Clients, Results, TechStack
│   ├── Testimonials.tsx    Testimonial carousel (client component)
│   ├── Contact.tsx         Contact form (client component)
│   ├── Footer.tsx          Footer
│   ├── ImageSlot.tsx       Renders an image or a labelled placeholder; optional click-to-enlarge
│   ├── Lightbox.tsx        Full-screen technical image viewer (client component)
│   └── icons.tsx           All inline SVG icons
├── content/
│   ├── site.ts             All copy and data: hero, stats, services, industries, products, clients, results, tech stack, testimonials
│   └── images.ts           Image slot register (IMG-01 to IMG-16, IND-01 to IND-09) and company film path
├── public/
│   ├── brand/              Wordmark and mark
│   ├── logos/              Client logos (transparent PNG)
│   ├── tech/               Technology logos (transparent PNG)
│   └── images/             Website photography and technical visuals
├── tools/visuals/          Python generators for the technical image overlays (see its README)
├── IMAGE_PROMPTS.md        Prompts used to generate every source photo
├── CHANGELOG.md            Release history
├── CONTRIBUTING.md         Branching, commit and review rules
├── SECURITY.md             How to report a vulnerability
├── LICENSE                 Proprietary licence
└── .github/                Issue templates, pull request template, repository settings
```

## 5. Getting started

### 5.1 Install Node.js (one time)
1. Download the **LTS** installer from https://nodejs.org and run it.
2. Check it in Terminal: `node -v` should print `v20.9` or newer.

### 5.2 Clone and run
```bash
git clone https://github.com/<your-github-username>/prowesstics-web.git
cd prowesstics-web
npm install
npm run dev
```
Open http://localhost:3000. The page reloads automatically when a file is saved. Stop the server with `Ctrl + C`.

### 5.3 Production check
```bash
npm run build
npm start
```

## 6. Editing content

Every word, number and list on the homepage lives in **`content/site.ts`**. Change the text between the quotes and save.

| To change | Edit in `content/site.ts` |
|---|---|
| Hero headline, subline, badge | `hero` |
| Track record numbers | `stats` |
| Industries (name, line, use cases) | `industries` |
| Service cards (body, bullets, outcome, tech tags) | `services` |
| Client commitments | `commitments` |
| Product cards and KPIs | `products` |
| Engagement steps | `steps` |
| Client logos | `clients` (add the PNG to `public/logos/` first) |
| Before-and-after results | `results` |
| Technology marquee | `techRow1`, `techRow2` (add the PNG to `public/tech/` first) |
| Testimonials | `testimonials` |
| Contact form interests | `interests` |
| Footer links | `footerCols` |

House style for all copy: no em dashes, no references to Singapore, outcome-led sentences, numbers backed by a client result or collateral.

## 7. Images and media

### 7.1 Image slot register
Every image position has a slot ID. `components/ImageSlot.tsx` shows the real image when `src` is set in `content/images.ts`, otherwise a labelled placeholder.

| Slot | Position | Format | Delivered size |
|---|---|---|---|
| IMG-01 | Hero background | JPG | 3344 x 1882 |
| IMG-02 to IMG-09 | Service card visuals: product cut-out with data callouts | Transparent PNG | 1200 x 640 |
| IMG-10 to IMG-14 | Product cards (card version plus `-detail.jpg` opened on click) | JPG | 2400 x 1340 |
| IMG-15 | Contact section (card plus detail) | JPG | 2400 x 1340 |
| IMG-16 | Optional photographic "10" badge | Transparent PNG | 2400 x 2400 |
| IND-01 to IND-09 | Industries grid with sector-specific detections (opens full size on click) | JPG | 2400 x 1340 |

### 7.2 Adding or replacing an image
1. Save the file in `public/images/` using the slot name, for example `IND-05.jpg`.
2. In `content/images.ts`, set `src` for that slot, for example `src: "/images/IND-05.jpg"`.
3. Run `npm run dev` and check the image at desktop and phone width.

### 7.3 Image standards
- Photorealistic, true-to-life colour, no visible AI artefacts (extra objects, warped hands, blurred faces).
- Technical visuals must show what the platform does: detection boxes with confidence, wireframes, measurements, heat maps, pipeline flows and live readouts. Overlay text is drawn in code so every label stays exact.
- Every illustrative data overlay carries the note "Illustrative visualisation".
- Product images come in two versions: a card version with three or four large callouts and a `-detail.jpg` with the full technical overlay that opens in the lightbox.
- Overlays are generated by the scripts in `tools/visuals/`; rerun them after replacing a source photo.
- Prompts for each slot are recorded in `IMAGE_PROMPTS.md`.

### 7.4 Company film
Place the video in `public/video/` and set `companyFilm` in `content/images.ts`, for example `"/video/company-film.mp4"`.

## 8. Design system

| Token | Value | Use |
|---|---|---|
| `--night` | `#061330` | Hero, dark bands, footer |
| `--navy` | `#0A1F44` | Primary brand navy |
| `--cyan` | `#2EC5DC` | Signal colour: links, buttons, data highlights |
| `--cyan-2` | `#1A9FD8` | Secondary cyan on light backgrounds |
| `--gold` | `#E8B452` | Highlights, rules, accents |
| `--ink` | `#0B1B3A` | Body text on light backgrounds |
| `--muted` | `#5A6B85` | Secondary text |
| `--mist` | `#F4F8FC` | Light section background |

- Typeface: Avenir Next or Avenir where available, then Nunito Sans.
- Layout: 1240 px maximum width, 24 px side gutter that respects device safe areas.
- Breakpoints: 1100, 1000, 960, 900, 640, 560 and 480 px. No horizontal scrolling at 390 px.
- Motion: marquees and the hero wave stop when the visitor has reduced motion enabled.

## 9. SEO and structured data

- Title, description, keywords, canonical URL, Open Graph and Twitter card in `app/layout.tsx`.
- `Organization` and `SoftwareApplication` (one per product) JSON-LD in `app/page.tsx`.
- `/sitemap.xml` and `/robots.txt` generated by `app/sitemap.ts` and `app/robots.ts`.
- Every image has descriptive `alt` text in `content/images.ts`.
- After go-live: verify the domain in Google Search Console and submit `https://www.prowesstics.com/sitemap.xml`.

## 10. Accessibility and performance

- Semantic landmarks (`header`, `main`, `section`, `footer`), labelled form controls, visible keyboard focus.
- Carousel controls and the video dialog are keyboard operable; the dialog closes with Escape.
- Images are served as AVIF or WebP at the size each screen needs.
- The font is self-hosted, so no third-party font request is made.

## 11. Deployment

### 11.1 GitHub Pages (live)
The site is published to **https://harish-e-g.github.io/prowesstics-web/** by `.github/workflows/deploy-pages.yml`.
1. One-time: **Settings > Pages > Build and deployment > Source: GitHub Actions**.
2. Every push to `main` builds a static copy and publishes it in about two minutes. Progress shows under the **Actions** tab.
3. Custom domain: enter it under **Settings > Pages > Custom domain**, add the DNS records GitHub shows at the registrar, then set `BASE_PATH: ""` in the workflow so the site is served from the domain root.
4. The repository must stay public on a free GitHub plan for Pages to work.

### 11.2 Vercel or Railway (alternative)
Import the repository at https://vercel.com or https://railway.app and keep the detected Next.js settings. These hosts run the full Next.js server with automatic image resizing and work with a private repository. Vercel's free plan is for non-commercial use, so a company site needs Vercel Pro.

### 11.3 Static copy
`npm run preview:static` writes a plain static copy to `out/`. It is used for quick previews and for hosts that serve static files only. Images are served as built in this mode. Set `NEXT_PUBLIC_BASE_PATH` when the site lives in a sub-folder.

## 12. Contact form and lead capture

The form in `components/Contact.tsx` validates name and work email and confirms on the page. It does not send data anywhere yet. Connect one of:

| Option | How |
|---|---|
| Form service (fastest) | Formspree or Basin: post the form data to their endpoint inside `handleSubmit` |
| CRM | HubSpot or Zoho forms API called from `handleSubmit` |
| Own email | Add `app/api/contact/route.ts` and send through Resend or SMTP; keep keys in Vercel environment variables, never in the code |

## 13. Scripts reference

| Command | What it does |
|---|---|
| `npm run dev` | Local development server on port 3000 |
| `npm run build` | Production build with type checking |
| `npm start` | Serves the production build |
| `npm run lint` | Next.js lint checks |
| `npm run preview:static` | Static export to `out/` |

## 14. Quality checklist before every release

- [ ] `npm run build` passes with no errors
- [ ] `npm audit` reports 0 vulnerabilities
- [ ] Page checked at 1440 px, 768 px and 390 px with no horizontal scroll
- [ ] No console errors in the browser
- [ ] All images load; no placeholders left unintentionally
- [ ] No em dashes and no Singapore references in copy
- [ ] Every new number traceable to a client result or collateral
- [ ] `CHANGELOG.md` updated

## 15. Roadmap

- Product detail pages for ProVision AI, ProChurn AI, DEO Suite, ProSight AI and ProTrace AI
- Industry pages and case study library
- Insights and blog section managed through a CMS
- Contact form connected to the CRM
- Analytics and Search Console set up

## 16. Ownership, licence and contact

Copyright © 2026 IT Services Pvt. Ltd. All rights reserved. This repository is proprietary; see [LICENSE](LICENSE).

Client names, logos and testimonials appear with reference to delivered engagements. Third-party technology logos belong to their respective owners and are shown to indicate platform experience only.

- Sales: sales@prowesstics.com
- Website: https://www.prowesstics.com
