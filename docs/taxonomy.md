# Category taxonomy

Stable IDs use kebab-case. Every tool gets **exactly one** L1 + L2 pair (primary classification). Optional `tags` (see [schema](schema.md)) may list secondary capabilities.

## Primary (L1) and secondary (L2) categories

| L1 slug | L1 name | L2 slug | L2 name | Definition |
|---------|---------|---------|---------|------------|
| `writing-text` | Writing & text | `general-writing` | General writing | Drafting, rewriting, and long-form text generation. |
| | | `grammar-style` | Grammar & style | Proofreading, tone, clarity, and style suggestions. |
| | | `marketing-copy` | Marketing & copy | Ads, social, email, and conversion-oriented copy. |
| | | `academic-writing` | Academic writing | Essays, theses, and discipline-specific writing assistance. |
| `coding-development` | Coding & development | `code-assistants` | Code assistants | Inline completion, chat-in-IDE, and codegen copilots. |
| | | `dev-environments` | Dev environments | Cloud IDEs, notebooks, and full dev workspaces. |
| | | `testing-debugging` | Testing & debugging | Test generation, debugging, and code review automation. |
| | | `api-sdks` | APIs & SDKs | Developer APIs and SDKs with student credit or tier programs. |
| `research-academia` | Research & academia | `literature-search` | Literature search | Paper discovery, summaries, and research Q&A. |
| | | `citation-bibliography` | Citation & bibliography | Reference managers and citation formatting. |
| | | `data-collection` | Data collection | Surveys, scraping (where permitted), and research data tools. |
| `video` | Video | `generation` | Generation | Text/image-to-video and synthetic media creation. |
| | | `editing` | Editing | Cutting, captions, B-roll, and post-production AI. |
| | | `avatars-presenting` | Avatars & presenting | AI presenters, dubbing, and talking-head workflows. |
| `audio-voice` | Audio & voice | `speech-to-text` | Speech-to-text | Transcription and meeting capture. |
| | | `text-to-speech` | Text-to-speech | Voice synthesis and narration. |
| | | `music-audio-edit` | Music & audio editing | Music, SFX, mixing, and podcast production AI. |
| `image-design` | Image & design | `image-generation` | Image generation | Still image and illustration generation. |
| | | `photo-editing` | Photo editing | Retouching, upscaling, and photo enhancement. |
| | | `ui-graphic-design` | UI & graphic design | Layout, brand, and design-system assistance. |
| `presentation-documents` | Presentations & documents | `slides` | Slides | Deck creation and slide design. |
| | | `documents-pdf` | Documents & PDF | Document Q&A, PDF tools, and structured doc workflows. |
| | | `diagrams-whiteboards` | Diagrams & whiteboards | Flowcharts, boards, and visual explanation tools. |
| `learning-education` | Learning & education | `tutoring-explanation` | Tutoring & explanation | Step-by-step help and concept tutoring (non-cheating use). |
| | | `language-learning` | Language learning | Vocabulary, conversation practice, and fluency tools. |
| | | `course-study-aids` | Course & study aids | Flashcards, study plans, and course-specific assistants. |
| `data-analytics` | Data & analytics | `spreadsheets` | Spreadsheets | Sheet formulas, analysis, and table automation. |
| | | `sql-bi` | SQL & BI | Queries, dashboards, and business intelligence AI. |
| | | `notebooks-ml` | Notebooks & ML | Notebook environments and ML experimentation (non-dev-primary). |
| `productivity-notes` | Productivity & notes | `note-taking` | Note-taking | Notes, PKM, and knowledge bases with AI features. |
| | | `task-automation` | Task automation | Workflow, Zapier-style, and agent automation platforms. |
| | | `calendar-email` | Calendar & email | Scheduling and inbox assistance. |
| `communication-meetings` | Communication & meetings | `meeting-assistants` | Meeting assistants | Recaps, action items, and live meeting copilots. |
| | | `team-chat` | Team chat | Slack/Teams-style AI add-ons and team messaging AI. |
| `translation-language` | Translation & language | `machine-translation` | Machine translation | Document and text translation at scale. |
| | | `localization` | Localization | Product copy and locale adaptation workflows. |
| `legal` | Legal | `legal-research` | Legal research | Case law, statutes, and legal Q&A (jurisdiction-specific). |
| | | `contracts-documents` | Contracts & documents | Contract review and legal document drafting aids. |
| `cloud-api-credits` | Cloud & API credits | `hosting-deploy` | Hosting & deploy | App hosting and deployment platforms with education tiers. |
| | | `gpu-compute` | GPU & compute | GPU clouds and compute credits for models/training. |
| | | `model-apis` | Model APIs | Hosted LLM/multimodal APIs with student or education credits. |
| `platforms-bundles` | Platforms & bundles | `suites` | Suites | Multi-product bundles where no single modality dominates. |
| | | `marketplaces` | Marketplaces | App stores or aggregators with one education program covering many tools. |
| | | `student-programs` | Student programs | Vendor-agnostic education portals listing multiple partner offers. |

**L1 count:** 15 primary categories.

## Classification rules

1. **Primary intent:** Classify by the main job the student discount is marketed for (e.g. “AI writing assistant” → `writing-text`, not `productivity-notes`).
2. **Output modality wins ties:** If equally strong, pick the dominant output: text → `writing-text`, pixels → `image-design`, video → `video`, code → `coding-development`.
3. **Education-specific tutoring** vs **general chat:** Tools marketed primarily as tutors or study companions → `learning-education`; general-purpose chat with an education discount → `writing-text` / `productivity-notes` by primary use case stated on the offer page.
4. **API/credit programs** vs **apps:** Subscription app → modality L1; credits for API/compute/hosting → `cloud-api-credits`.
5. **Legal tools** always use `legal` even if they also handle documents.

## Edge cases

| Situation | Rule |
|-----------|------|
| **Multi-modal** (text + image + video) | One L1/L2 using primary intent; add optional `tags: [image-generation, video-generation]` in the tool record. Do not assign multiple L1s. |
| **IDE + cloud + model API** | If the offer is for an IDE product → `coding-development`; if only API credits → `cloud-api-credits` → `model-apis`. |
| **Bundle / suite** | No single hero product → `platforms-bundles` → `suites`. Link subsidiary tools in `related_tools` (optional) without duplicating full records. |
| **Marketplace education program** | One record for the marketplace under `platforms-bundles` → `marketplaces`; separate records for included tools only when they have **their own** distinct student offer pages. |
| **Same vendor, multiple products** | One YAML file per distinct product or distinct offer URL. |
| **Non-AI product with education discount** | Out of scope unless the offer page positions AI features as part of the discounted product; then classify by those features. |
| **Regional / institution-only offers** | In scope; document in `regional_restrictions` and `eligibility` (schema). Category unchanged. |

## Adding categories

Open an issue before adding L1/L2 slugs. New L2s must fit existing L1; new L1s require a MECE gap analysis and updates to this table and validation scripts.
