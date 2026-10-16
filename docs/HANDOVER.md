# Handover: current state

Updated: 2026-10-16

## Done and live
- Next.js site live on GitHub Pages (latest: 7bc70f5, 78-logo tech stack).
- Services and Solutions menus, /services/ page with chapters, animated 10-year badge,
  200+ team stat, universal 2-minute factory film, laptop-fit hero, two-row industry chips.

## In progress
- Legacy PHP site takeover. Agreed with Harish: private shared repo, `testing` branch for
  handover, his team tests and deploys `main` live.
- Waiting on from the tech team: full source zip (secrets removed), DB schema only,
  hosting details (provider, PHP and MySQL versions, cPanel or not), `.htaccess`,
  `sitemap.xml`, Search Console top-pages export, admin feature list, their report.
- Their admin creates the private repo, adds members, protects `main`, grants
  the harish-e-g GitHub connection access.

## Next steps
1. Commit the PHP code as-is and tag `legacy-baseline`.
2. Audit: structure, security, PHP version, plain-English health report.
3. URL inventory from sitemap and Search Console; redirect map if anything moves.
4. Rebuild templates page by page into `testing`, one pull request each.
