# Deploying the viewer to Cloudflare Pages

The site is **data-viewer separated**: `site/index.html` + `site/app.js` are a static viewer
that never changes with content; `scripts/build_data.py` turns the verified `data/*.yaml`
into `dist/data.json` and copies the viewer into `dist/`. To update the site you edit YAML
and push — nothing else.

## Model: Cloudflare builds on push (Pages Git integration)

```
edit data/*.yaml ─push─▶ GitHub ─▶ Cloudflare Pages
                                     └─ runs ./build.sh:
                                          1. pip install pyyaml
                                          2. validate.py   ← GATE: nonzero exit aborts deploy
                                          3. build_data.py → dist/
                                     └─ serves dist/ at your *.pages.dev domain
```

The site always reflects the latest **pushed** data, because every push rebuilds. Bad data
cannot deploy, because the build aborts if `validate.py` fails (verified: an invalid status
exits 1 and Pages treats a nonzero build as failed, keeping the last good deploy live).

### One-time Cloudflare Pages setup

Connect the GitHub repo in the Cloudflare dashboard (Workers & Pages → Create → Pages →
Connect to Git), then set:

| Setting | Value |
|---|---|
| Framework preset | None |
| Build command | `./build.sh` |
| Build output directory | `dist` |
| Root directory | `/` |
| Environment variable | `PYTHON_VERSION = 3.12` (so the image exposes python3.12) |

That's it. No `package.json`, no Node. The build runs Python only.

## What gates where — deliberate split

- **Cloudflare build (`build.sh`)** — runs `validate.py` with `--expire-days 100000`, so
  schema / bucket-legality / unsupported-`ga` errors block the deploy, but 180-day
  staleness does NOT (public data legitimately ages between edits; you don't want the live
  site to 500 because a cell turned 181 days old).
- **GitHub Actions (`.github/workflows/validate.yml`)** — the strict PR gate: full
  `validate.py` (180-day staleness ON), `check_quotes.py` (needs network — the verbatim-quote
  check), and `check_links.py`. This is where fabricated quotes and dead links are caught,
  before merge. Cloudflare never runs `check_quotes.py` (too slow / network-fragile for a
  Pages build), so **keep branch protection on `main` requiring the Actions check** — that
  is what actually guarantees quote integrity; the CF gate only guarantees schema validity.

## Local preview

```bash
uv run scripts/build_data.py           # -> dist/
cd dist && python3 -m http.server 8791  # serve (file:// blocks fetch, so a server is needed)
open http://localhost:8791/index.html
```

## Do not commit `dist/`

It's a build artifact (in `.gitignore`). CF and local previews regenerate it; a checked-in
copy would go stale and mislead.
