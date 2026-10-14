# Security policy

## Reporting a vulnerability
Email **sales@prowesstics.com** with the subject "Security: prowesstics-web". Include the affected URL or file, steps to reproduce and the impact you observed. Please do not open a public issue for security problems.

We acknowledge reports within two business days and share a fix plan once the issue is confirmed.

## Supported versions
Only the current `main` branch, which is what runs on https://www.prowesstics.com, receives security fixes.

## Practices in this repository
- Dependencies pinned to exact versions; `npm audit` must report 0 vulnerabilities before release.
- No secrets in the code. API keys for forms or CRM go in Vercel environment variables.
- No third-party tracking or font requests are bundled by default.
