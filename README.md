# Prowesstics Website (Next.js)

Production-ready homepage built with Next.js 15, React 19 and TypeScript. Every image position shows a labelled placeholder (IMG-01 to IMG-16 and IND-01 to IND-09) until you add the real file. The ChatGPT prompts for each slot are in IMAGE_PROMPTS.md.

---

## Step 1 · Install Node.js (one time)
1. Go to https://nodejs.org and download the **LTS** version for Mac.
2. Open the downloaded file and click through the installer.
3. Open the **Terminal** app and check it worked:
   ```
   node -v
   ```
   You should see a version number such as `v22.x`.

## Step 2 · Open the project in Terminal
1. Unzip `prowesstics-web.zip` (double-click it).
2. In Terminal, type `cd ` (with a space), drag the unzipped `prowesstics-web` folder into the Terminal window, and press Enter.

## Step 3 · Install and run
```
npm install
npm run dev
```
Open http://localhost:3000 in your browser. The site reloads automatically whenever you save a file.
Press `Ctrl + C` in Terminal to stop it.

---

## Step 4 · Add your images
1. Save each image into `public/images/` using its slot name, for example `public/images/IMG-01.jpg`.
2. Open `content/images.ts` and add the path to that slot:
   ```ts
   "IMG-01": { src: "/images/IMG-01.jpg", alt: "Prowesstics leadership team in a boardroom at dusk" },
   ```
3. Save. The placeholder is replaced instantly.

| Slot | Where it appears | Format |
|---|---|---|
| IMG-01 | Hero background (right half) | JPG, 3840 x 2160 |
| IMG-02 to IMG-09 | Service cards (bottom right) | Transparent PNG, 2048 x 2048 |
| IMG-10 to IMG-14 | Product cards | JPG, 3840 x 2160 or 3000 x 2000 |
| IMG-15 | Contact section | JPG, 3840 x 1680 |
| IND-01 to IND-09 | Industries grid (3 x 3) | JPG, 3200 x 2000 |
| IMG-16 | Optional photographic "10" badge (the coded 3D badge shows by default) | Transparent PNG, 2400 x 2400 |

Next.js automatically converts and resizes images for each screen, so 4K originals stay fast to load.

**Company film:** put the video in `public/video/` (create the folder), then in `content/images.ts` set:
```ts
export const companyFilm = "/video/company-film.mp4";
```

## Step 5 · Change text, numbers, logos or testimonials
Everything is in **`content/site.ts`**: hero copy, stats, industries, services, products, results, client logos, tech stack and testimonials. Edit the words between the quotes and save.

- **New client logo:** add the transparent PNG to `public/logos/`, then add a line to `clients`.
- **New tech logo:** add the PNG to `public/tech/`, then replace that entry's `mono` and `color` with `logo: "/tech/yourfile.png"`. Power BI, Microsoft Fabric, AWS Glue, Informatica, Pentaho, Yellowfin, Honeywell and Rockwell currently use coloured badges until official PNGs are added.

## Step 6 · Put it live (recommended: Vercel, free to start)
1. Create a free account at https://github.com and upload this folder as a new repository (GitHub Desktop makes this point-and-click).
2. Go to https://vercel.com, sign in with GitHub, click **Add New > Project**, pick the repository and click **Deploy**.
3. In Vercel, open **Settings > Domains** and add `prowesstics.com`. Vercel shows the DNS records to add at your domain registrar.
4. Every future change you push to GitHub goes live automatically.

## Step 7 · Receive form leads
The contact form validates and shows a confirmation, but does not send anywhere yet. Choose one:
- **Easiest:** a form service such as Formspree or Basin. Paste their endpoint into `components/Contact.tsx` inside `handleSubmit`.
- **CRM:** HubSpot or Zoho forms API, called from `handleSubmit`.
- **Own email:** add a Next.js route handler at `app/api/contact/route.ts` that sends via Resend or SMTP.

## Step 8 · SEO checklist after go-live
- Add the site to **Google Search Console** and submit `https://www.prowesstics.com/sitemap.xml` (generated automatically).
- `robots.txt`, page titles, descriptions, Open Graph tags and Organization structured data are already in place (`app/layout.tsx`, `app/page.tsx`).

---

## Project map
```
app/            layout (fonts, SEO), page (section order), sitemap, robots, favicon
components/     one file per section (Hero, Sections, Testimonials, Contact, Footer)
content/        site.ts (all copy and data), images.ts (image slots)
public/         brand/, logos/ (clients), tech/ (stack), images/ (your photos)
```

Commands: `npm run dev` (preview) · `npm run build` (production check) · `npm start` (run the production build).
