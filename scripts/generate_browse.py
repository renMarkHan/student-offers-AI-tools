#!/usr/bin/env python3
"""Regenerate docs/browse.md from data/tools/*.yaml (student-readable view)."""

from __future__ import annotations

import pathlib
import re
from collections import defaultdict
from urllib.parse import urlparse

from tool_about import TOOL_ABOUT

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT / "data/tools"
OUT = ROOT / "docs/browse.md"

L1_ORDER = [
    "writing-text",
    "coding-development",
    "research-academia",
    "video",
    "audio-voice",
    "image-design",
    "presentation-documents",
    "learning-education",
    "data-analytics",
    "productivity-notes",
    "communication-meetings",
    "translation-language",
    "legal",
    "cloud-api-credits",
    "platforms-bundles",
]

L1_META: dict[str, tuple[str, str, str]] = {
    "writing-text": (
        "Writing & text",
        "✍️",
        "Drafting, editing, grammar, and general-purpose writing assistants.",
    ),
    "coding-development": (
        "Coding & development",
        "💻",
        "IDEs, copilots, cloud dev environments, and student API or credit programs for builders.",
    ),
    "research-academia": (
        "Research & academia",
        "🔬",
        "Literature search, citations, and research Q&A tools.",
    ),
    "video": ("Video", "🎬", "Video generation, editing, and AI presenters."),
    "audio-voice": (
        "Audio & voice",
        "🎙️",
        "Transcription, text-to-speech, and audio production.",
    ),
    "image-design": (
        "Image & design",
        "🎨",
        "Image generation, photo editing, and UI or graphic design.",
    ),
    "presentation-documents": (
        "Presentations & documents",
        "📊",
        "Slides, documents, PDFs, diagrams, and whiteboards.",
    ),
    "learning-education": (
        "Learning & education",
        "📚",
        "Tutoring, language learning, flashcards, and classroom tools.",
    ),
    "data-analytics": (
        "Data & analytics",
        "📈",
        "Spreadsheets, SQL, BI, and notebook or ML platforms.",
    ),
    "productivity-notes": (
        "Productivity & notes",
        "📓",
        "Notes, tasks, and personal knowledge tools with AI features.",
    ),
    "communication-meetings": (
        "Communication & meetings",
        "💬",
        "Meeting notes, team chat, and video conferencing for schools.",
    ),
    "translation-language": (
        "Translation & language",
        "🌐",
        "Translation, localization, and writing help for multiple languages.",
    ),
    "legal": (
        "Legal",
        "⚖️",
        "Law-school and legal research platforms (often via your institution).",
    ),
    "cloud-api-credits": (
        "Cloud & API credits",
        "☁️",
        "Cloud hosting, GPU compute, and hosted model API credits.",
    ),
    "platforms-bundles": (
        "Platforms & bundles",
        "🧰",
        "Multi-product bundles and education portals (e.g. GitHub Student Pack).",
    ),
}

L2_LABEL = {
    "general-writing": "writing",
    "grammar-style": "grammar",
    "marketing-copy": "marketing copy",
    "academic-writing": "academic writing",
    "code-assistants": "code assistant",
    "dev-environments": "cloud IDE",
    "testing-debugging": "testing",
    "api-sdks": "developer API",
    "literature-search": "research search",
    "citation-bibliography": "citations",
    "data-collection": "research data",
    "generation": "video generation",
    "editing": "video editing",
    "avatars-presenting": "AI avatars",
    "speech-to-text": "transcription",
    "text-to-speech": "text-to-speech",
    "music-audio-edit": "audio editing",
    "image-generation": "image generation",
    "photo-editing": "photo editing",
    "ui-graphic-design": "UI design",
    "slides": "slides",
    "documents-pdf": "documents",
    "diagrams-whiteboards": "whiteboard",
    "tutoring-explanation": "tutoring",
    "language-learning": "language learning",
    "course-study-aids": "study aids",
    "spreadsheets": "spreadsheets",
    "sql-bi": "SQL / BI",
    "notebooks-ml": "notebooks / ML",
    "note-taking": "notes",
    "task-automation": "automation",
    "calendar-email": "calendar / email",
    "meeting-assistants": "meetings",
    "team-chat": "team chat",
    "machine-translation": "translation",
    "localization": "localization",
    "legal-research": "legal research",
    "contracts-documents": "contracts",
    "hosting-deploy": "hosting",
    "gpu-compute": "cloud compute",
    "model-apis": "model API",
    "suites": "software suite",
    "marketplaces": "marketplace",
    "student-programs": "student program",
}


def field(text: str, key: str) -> str:
    m = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def block(text: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*\|\s*\n((?:  .+\n)*)", text, re.M)
    if m:
        return "\n".join(
            ln[2:] if ln.startswith("  ") else ln for ln in m.group(1).splitlines()
        ).strip()
    m = re.search(rf"^{key}:\s*>\s*\n((?:  .+\n)*)", text, re.M)
    if m:
        return " ".join(ln.strip() for ln in m.group(1).splitlines()).strip()
    return field(text, key)


def regional_notes(text: str) -> str:
    folded = re.search(
        r"regional_restrictions:\s*\n\s+notes:\s*>\s*\n((?:  .+\n)*)",
        text,
        re.M,
    )
    if folded:
        return " ".join(ln.strip() for ln in folded.group(1).splitlines()).strip()
    inline = re.search(
        r"regional_restrictions:\s*\n\s+notes:\s*(.+)$",
        text,
        re.M,
    )
    if inline:
        return inline.group(1).strip()
    countries = re.search(
        r"regional_restrictions:\s*\n\s+countries:\s*\[([^\]]+)\]",
        text,
        re.M,
    )
    if countries:
        return f"Listed countries: {countries.group(1).strip()}"
    return ""


def link_label(url: str) -> str:
    if not url:
        return "Official page"
    host = urlparse(url).netloc.replace("www.", "")
    return host or "Official page"


def parse_tags(text: str) -> list[str]:
    m = re.search(r"^tags:\s*\n((?:  - .+\n)*)", text, re.M)
    if not m:
        return []
    return [
        ln.strip().removeprefix("- ").strip()
        for ln in m.group(1).splitlines()
        if ln.strip().startswith("-")
    ]


def keyword_line(l2: str, tags: list[str]) -> str:
    words: list[str] = []
    if l2 and l2 in L2_LABEL:
        words.append(L2_LABEL[l2])
    for tag in tags:
        if tag.replace("-", " ") not in words:
            words.append(tag.replace("-", " "))
    if not words:
        return ""
    joined = " · ".join(f"`{w}`" for w in words[:6])
    return f"**Keywords:** {joined}\n\n"


def format_steps(how: str) -> str:
    lines = [ln.strip() for ln in how.splitlines() if ln.strip()]
    if not lines:
        return ""
    out: list[str] = []
    for line in lines:
        if re.match(r"^\d+\.", line):
            out.append(line)
        else:
            out.append(f"1. {line}" if not out else f"- {line}")
    return "\n".join(out)


def render_tool(t: dict) -> str:
    parts: list[str] = []
    parts.append(f'<a id="{t["slug"]}"></a>\n\n')
    parts.append(f"### {t['name']}\n\n")
    parts.append(f"**What it is:** {t['about']}\n\n")
    kw = keyword_line(t["l2"], t["tags"])
    if kw:
        parts.append(kw)

    parts.append("| Field | Value |\n")
    parts.append("|-------|-------|\n")
    parts.append(f"| **Listing status** | `{t['status']}` |\n")
    parts.append(f"| **Last checked** | {t['verified'] or '—'} |\n")
    if t["eligibility"]:
        parts.append(f"| **Who qualifies** | {t['eligibility']} |\n")
    parts.append("\n")

    parts.append(f"> **What you get:** {t['summary']}\n\n")

    if t["how"]:
        parts.append("**Steps to apply**\n\n")
        parts.append(format_steps(t["how"]))
        parts.append("\n\n")

    parts.append(
        f"**[→ Verify on official site ({link_label(t['source'])})]({t['source']})**\n\n"
    )
    if t["website"] and t["website"] != t["source"]:
        parts.append(
            f"Product homepage: [{link_label(t['website'])}]({t['website']})\n\n"
        )

    if t["regional"]:
        parts.append(f"*Region / eligibility notes:* {t['regional']}\n\n")

    parts.append("---\n\n")
    return "".join(parts)


def load_tools() -> dict[str, list[dict]]:
    by_l1: dict[str, list[dict]] = defaultdict(list)
    for path in sorted(TOOLS_DIR.glob("*.yaml")):
        if path.name == ".gitkeep":
            continue
        text = path.read_text()
        l1m = re.search(r"^\s+l1:\s*(\S+)", text, re.M)
        if not l1m:
            continue
        summary_m = re.search(r"^\s+summary:\s*(.+)$", text, re.M)
        l2m = re.search(r"^\s+l2:\s*(\S+)", text, re.M)
        slug = path.stem
        about = field(text, "about") or TOOL_ABOUT.get(slug, "")
        by_l1[l1m.group(1)].append(
            {
                "slug": slug,
                "name": field(text, "name"),
                "status": field(text, "status") or "unknown",
                "about": about,
                "l2": l2m.group(1) if l2m else "",
                "tags": parse_tags(text),
                "summary": summary_m.group(1).strip() if summary_m else "",
                "source": field(text, "source_url"),
                "verified": field(text, "verified_at"),
                "how": block(text, "how_to_apply"),
                "website": field(text, "website"),
                "eligibility": block(text, "eligibility") or field(text, "eligibility"),
                "regional": regional_notes(text),
            }
        )
    return by_l1


def render(by_l1: dict[str, list[dict]]) -> str:
    total_active = sum(
        1 for slug in L1_ORDER for t in by_l1[slug] if t["status"] == "active"
    )
    out: list[str] = []

    out.append("# Browse student AI offers\n\n")
    out.append(
        "Readable catalog for students. Every detail below is copied from "
        "[`data/tools/`](../data/tools/) and linked to an official vendor page—"
        "**prices and eligibility can change; always confirm on the official site before you sign up.**\n\n"
    )
    out.append(
        "[← Home](../README.md) · [Category index](#category-index) · "
        "[Taxonomy](taxonomy.md) · [Contribute](../CONTRIBUTING.md)\n\n"
    )

    out.append("## How to use this page\n\n")
    out.append("1. Pick a **category** in the table below.\n")
    out.append("2. Open a tool and read **What you get** and **Steps to apply**.\n")
    out.append(
        "3. Click **Verify on official site** and confirm the offer still applies to you.\n\n"
    )
    out.append("| Term | Meaning |\n")
    out.append("|------|--------|\n")
    out.append("| **Listing status `active`** | A maintainer matched this entry to `source_url` on the date shown. |\n")
    out.append("| **Last checked** | Date of that match—not a guarantee the offer still works today. |\n")
    out.append(
        f"| **Tools shown** | **{total_active}** listings with `status: active` only "
        "(unverified entries are hidden here; see [`data/tools/`](../data/tools/) for the full set). |\n\n"
    )

    out.append('<a id="category-index"></a>\n\n')
    out.append("## Category index\n\n")
    out.append("| | Category | Tools | Jump |\n")
    out.append("|:---:|----------|:-----:|:----:|\n")
    for slug in L1_ORDER:
        label, icon, _ = L1_META[slug]
        active = sum(1 for t in by_l1[slug] if t["status"] == "active")
        out.append(
            f"| {icon} | **{label}** | {active} | [↓](#{slug}) |\n"
        )
    out.append("\n---\n\n")

    for slug in L1_ORDER:
        label, icon, blurb = L1_META[slug]
        tools = by_l1.get(slug, [])
        active = sorted(
            [t for t in tools if t["status"] == "active"],
            key=lambda x: x["name"].lower(),
        )
        other = len(tools) - len(active)

        out.append(f'<a id="{slug}"></a>\n\n')
        out.append(f"## {icon} {label}\n\n")
        out.append(f"{blurb}\n\n")
        out.append(
            f"**{len(active)}** active listing{'s' if len(active) != 1 else ''}"
        )
        if other:
            out.append(f" · {other} other status in data (not shown)")
        out.append(" · [↑ Back to index](#category-index)\n\n")

        if not active:
            out.append("_No active listings in this category yet._\n\n")
            out.append("---\n\n")
            continue

        out.append("**Tools in this category**\n\n")
        for t in active:
            out.append(
                f"- [**{t['name']}**](#{t['slug']}) — {t['about']}\n"
            )
        out.append("\n")

        for t in active:
            out.append(render_tool(t))

    out.append("## Before you sign up\n\n")
    out.append(
        "- Offers expire, change region, or require `.edu`, SheerID, or a school license.\n"
    )
    out.append(
        "- Found a mistake? [Open an issue](https://github.com/renMarkHan/student-offers-AI-tools/issues) "
        "or see [CONTRIBUTING.md](../CONTRIBUTING.md).\n"
    )

    return "".join(out)


def main() -> None:
    by_l1 = load_tools()
    OUT.write_text(render(by_l1))
    print(f"Wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
