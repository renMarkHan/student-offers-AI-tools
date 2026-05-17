# Contributing

Thanks for helping keep this catalog accurate. We treat each YAML file as a small, reviewable fact record—not marketing copy.

## Before you start

- **In scope:** AI-related products with a **documented** student or education offer on the vendor’s own site (pricing, `/education`, `/students`, help center, or GitHub Education Pack listing).
- **Out of scope:** Blog roundups, coupon aggregators, affiliate landing pages, or discounts you only saw in a screenshot/DM.
- **One tool per PR:** Add or update a single `data/tools/<slug>.yaml` per pull request so reviewers can re-check one `source_url` end to end.

Questions about taxonomy or a product that does not fit? Open an issue first.

## How to add a new tool

### 1. Check for duplicates

Search [`data/tools/`](data/tools/) and [open issues](https://github.com/search?q=repo%3AOWNER%2FREPO+tool) for the product name. If a file exists, **update** it instead of creating a second slug.

### 2. Pick a slug and category

- **Slug:** lowercase kebab-case, stable over time (e.g. `notion-education`, not `notion-50-off`).
- **Category:** exactly one `category.l1` + `category.l2` from [docs/taxonomy.md](docs/taxonomy.md). Do not invent new slugs in a drive-by PR—propose taxonomy changes in a separate issue.

### 3. Verify on an official page

Open the page you will cite as `source_url`. It should state (or clearly imply) the offer you summarize:

| Good `source_url` | Avoid |
|-------------------|--------|
| Vendor pricing / education / students / help article | Third-party “best student discounts” lists |
| `education.github.com/pack` for Pack benefits | Personal referral or `?ref=` affiliate URLs |
| Press release **only** if no pricing page exists—say so in `notes` | Paywalled content you cannot link |

Copy **facts**, not hype: plan names, percent off, duration, regions, verification method (SheerID, `.edu`, institutional license).

### 4. Create the YAML file

Create `data/tools/<slug>.yaml` following [docs/schema.md](docs/schema.md).

Minimum you must get right:

```yaml
name: Product Name          # As on the official site
website: https://...        # Product homepage (HTTPS)
slug: product-slug          # Must match filename

category:
  l1: coding-development    # From taxonomy
  l2: code-assistants

discount:
  summary: One line, matches what source_url says today.
  details: >                # Optional: eligibility, duration, plan SKU

how_to_apply: |
  Numbered steps from the official flow.

regional_restrictions:
  notes: Country/age/school-type limits if the page mentions them.

source_url: https://...     # The page you actually read
verified_at: 2026-05-17     # Date you confirmed (see below)
status: unverified          # New contributor PRs (see Status)
```

**New contributor PRs:** use `status: unverified` unless a maintainer asked you to set `active` after their review.

**Maintainers** may set `status: active` when they have confirmed `source_url` on the same day as `verified_at`.

Optional but helpful: `eligibility`, `proof_required`, `offer_type`, `related_tools`, `last_checked_by`, `last_checked_at`, `notes` (factual caveats only).

### 5. Open the pull request

Use the [PR template](.github/PULL_REQUEST_TEMPLATE.md). Title examples:

- `Add: Notion for Education`
- `Update: Cursor student discount`

## How to update `verified_at`

Offers change. When you re-read the official page:

1. **Open the existing file** in `data/tools/`—do not duplicate the product under a new slug.
2. **Re-fetch `source_url`** in a browser (or equivalent). If the URL moved, update `source_url` in the same PR and mention the redirect in the PR description.
3. **Align copy with the page:**
   - If the benefit changed → update `discount.summary` / `details` / `how_to_apply`.
   - If the offer ended → set `status: expired` (or `deprecated` if the product/program is gone) and explain in `notes` with the date if known.
   - If you cannot reach the page (404, login wall, bot block) → do **not** bump `verified_at` to today; set `status: reported` or leave a PR comment and open an issue.
4. **Set `verified_at`** to the **calendar date (UTC)** when you confirmed the page still supports your summary—format `YYYY-MM-DD` only, no time zone suffix.
5. **Optionally set** `last_checked_at` to the same date and `last_checked_by` to your GitHub handle (especially for drive-by fixes).

Rules of thumb:

| Situation | What to do |
|-----------|------------|
| Wording on official page changed | Update summary + `verified_at` |
| Only typo in our YAML, offer unchanged | Fix typo; **do not** change `verified_at` |
| Offer removed from official site | `status: expired`, note in `notes`, update `verified_at` to check date |
| Checkout fails but page still advertises offer | `status: reported`, describe evidence in PR |

Do not guess discount numbers. If the page says “discount at checkout” without a percent, say that in `summary`—do not invent `50%`.

## Pull request checklist

Your PR should satisfy everything in [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md). In short:

- [ ] **One tool file** changed (or one add + no unrelated edits)
- [ ] **`source_url`** is official and matches `discount.summary` / `how_to_apply`
- [ ] **`verified_at`** is `YYYY-MM-DD` and ≤ today (UTC)
- [ ] **`website`** is the product homepage (HTTPS)
- [ ] **`category.l1` / `category.l2`** exist in [taxonomy](docs/taxonomy.md)
- [ ] No affiliate links, personal referral codes, or scraped paywalled text
- [ ] Regional and eligibility limits documented when the vendor mentions them

## Status values

| Status | Use when |
|--------|----------|
| `active` | Official offer page checked; summary matches; maintainer or trusted review complete. |
| `unverified` | Reasonable PR; maintainer has not re-opened `source_url` yet. |
| `reported` | Evidence that checkout/verification fails or page is unreachable; needs re-check. |
| `expired` | Vendor ended the offer; keep the file for history. |
| `deprecated` | Product or education program shut down; point to replacement in `notes` if any. |

Prefer updating status over deleting files so issues and git history stay useful.

## Repository layout

```text
docs/taxonomy.md      # L1/L2 categories
docs/schema.md        # Field definitions and example
data/tools/*.yaml     # One file per product offer
.github/              # PR template, workflows (if any)
```

## Validation (optional locally)

If `scripts/validate.py` exists, run it before pushing. CI may check taxonomy slugs and required fields—fix reported errors in the same PR.

## Code of conduct

Be direct and kind in issues and reviews. We care about accurate citations, not volume.

<!-- Link CODE_OF_CONDUCT.md when added. -->
