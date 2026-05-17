#!/usr/bin/env python3
"""Regenerate docs/browse.md from data/tools/*.yaml (student-readable view)."""

from __future__ import annotations

import pathlib
import re
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT / "data/tools"
OUT = ROOT / "docs/browse.md"

# Display order (matches README / taxonomy.md)
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

L1_META = {
    "writing-text": ("Writing & text", "✍️"),
    "coding-development": ("Coding & development", "💻"),
    "research-academia": ("Research & academia", "🔬"),
    "video": ("Video", "🎬"),
    "audio-voice": ("Audio & voice", "🎙️"),
    "image-design": ("Image & design", "🎨"),
    "presentation-documents": ("Presentations & documents", "📊"),
    "learning-education": ("Learning & education", "📚"),
    "data-analytics": ("Data & analytics", "📈"),
    "productivity-notes": ("Productivity & notes", "📓"),
    "communication-meetings": ("Communication & meetings", "💬"),
    "translation-language": ("Translation & language", "🌐"),
    "legal": ("Legal", "⚖️"),
    "cloud-api-credits": ("Cloud & API credits", "☁️"),
    "platforms-bundles": ("Platforms & bundles", "🧰"),
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
        by_l1[l1m.group(1)].append(
            {
                "slug": path.stem,
                "name": field(text, "name"),
                "status": field(text, "status") or "unknown",
                "summary": summary_m.group(1).strip() if summary_m else "",
                "source": field(text, "source_url"),
                "verified": field(text, "verified_at"),
                "how": block(text, "how_to_apply"),
                "website": field(text, "website"),
            }
        )
    return by_l1


def render(by_l1: dict[str, list[dict]]) -> str:
    out: list[str] = []
    out.append("# Browse student AI offers\n\n")
    out.append(
        "Plain-English listings for students. Data is stored in "
        "[`data/tools/`](../data/tools/) as YAML for contributors—"
        "**you do not need to read YAML** to use this catalog.\n\n"
    )
    out.append(
        "[← Back to README](../README.md) · [Taxonomy](taxonomy.md) · "
        "[Contributing](../CONTRIBUTING.md)\n\n---\n\n"
    )
    out.append("## Category index\n\n")
    out.append("| | Category | Active |\n")
    out.append("|---|----------|--------|\n")
    for slug in L1_ORDER:
        label, icon = L1_META[slug]
        active = sum(1 for t in by_l1[slug] if t["status"] == "active")
        out.append(f"| {icon} | [{label}](#{slug}) | {active} |\n")
    out.append("\n---\n\n")

    for slug in L1_ORDER:
        label, icon = L1_META[slug]
        tools = by_l1.get(slug, [])
        active = [t for t in tools if t["status"] == "active"]
        other = len(tools) - len(active)
        out.append(f'<a id="{slug}"></a>\n\n')
        out.append(f"## {icon} {label}\n\n")
        out.append(f"`{slug}` · **{len(active)}** active")
        if other:
            out.append(f" · {other} not active")
        out.append("\n\n")
        if not active:
            out.append("_No active listings in this category yet._\n\n")
            continue
        for t in sorted(active, key=lambda x: x["name"].lower()):
            out.append(f'<a id="{t["slug"]}"></a>\n\n')
            out.append(f"### {t['name']}\n\n")
            out.append(
                f"**Status:** `{t['status']}` · "
                f"**Last verified:** {t['verified'] or '—'}\n\n"
            )
            out.append(f"**Offer:** {t['summary']}\n\n")
            if t["how"]:
                out.append("**How to apply**\n\n")
                for line in t["how"].splitlines():
                    line = line.strip()
                    if line:
                        out.append(f"{line}\n")
                out.append("\n")
            out.append(
                f"**Official offer page:** [{t['source']}]({t['source']})\n\n"
            )
            if t["website"] and t["website"] != t["source"]:
                out.append(
                    f"**Product homepage:** [{t['website']}]({t['website']})\n\n"
                )
            out.append("---\n\n")
    return "".join(out)


def main() -> None:
    by_l1 = load_tools()
    OUT.write_text(render(by_l1))
    print(f"Wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
