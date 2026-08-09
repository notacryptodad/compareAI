# Generative Engine Optimization (GEO) readiness of vendor docs

## Observation

AI search tools (Perplexity, Google AI Overview, ChatGPT search, Gemini) fetch vendor
documentation the same way a plain HTTP client does. If a page requires JavaScript to
render its body content, these tools see an empty nav shell — the vendor effectively
does not exist in AI-generated answers.

This is the generative-engine equivalent of failing SEO: being invisible not to Google's
crawler but to the AI layer that synthesises buying recommendations.

## Evidence from this project

| Provider | Doc host | Rendering | AI-discoverable? |
|----------|----------|-----------|-----------------|
| AWS | docs.aws.amazon.com | Server-rendered (mostly) | Yes |
| Azure | learn.microsoft.com | Server-rendered | Yes |
| GCP | docs.cloud.google.com | Server-rendered | Yes |
| BytePlus | docs.byteplus.com | Client-side SPA | No |
| Alibaba | help.aliyun.com (sub-pages) | Client-side SPA | No |

We proved this directly: `check_quotes.py` gets ~3.3 KB of nav chrome from BytePlus pages
(vs 12-50 KB of prose when rendered with headless Chrome). The same pages return HTTP 200
— they're reachable but unreadable. An AI search tool querying "BytePlus managed agents"
would find nothing meaningful.

## Impact on buying decisions

When an enterprise evaluator asks an AI assistant "compare cloud agent platforms," the
answer will systematically over-represent AWS/Azure/GCP and under-represent BytePlus and
Alibaba Cloud — not because those products are weaker, but because their documentation
is architecturally invisible to the answering system.

This creates a self-reinforcing disadvantage:
1. AI tools can't read the docs → product doesn't appear in comparisons
2. Product doesn't appear → fewer developers evaluate it
3. Fewer developers → smaller community signal → AI tools rank it lower

## Practical implications for this project

- **Research methodology**: always try Playwright before concluding a vendor "doesn't
  document" a capability. We went from 14 unknowns to 2 for BytePlus once we rendered
  the pages properly.
- **Fairness rule**: the comparison must not penalise providers for thin *crawlable* docs
  when rich *rendered* docs exist behind the JS wall.
- **Refresh skill**: the Playwright auto-fallback (Step 2 in Phase 3) exists specifically
  because of this gap. Known JS-rendered domains skip straight to headless Chrome.

## Recommendations for affected vendors

1. **Server-side render** (SSR) the doc content, even if the interactive shell is a SPA.
   Next.js, Nuxt, and Astro all support this with minimal architectural change.
2. **Serve `<meta>` and `<article>` content** in the initial HTML response so that
   HTTP-only clients (including AI search crawlers) get the prose.
3. **Test with `curl -s URL | wc -c`** — if the text content is < 5 KB, AI tools
   can't read it.
4. Ship a **sitemap with pre-rendered snapshots** or use dynamic rendering for known
   bot user-agents (Perplexity, GPTBot, Google-Extended).

## Status

Written 2026-08-09 based on the `/refresh all unknown entry` sweep that demonstrated the
gap across 51+ cells. This is an insight document, not a data cell — it explains WHY some
providers have more unknowns and what it means commercially.
