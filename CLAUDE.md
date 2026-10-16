# Prowesstics website: working rules for Claude Code

Claude Code reads this file automatically at the start of every session. It holds the
standing rules so no session depends on chat history.

## Owner and ways of working
- Owner: Harish E G (Head of Sales and Marketing, APAC and EMEA, Prowesstics).
- Commit and push every finished change without asking. Be professional in version control.
- When Harish asks for a correction, change only what he names. Leave everything else as is.
- Give step-by-step, plain-English explanations. Keep replies short.
- Never mention Singapore in Prowesstics-facing content.

## Git conventions
- Author: `Harish E G <harishesakkiyappan@gmail.com>`.
- Conventional commit subject (`feat(scope): ...`, `fix(scope): ...`, `docs: ...`) plus a body
  explaining what and why. End with:
  `Co-Authored-By: Claude <noreply@anthropic.com>`
- Add a `CHANGELOG.md` entry under `[Unreleased]` for every user-visible change.
- Never force-push to shared branches. Never rewrite someone else's commits.
- After pushing `main`, check the Pages deploy:
  `gh api repos/harish-e-g/prowesstics-web/actions/runs --jq '.workflow_runs[0] | {status,conclusion}'`
  If it failed for a GitHub-side reason, rerun the failed jobs.

## Stack (this repo)
- Next.js 15 App Router, React 19, TypeScript strict, static export.
- Build for Pages: `STATIC_EXPORT=1 NEXT_PUBLIC_BASE_PATH=/prowesstics-web npm run build`.
- Deploy: `.github/workflows/deploy-pages.yml` on push to `main`.
  Live preview: https://harish-e-g.github.io/prowesstics-web/
- All asset URLs go through `asset()` in `lib/image-loader.ts` (base path aware).
- Content lives in `content/site.ts`; sections in `components/Sections.tsx`.
- Generators: `tools/visuals` (image overlays), `tools/video` (film edits), `tools/tech-logos`.

## Design rules (non-negotiable)
- Palette: navy #0A1F44, deep navy #061330, secondary navy #102A5C, teal #5BB4BC,
  cyan #2EC5DC, blue-cyan #1A9FD8, gold #E8B452 (sparingly). Body text #111111.
- Font weight 500 maximum. No heavy or extra bold.
- No em dashes anywhere, in copy or code.
- Images are technical, data-driven visuals, labelled "Illustrative visualisation".
  Nothing that looks like an online hardware store.
- Desktop hero and stats bar must fit the first screen on any laptop (vh clamps from 961 px).
- Respect `prefers-reduced-motion`.

## Legacy PHP site (next phase)
- The live prowesstics.com is a 9-year-old PHP site. Plan: keep PHP and the database,
  rebuild the front end in place with this design system. Protect URLs (same URLs or 301s)
  to keep Google ranking.
- It will live in a separate PRIVATE repo. Branches: `main` (approved, team deploys live),
  `testing` (Claude delivers here), short work branches. Claude never pushes to `main`.
- First commit = live code as-is, tagged `legacy-baseline`.
- Never commit secrets, DB dumps, customer uploads or logs. Commit `config.example.php` only.
- Database changes ship as numbered SQL migration files.

## Keeping sessions from breaking
- Session state is in git, this file and `docs/HANDOVER.md`. Update HANDOVER.md at the end
  of any long task (use `/handover`).
- Big inputs (source zips, videos) go into the repo or a working folder, not into chat.
- Read large files in parts. Use subagents for wide searches so the main context stays small.
