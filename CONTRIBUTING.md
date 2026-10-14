# Contributing

This is a private repository for the Prowesstics corporate website. These rules keep every change reviewable and the live site stable.

## Branches
| Branch | Purpose |
|---|---|
| `main` | Production. Every push deploys to the live site. |
| `feature/<short-name>` | New sections, pages or components |
| `content/<short-name>` | Copy, numbers, logos or testimonials |
| `fix/<short-name>` | Bug fixes |
| `images/<batch>` | New or replaced images |

## Workflow
1. Create a branch from `main`.
2. Make the change and run `npm run build` locally.
3. Open a pull request using the template. Vercel posts a preview URL on the pull request.
4. Review the preview at desktop, tablet and phone width.
5. Merge into `main` once approved. The change goes live automatically.

## Commit messages
Use the imperative mood and say what changed, for example:
- `Add ProTrace AI product card`
- `Replace IND-05 retail image with sharp-focus version`
- `Fix testimonial carousel overflow on 390 px screens`

## Content rules
- No em dashes anywhere in copy or code.
- Never reference Singapore.
- Every number must trace back to a client result, case study or collateral.
- Client names and logos only for delivered engagements.
- Images must look photographic, with no AI artefacts. Technical overlays are drawn in code and labelled "Illustrative visualisation".

## Before requesting review
- [ ] `npm run build` passes
- [ ] `npm audit` shows 0 vulnerabilities
- [ ] Checked at 1440, 768 and 390 px with no horizontal scroll
- [ ] No console errors
- [ ] `CHANGELOG.md` updated under "Unreleased"
