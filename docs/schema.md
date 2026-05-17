# Tool record schema (minimum)

One tool per file: `data/tools/<slug>.yaml`. Slug = lowercase kebab-case derived from product name (e.g. `example-product`).

## Required fields

| Field | Type | Format / constraints | Description |
|-------|------|----------------------|-------------|
| `name` | string | 1–120 chars | Display name as shown on the official site. |
| `website` | string | HTTPS URL | Official product homepage (not affiliate). |
| `category` | object | — | Primary classification. |
| `category.l1` | string | L1 slug from taxonomy | Must match [taxonomy](taxonomy.md). |
| `category.l2` | string | L2 slug under that L1 | Must be valid pair for the L1. |
| `discount` | object | — | What the student/education offer is. |
| `discount.summary` | string | 1–500 chars | Plain-language benefit (e.g. “50% off Pro for 12 months”). |
| `discount.details` | string | optional | Eligibility nuances, duration, plan names. |
| `how_to_apply` | string | Markdown allowed, plain preferred | Steps to claim (portal, SheerID, .edu email, etc.). |
| `regional_restrictions` | string or array | ISO 3166-1 alpha-2 if listing countries | `global`, `unknown`, or list like `[US, CA, GB]` plus free-text notes. |
| `source_url` | string | HTTPS URL | Official page documenting the offer (pricing/education/students). |
| `verified_at` | string | `YYYY-MM-DD` (ISO 8601 date) | Date offer was confirmed on `source_url`. |
| `status` | enum | see below | Lifecycle of the listing. |

### `status` enum

| Value | Meaning |
|-------|---------|
| `active` | Offer verified on official source; expected to work. |
| `unverified` | Added by contributor; not yet checked by a maintainer. |
| `deprecated` | Product or program discontinued; keep for history. |
| `expired` | Offer ended but product may still exist. |
| `reported` | Community report that offer may be broken; needs re-check. |

## Recommended optional fields (maintainers)

| Field | Type | Description |
|-------|------|-------------|
| `slug` | string | Filename without `.yaml`; must match file name if present. |
| `about` | string | 1–200 chars: what the product does (for students browsing—not the discount). |
| `eligibility` | string | Who qualifies (enrolled student, faculty, alumni, age, institution type). |
| `proof_required` | string | e.g. SheerID, .edu email, ISIC, enrollment letter. |
| `offer_type` | enum | `percent_off`, `fixed_price`, `free_tier`, `credits`, `extended_trial`, `other` |
| `tags` | array of strings | Secondary capabilities; not alternate L1s. |
| `last_checked_by` | string | GitHub handle or `community` |
| `last_checked_at` | string | ISO date |
| `expires_at` | string | ISO date if offer has a published end date |
| `related_tools` | array of strings | Slugs of other records in this repo |
| `notes` | string | Maintainer-only context (not marketing copy) |
| `issues_url` | string | Link to open GitHub discussion/issue about this entry |

## Validation rules

- All URLs must use `https://`.
- `verified_at` ≤ today (UTC) at time of PR.
- `category.l1` + `category.l2` must exist in taxonomy.
- `status: active` requires `source_url` reachable and offer language still matches `discount.summary`.
- Do not commit API keys, referral codes tied to individuals, or affiliate-only links as `source_url`.

## Example (placeholders only)

```yaml
# data/tools/example-product.yaml

name: Example Product
website: https://example.com
slug: example-product

category:
  l1: writing-text
  l2: general-writing

discount:
  summary: Example discount summary (e.g. 40% off annual plan).
  details: >
    Optional details—plan name, billing period, stacking rules,
    or limits copied from the official page.

how_to_apply: |
  1. Go to the official education page (see source_url).
  2. Sign in with an account using your institutional email.
  3. Complete verification if prompted.
  4. Select the discounted plan at checkout.

regional_restrictions:
  countries: [US, CA]
  notes: Offer page states availability may vary outside North America.

source_url: https://example.com/pricing/education
verified_at: 2026-05-01
status: active

# --- optional ---
eligibility: Enrolled students at accredited institutions; faculty may differ—check source.
proof_required: .edu email or third-party student verification (see how_to_apply).
offer_type: percent_off
tags:
  - grammar-style
last_checked_by: your-github-handle
last_checked_at: 2026-05-01
notes: Replace placeholders before merge; remove this comment block.
```
