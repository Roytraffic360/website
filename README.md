# traffik360.com

Source for the Traffik360 website, English and Arabic.

## How it works
- `site/` is the website exactly as published. Plain HTML, CSS and a little JavaScript.
- `tools/build.py` generates every page in `site/` from one table of English and Arabic text (`STR`).
  To change wording: edit `STR`, run `python3 tools/build.py`, commit both.
- `site/_redirects` sends old WordPress URLs to the new pages. `site/_headers` sets security headers.

## Cloudflare Pages settings
- Production branch: `main`
- Framework preset: None
- Build command: (leave empty)
- Build output directory: `site`

## Before launch
- Replace every `[placeholder]` (search the repo for `[`).
- Client names appear only with written approval.
- Arabic copy is a draft: native copywriter review required.
- "600+ orders a year" is derived from Zoho CRM sales orders 2023 to 2025: confirm against Zoho Books.
- Paste the Zoho Forms embed into `brief()` in `tools/build.py` (marked `ZOHO_FORM_EMBED`).
- Privacy policy text needs legal review.
- Colours and type are a proposal until the brand files are confirmed (tokens at the top of `site/assets/site.css`).
