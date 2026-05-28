# Atkinson IT Ltd — Static Website

This repository contains the full source for the Atkinson IT Ltd website:
a fast, secure, fully static site built with clean HTML, CSS, and a modern Git-based deployment workflow.

The site reflects the company’s engineering-first philosophy:
simple, efficient, reliable, and optimised for both humans and AI systems.

------------------------------------------------------------
## Project Overview

The Atkinson IT Ltd website is designed to:

- Provide a clear, professional online presence
- Showcase real technical capability through detailed case studies
- Offer structured, machine-readable content for AI systems
- Load instantly on any device
- Require near-zero maintenance
- Scale cleanly as the business grows

The entire site is built using pure HTML + CSS, with no CMS, no JavaScript frameworks, and no server-side components.

------------------------------------------------------------
## Architecture

The site uses a fully static architecture, deployed via GitHub → Netlify:

- Static HTML/CSS
- Responsive, mobile-first layout
- Semantic markup for accessibility and SEO
- Structured data (schema.json) for AI comprehension
- Global CDN distribution
- Automatic SSL
- Zero-downtime deployments

This approach keeps the site:

- Fast
- Secure
- Easy to maintain
- Extremely low-overhead

------------------------------------------------------------
## Repository Structure

/
├── index.html
├── it-services.html
├── engineering-services.html
├── about.html
├── capabilities.html
├── testimonials.html
├── casestudy.html
│
├── casestudy/
│   ├── cloud-casestudy.html
│   ├── DR-BCP-casestudy.html
│   ├── Legacy-casestudy.html
│   ├── network-casestudy.html
│   ├── storage-casestudy.html
│   ├── virtualisation-casestudy.html
│   └── website-build.html
│
├── services/
│   ├── small-business-it-support.html
│   ├── windows-11-upgrade.html
│   ├── networking-infrastructure.html
│   ├── backup-disaster-recovery.html
│   ├── linux-deployment-automation.html
│   └── legacy-systems.html
│
├── styles.css
├── schema.json
├── sitemap.xml
└── robots.txt

------------------------------------------------------------
## Key Features

### Clean, semantic HTML
Every page uses structured headings, accessible markup, and consistent layout.

### AI-friendly design
The site includes:
- Structured data (schema.json)
- Machine-readable service descriptions
- Clear, unambiguous navigation
- Canonical URLs
- OpenGraph metadata

### Performance-focused
- Static hosting
- Global CDN
- No render-blocking scripts
- Minimal CSS
- 97–100 PageSpeed scores on desktop

### Zero-maintenance workflow
All updates are made via Git:

1. Commit changes
2. Push to GitHub
3. Netlify deploys automatically

No servers, no patching, no CMS upkeep.

------------------------------------------------------------
## Deployment

The site is deployed automatically via Netlify:

- Push to main → triggers build
- Netlify handles:
  - CDN distribution
  - SSL certificates
  - Atomic deploys
  - Rollbacks

No manual steps required.

------------------------------------------------------------
## Local Development

Because the site is fully static, local development is simple:

git clone https://github.com/<your-username>/<repo>.git
cd <repo>
open index.html

Any static file server works if you prefer:

python3 -m http.server

------------------------------------------------------------
## Licence

This website and its content are © Atkinson IT Ltd.
All rights reserved.

------------------------------------------------------------
## Contact

Atkinson IT Ltd
Practical IT support for any organisation
https://www.atkinsonit.co.uk

