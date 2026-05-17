# Student AI Offers

A **community-maintained directory** of student and education discounts on AI-related tools. Each listing links to an official offer page and shows when it was last checked.

**Disclaimer:** Informational only—not legal, tax, or financial advice. We are not affiliated with vendors. Offers and eligibility change; **always confirm on the vendor’s site** before you sign up or pay.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## For students: how to find a tool

You do **not** need to clone the repo. Everything lives in plain YAML on GitHub.

### 1. Pick a category below

Scroll to **[Browse by category](#browse-by-category)** and open the section that matches what you need (coding, writing, video, cloud credits, etc.). Each line links to one tool file.

### 2. Open the tool file on GitHub

Example: [Cursor](data/tools/cursor.yaml) → read these fields first:

| Field | What it tells you |
|-------|-------------------|
| `discount.summary` | The deal in one sentence |
| `how_to_apply` | Steps to claim it |
| `source_url` | **Official page**—open this and verify price/terms yourself |
| `verified_at` | When a maintainer last matched the listing to that page |
| `status` | `active` = reviewed; `unverified` = added but not yet double-checked |
| `eligibility` / `regional_restrictions` | Who qualifies and where |

### 3. Or browse / search the folder

- **All tools (flat list):** [`data/tools/`](data/tools/) on GitHub  
- **GitHub search** (from the repo page, press `/` then search, or use the search box with `path:data/tools`):
  - By name: `cursor path:data/tools`
  - By category slug in files: `category.l1: coding-development`

**Catalog size (May 2026):** 68 `active` · 33 `unverified` · 1 `expired` — [102 listings total](data/tools/).

---

## Quick picks

| I want to… | Start here |
|------------|------------|
| Code with AI / get cloud dev tools | [GitHub Student Developer Pack](data/tools/github-student-developer-pack.yaml) · [Cursor](data/tools/cursor.yaml) · [GitHub Copilot (Student)](data/tools/github-copilot-student.yaml) · [Azure for Students](data/tools/microsoft-azure-students.yaml) |
| Write, study, or research | [Notion for Education](data/tools/notion-education.yaml) · [Perplexity Pro](data/tools/perplexity.yaml) · [Consensus](data/tools/consensus.yaml) · [Wolfram\|Alpha Pro (Students)](data/tools/wolfram-alpha-pro-students.yaml) |
| Slides, whiteboards, design | [Figma for Education](data/tools/figma-education.yaml) · [Canva for Education](data/tools/canva-education.yaml) · [Miro Education](data/tools/miro-education.yaml) |
| Video / audio | [Adobe Creative Cloud Pro](data/tools/adobe-creative-cloud-pro.yaml) · [Descript](data/tools/descript.yaml) · [Loom](data/tools/loom.yaml) · [ElevenLabs (Students)](data/tools/elevenlabs.yaml) |
| Law school (US) | [Westlaw (Law School)](data/tools/westlaw-law-school.yaml) · [Lexis+ AI (Law Schools)](data/tools/lexis-plus-ai-law-schools.yaml) · [Harvey Academy](data/tools/harvey-academy.yaml) |

More categories in the index below.

---

## Browse by category

Each tool is filed under **one** primary category ([full taxonomy](docs/taxonomy.md)). Expand a section to see **`active`** listings only.

### Category index

| Category | Slug | Active |
|----------|------|--------|
| [Writing & text](#writing-text) | `writing-text` | 3 |
| [Coding & development](#coding--development) | `coding-development` | 7 |
| [Research & academia](#research--academia) | `research-academia` | 2 |
| [Video](#video) | `video` | 4 |
| [Audio & voice](#audio--voice) | `audio-voice` | 2 |
| [Image & design](#image--design) | `image-design` | 5 |
| [Presentations & documents](#presentations--documents) | `presentation-documents` | 4 |
| [Learning & education](#learning--education) | `learning-education` | 5 |
| [Data & analytics](#data--analytics) | `data-analytics` | 5 |
| [Productivity & notes](#productivity--notes) | `productivity-notes` | 4 |
| [Communication & meetings](#communication--meetings) | `communication-meetings` | 4 |
| [Translation & language](#translation--language) | `translation-language` | 4 |
| [Legal](#legal) | `legal` | 5 |
| [Cloud & API credits](#cloud--api-credits) | `cloud-api-credits` | 7 |
| [Platforms & bundles](#platforms--bundles) | `platforms-bundles` | 7 |

### Writing & text

`writing-text` · 3 active

<details>
<summary>Show tools</summary>

- [ChatGPT Edu](data/tools/chatgpt-edu.yaml) — Campus institutional plan; not individual student checkout
- [Perplexity Pro](data/tools/perplexity.yaml) — 50% off for students and educators
- [Writesonic](data/tools/writesonic.yaml) — Up to 30% off for eligible students

</details>

### Coding & development

`coding-development` · 7 active

<details>
<summary>Show tools</summary>

- [Appwrite Education](data/tools/appwrite-education.yaml) — Free Education plan via GitHub Student Pack
- [Cursor](data/tools/cursor.yaml) — One free year of Cursor Pro (.edu + SheerID)
- [Educative](data/tools/educative.yaml) — 6 months free + 30% off via GitHub Pack
- [GitHub Codespaces](data/tools/github-codespaces.yaml) — Pro-level Codespaces via GitHub Pack
- [OpenAI Codex (Students)](data/tools/openai-codex-students.yaml) — $100 Codex credits (US/Canada students)
- [Replit](data/tools/replit.yaml) — 50% off Core with .edu email
- [Windsurf](data/tools/windsurf.yaml) — Over 50% off Pro with school .edu email

</details>

### Research & academia

`research-academia` · 2 active

<details>
<summary>Show tools</summary>

- [Consensus](data/tools/consensus.yaml) — 40% off Premium for students/faculty
- [Wolfram|Alpha Pro (Students)](data/tools/wolfram-alpha-pro-students.yaml) — Student Pro from $5/mo (annual billing)

</details>

### Video

`video` · 4 active

<details>
<summary>Show tools</summary>

- [Adobe Creative Cloud Pro](data/tools/adobe-creative-cloud-pro.yaml) — 69% off first year (US pricing on official page)
- [Descript](data/tools/descript.yaml) — Education plan from $8/editor/mo (annual)
- [Loom](data/tools/loom.yaml) — Up to 50% off (75% for classroom use)
- [Runway](data/tools/runway.yaml) — 25% off paid plans (SheerID)

</details>

### Audio & voice

`audio-voice` · 2 active

<details>
<summary>Show tools</summary>

- [ElevenLabs (Students)](data/tools/elevenlabs.yaml) — Expanded free access; ElevenReader Ultra via separate page
- [Murf AI](data/tools/murf-ai.yaml) — 20% off after email verification

</details>

### Image & design

`image-design` · 5 active

<details>
<summary>Show tools</summary>

- [Autodesk Education](data/tools/autodesk-education.yaml) — Free 1-year licenses for eligible students
- [Canva for Education](data/tools/canva-education.yaml) — Free for K–12 (teacher-invited students)
- [Figma for Education](data/tools/figma-education.yaml) — Free Education plan (K–12 / higher ed)
- [Icons8 (GitHub Student Pack)](data/tools/icons8-student-pack.yaml) — 3 months free via Pack
- [IconScout (GitHub Student Pack)](data/tools/iconscout-student-pack.yaml) — 60 premium icons/month for 1 year via Pack

</details>

### Presentations & documents

`presentation-documents` · 4 active

<details>
<summary>Show tools</summary>

- [Beautiful.ai Education](data/tools/beautiful-ai-education.yaml) — Free annual Pro for .edu students
- [Miro Education](data/tools/miro-education.yaml) — Free Education plan; limited Miro AI
- [SlideCoach](data/tools/slidecoach.yaml) — 2,000 credits via GitHub Pack
- [Visme (GitHub Student Pack)](data/tools/visme-student-pack.yaml) — 3 months Starter via Pack

</details>

### Learning & education

`learning-education` · 5 active

<details>
<summary>Show tools</summary>

- [Coursera for Campus](data/tools/coursera-campus.yaml) — Institutional licensing (not individual SKU)
- [Duolingo for Schools](data/tools/duolingo-for-schools.yaml) — Free classroom layer for teachers
- [Edpuzzle](data/tools/edpuzzle.yaml) — Free Basic for teachers/students
- [Khanmigo](data/tools/khanmigo.yaml) — Free for teachers; paid for learners
- [Quizlet for Schools](data/tools/quizlet-for-schools.yaml) — School-wide discounted Plus

</details>

### Data & analytics

`data-analytics` · 5 active

<details>
<summary>Show tools</summary>

- [Camber](data/tools/camber.yaml) — Free student plan via GitHub Pack
- [CARTO (GitHub Student Pack)](data/tools/carto-student-pack.yaml) — 2-year upgrade via Pack
- [DataCamp (Student Premium)](data/tools/datacamp-student.yaml) — 3 months free via GitHub Pack
- [Deepnote](data/tools/deepnote.yaml) — Free Team plan via GitHub Pack
- [PopSQL (GitHub Student Pack)](data/tools/popsql-student-pack.yaml) — Free Premium while a student (Pack)

</details>

### Productivity & notes

`productivity-notes` · 4 active

<details>
<summary>Show tools</summary>

- [Microsoft 365 (College Students)](data/tools/microsoft-365-college-students.yaml) — 12 months Microsoft 365 Premium free (eligible new students)
- [Notion for Education](data/tools/notion-education.yaml) — Free Plus for WHED-listed school email
- [Notion (GitHub Student Pack)](data/tools/notion-student-pack.yaml) — Education plan + extra AI via Pack
- [Obsidian (Education Discount)](data/tools/obsidian-education.yaml) — 40% off Sync and Publish

</details>

### Communication & meetings

`communication-meetings` · 4 active

<details>
<summary>Show tools</summary>

- [Microsoft 365 Copilot in Education](data/tools/microsoft-copilot-education.yaml) — Copilot Chat with school M365 A1/A3/A5
- [Otter.ai](data/tools/otter-ai.yaml) — 20% off Pro for .edu students/teachers
- [Slack for Education](data/tools/slack-education.yaml) — 85% off for qualifying institutions
- [Zoom Workplace for Education](data/tools/zoom-workplace-education.yaml) — Institutional plans via sales

</details>

### Translation & language

`translation-language` · 4 active

<details>
<summary>Show tools</summary>

- [Grammarly for Education](data/tools/grammarly-education.yaml) — Institution-wide licenses
- [QuillBot Premium](data/tools/quillbot.yaml) — Student pricing at checkout
- [Reverso Premium (Students & Teachers)](data/tools/reverso-premium-education.yaml) — Promo code via official pricing page
- [Wordtune](data/tools/wordtune.yaml) — 30% academic discount (application form)

</details>

### Legal

`legal` · 5 active

<details>
<summary>Show tools</summary>

- [CoCounsel (Law School)](data/tools/cocounsel-law-school.yaml) — Via participating law schools
- [Harvey Academy](data/tools/harvey-academy.yaml) — Free courses and certifications
- [Harvey (Law School Alliance)](data/tools/harvey-law-school-program.yaml) — Platform access at partner schools
- [Lexis+ AI (Law Schools)](data/tools/lexis-plus-ai-law-schools.yaml) — Law-school educational ID (US)
- [Westlaw (Law School)](data/tools/westlaw-law-school.yaml) — Included with school subscription

</details>

### Cloud & API credits

`cloud-api-credits` · 7 active

<details>
<summary>Show tools</summary>

- [AWS Educate](data/tools/aws-educate.yaml) — Free learning platform and labs
- [AWS Education Equity Initiative](data/tools/aws-education-equity-initiative.yaml) — Up to $10k credits for eligible orgs
- [DigitalOcean (GitHub Student Pack)](data/tools/digitalocean-student-pack.yaml) — $200 credit for 1 year via Pack
- [Google Cloud Education Grants](data/tools/google-cloud-education-grants.yaml) — Faculty-led course credits
- [Hugging Face Academia Hub](data/tools/huggingface-academia-hub.yaml) — Institutional $10/seat/mo program
- [Microsoft Azure for Students](data/tools/microsoft-azure-students.yaml) — $100 / 12 months, no credit card
- [OpenAI Researcher Access Program](data/tools/openai-researcher-access.yaml) — Up to $1k API credits for researchers

</details>

### Platforms & bundles

`platforms-bundles` · 7 active

<details>
<summary>Show tools</summary>

- [AWS Education Programs](data/tools/aws-education-programs.yaml) — Hub for Educate + related programs
- [GitHub Copilot (Student)](data/tools/github-copilot-student.yaml) — Free Copilot for verified students
- [GitHub Education Experiences](data/tools/github-education-experiences.yaml) — Free learning Experiences
- [GitHub Student Developer Pack](data/tools/github-student-developer-pack.yaml) — Partner tools bundle (apply once)
- [Google AI Pro for Students](data/tools/google-ai-pro-students.yaml) — 12 months free (US, SheerID)
- [JetBrains Student Pack](data/tools/jetbrains-student-pack.yaml) — Free IDEs + limited AI trial
- [Microsoft Education (Students)](data/tools/microsoft-education-students.yaml) — Azure, Learn, and related pathways

</details>

**Also in the repo but not listed above:** entries with `status: unverified` or `expired` still appear in [`data/tools/`](data/tools/)—read `status` before you rely on them.

---

## For contributors

Help keep offers accurate:

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) — how to add a tool, update `verified_at`, and use `status`.
2. Open a PR with the [pull request template](.github/PULL_REQUEST_TEMPLATE.md) (**one tool per PR**).
3. Cite an official `source_url`; do not guess discount numbers.

Schema and categories: [docs/schema.md](docs/schema.md) · [docs/taxonomy.md](docs/taxonomy.md)  
Research backlog (not yet in catalog): [docs/research/candidate-list-2026.md](docs/research/candidate-list-2026.md)

---

## License

MIT — see [LICENSE](LICENSE).
