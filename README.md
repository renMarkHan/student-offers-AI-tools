# Student AI Offers

A **community-maintained directory** of student and education discounts on AI-related tools. Each listing links to an official offer page and shows when it was last checked.

**Disclaimer:** Informational only—not legal, tax, or financial advice. We are not affiliated with vendors. Offers and eligibility change; **always confirm on the vendor’s site** before you sign up or pay.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## For students: start here

### 👉 [Open the browse page (recommended)](docs/browse.md)

That page is written for humans: offer summary, step-by-step **how to apply**, and a link to the **official** pricing/education page.

You do **not** need to open `.yaml` files.

| If you see… | What it is |
|-------------|------------|
| **[docs/browse.md](docs/browse.md)** | Student-friendly catalog (use this) |
| **`data/tools/*.yaml`** | Machine-readable records for contributors and scripts—not required reading for students |
| **`verified_at`** | Date someone last checked the offer against the official page |
| **`status: active`** | Reviewed listing; still confirm on the vendor site today |

**Catalog size (May 2026):** 68 active · 33 unverified · 1 expired — [102 entries in `data/tools/`](data/tools/).

---

## Browse by category

Jump into the **[full browse page](docs/browse.md)** or pick a category below (stable links).

| | Category | Active | Open |
|---|----------|--------|------|
| ✍️ | Writing & text | 3 | [Browse →](docs/browse.md#writing-text) |
| 💻 | Coding & development | 7 | [Browse →](docs/browse.md#coding-development) |
| 🔬 | Research & academia | 2 | [Browse →](docs/browse.md#research-academia) |
| 🎬 | Video | 4 | [Browse →](docs/browse.md#video) |
| 🎙️ | Audio & voice | 2 | [Browse →](docs/browse.md#audio-voice) |
| 🎨 | Image & design | 5 | [Browse →](docs/browse.md#image-design) |
| 📊 | Presentations & documents | 4 | [Browse →](docs/browse.md#presentation-documents) |
| 📚 | Learning & education | 5 | [Browse →](docs/browse.md#learning-education) |
| 📈 | Data & analytics | 5 | [Browse →](docs/browse.md#data-analytics) |
| 📓 | Productivity & notes | 4 | [Browse →](docs/browse.md#productivity-notes) |
| 💬 | Communication & meetings | 4 | [Browse →](docs/browse.md#communication-meetings) |
| 🌐 | Translation & language | 4 | [Browse →](docs/browse.md#translation-language) |
| ⚖️ | Legal | 5 | [Browse →](docs/browse.md#legal) |
| ☁️ | Cloud & API credits | 7 | [Browse →](docs/browse.md#cloud-api-credits) |
| 🧰 | Platforms & bundles | 7 | [Browse →](docs/browse.md#platforms-bundles) |

Category definitions: [docs/taxonomy.md](docs/taxonomy.md)

---

## Quick picks

| I want to… | Open on browse page |
|------------|---------------------|
| Code with AI / dev tools | [GitHub Student Pack](docs/browse.md#github-student-developer-pack) · [Cursor](docs/browse.md#cursor) · [Copilot Student](docs/browse.md#github-copilot-student) · [Azure for Students](docs/browse.md#microsoft-azure-students) |
| Write, study, research | [Notion for Education](docs/browse.md#notion-education) · [Perplexity Pro](docs/browse.md#perplexity) · [Consensus](docs/browse.md#consensus) · [Wolfram\|Alpha Pro](docs/browse.md#wolfram-alpha-pro-students) |
| Slides & design | [Figma Education](docs/browse.md#figma-education) · [Canva Education](docs/browse.md#canva-education) · [Miro Education](docs/browse.md#miro-education) |
| Video / audio | [Adobe CC Pro](docs/browse.md#adobe-creative-cloud-pro) · [Descript](docs/browse.md#descript) · [Loom](docs/browse.md#loom) · [ElevenLabs](docs/browse.md#elevenlabs) |
| US law school | [Westlaw](docs/browse.md#westlaw-law-school) · [Lexis+ AI](docs/browse.md#lexis-plus-ai-law-schools) · [Harvey Academy](docs/browse.md#harvey-academy) |

---

## For contributors

- Edit YAML in [`data/tools/`](data/tools/) per [docs/schema.md](docs/schema.md)
- After YAML changes, run `python3 scripts/generate_browse.py` to refresh [docs/browse.md](docs/browse.md)
- See [CONTRIBUTING.md](CONTRIBUTING.md) and the [PR template](.github/PULL_REQUEST_TEMPLATE.md) (**one tool per PR**)

Research backlog: [docs/research/candidate-list-2026.md](docs/research/candidate-list-2026.md)

---

## License

MIT — see [LICENSE](LICENSE).
