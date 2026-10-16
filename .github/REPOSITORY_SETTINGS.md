# GitHub repository settings

Fill these in on GitHub once the repository exists. Each value is ready to paste.

## About (gear icon on the repository home page)
| Field | Value |
|---|---|
| Description | Official corporate website of IT Services: data engineering, AI, computer vision and factory automation. Next.js 15, React 19, TypeScript. |
| Website | https://www.prowesstics.com |
| Topics | `nextjs` `react` `typescript` `corporate-website` `data-engineering` `artificial-intelligence` `computer-vision` `factory-automation` `machine-learning` `business-intelligence` |
| Include in home page | Releases: on. Packages: off. Deployments: on. |

## General
| Setting | Value |
|---|---|
| Repository name | `prowesstics-web` |
| Visibility | Private |
| Default branch | `main` |
| Features | Issues on. Wiki off. Projects on. Discussions off. |
| Pull requests | Allow squash merging only. Automatically delete head branches: on. |

## Branch protection for `main` (Settings > Branches > Add rule)
- Require a pull request before merging, with 1 approval
- Require status checks to pass (Vercel)
- Require conversation resolution before merging
- Do not allow force pushes or deletions

## Labels
| Label | Colour | Use |
|---|---|---|
| `bug` | `#D73A4A` | Something is broken |
| `content` | `#2EC5DC` | Copy, numbers, logos, testimonials |
| `images` | `#E8B452` | New or replaced images |
| `feature` | `#0A1F44` | New sections or pages |
| `seo` | `#14965E` | Search and structured data |

## First release
Tag `v1.0.0` on `main` with the notes from `CHANGELOG.md` section 1.0.0.
