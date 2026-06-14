#!/usr/bin/env python3
"""Build the overclaim.org site.

Three things happen here, in order:

1. Generate the human-browsable code catalog (`docs/codes.md`) from the shipped
   packs, so the catalog never drifts from the YAML source of truth.
2. Run `mkdocs build --strict`, producing the human HTML site in `site/`.
3. Inject the *raw* agent-facing artifacts into `site/` after the HTML build:
   `/llms.txt`, `/rubric/<genre>.md` (paste-ready rubric per frame), and
   `/packs/<pack>.yaml` (raw packs served verbatim). These are served as-is, not
   rendered to HTML, because the primary consumer is a model that fetches markdown
   and YAML, not a browser.

The renderer (`ontology/render/rubric.py`) is the build step that compiles packs
into a rubric. It never reads subject text; it emits the rubric an LLM applies.

Run locally: `python build.py`. CI runs the same command (see deploy.yml).
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "ontology", "render"))
import rubric  # noqa: E402  (the packs -> rubric compiler)

# Base URL for absolute links in llms.txt. Flip to https://overclaim.org once the
# custom domain is wired (the org Pages site then serves at the apex).
BASE_URL = "https://overclaim-org.github.io"

# v1 shipped scope: the validated spine + grounding + management. The deferred
# packs (engineering, sales, marketing) live in ontology/packs/ as source but are
# not rendered or served until they clear the contribution rule through real use.
V1_PACKS = ["core", "substantiation", "grounding", "management"]

# The frames the rubric is rendered for. Each is the same pack set under a
# different frame gate, so severity is scored relative to the declared purpose.
GENRES = ["analytical", "advocacy", "sales", "status", "persuasion"]

GENRE_BLURB = {
    "analytical": "factual/analytical writing , memos, reports, design docs, reviews",
    "advocacy": "advocacy , making a case, proposals, opinion pieces",
    "sales": "sales copy , pitches, landing pages, outbound",
    "status": "status reporting , standups, updates, exec replies",
    "persuasion": "general persuasion , essays, talks, internal selling",
}
PACK_BLURB = {
    "core": "epistemic-overclaim core (evidence, narrative, communication, risk)",
    "substantiation": "shared proof-bar axis (the FTC competent-and-reliable-evidence duty)",
    "grounding": "reasoning-environment warning lights (CC0, WillowEmberly / Negentropy)",
    "management": "commitment-without-mechanism and management-specific modes",
}

SEVERITY_ORDER = {"clarify": 0, "constrain": 1, "revise": 2, "block": 3}


def sh(cmd: list[str]) -> None:
    print(f"  $ {' '.join(cmd)}", flush=True)
    subprocess.run(cmd, cwd=HERE, check=True)


def generate_codes_catalog() -> None:
    """Write docs/codes.md: a browsable catalog of every shipped code."""
    packs = rubric.load_packs(V1_PACKS)
    codes = sorted(packs["codes"], key=lambda c: (c["axis"], c["code"]))
    out: list[str] = [
        "# Code catalog",
        "",
        f"Every code in the v1 packs ({', '.join(packs['packs'])}). "
        f"{len(codes)} codes. The YAML packs are the source of truth; this page is "
        "generated from them. The machine-readable packs are at "
        f"[`/packs/`]({BASE_URL}/packs/core.yaml).",
        "",
        "Severity ladder: `clarify < constrain < revise < block`. Disposition per "
        "genre comes from each code's frame gate (`defect` = full severity, "
        "`advisory` = one notch down, `suppressed` = expected for that genre).",
        "",
    ]
    by_axis: dict[str, list[dict]] = {}
    for c in codes:
        by_axis.setdefault(c["axis"], []).append(c)
    axis_order = [a for a in rubric.AXIS_ORDER if a in by_axis] + \
                 [a for a in by_axis if a not in rubric.AXIS_ORDER]
    for axis in axis_order:
        out.append(f"## {rubric.AXIS_TITLES.get(axis, axis.title())}")
        out.append("")
        for c in by_axis[axis]:
            out.append(f"### `{c['code']}`")
            out.append("")
            out.append(f"**{c['name']}** , severity `{c['default_severity']}`")
            out.append("")
            out.append(str(c["definition"]).strip())
            out.append("")
            out.append(f"- **Fails:** {str(c['example_fail']).strip()}")
            ok = c.get("example_ok")
            if ok:
                out.append(f"- **OK:** {str(ok).strip()}")
            frames = c.get("applies_in_frames") or {}
            if frames:
                disp = ", ".join(f"{g}: {d}" for g, d in frames.items())
                out.append(f"- **Frames:** {disp}")
            cb = c.get("cleared_by") or []
            if cb:
                out.append(f"- **Cleared by:** {', '.join(cb)}")
            mapped = c.get("maps_to") or []
            if mapped:
                out.append(f"- **Maps to:** {', '.join(mapped)}")
            out.append("")
    path = os.path.join(HERE, "docs", "codes.md")
    with open(path, "w") as f:
        f.write("\n".join(out))
    print(f"  generated docs/codes.md ({len(codes)} codes)")


def inject_raw_artifacts() -> None:
    """After mkdocs build, drop the raw markdown/YAML the agents consume into site/."""
    site = os.path.join(HERE, "site")
    rubric_dir = os.path.join(site, "rubric")
    packs_dir = os.path.join(site, "packs")
    os.makedirs(rubric_dir, exist_ok=True)
    os.makedirs(packs_dir, exist_ok=True)

    # /rubric/<genre>.md , rendered fresh from the packs every build.
    for genre in GENRES:
        packs = rubric.load_packs(V1_PACKS)
        text = rubric.render(packs, genre, audience="", goal="", include_suppressed=False)
        with open(os.path.join(rubric_dir, f"{genre}.md"), "w") as f:
            f.write(text + "\n")
    print(f"  wrote site/rubric/*.md ({len(GENRES)} genres)")

    # /packs/<pack>.yaml , served verbatim.
    for name in V1_PACKS:
        src = rubric._pack_path(name)
        with open(os.path.join(packs_dir, f"{name}.yaml"), "w") as out, open(src) as f:
            out.write(f.read())
    print(f"  wrote site/packs/*.yaml ({len(V1_PACKS)} packs)")

    # /llms.txt , the agent anchor file (llms.txt convention).
    lines = [
        "# Overclaim",
        "",
        "> An ontology of epistemic-overclaim failure modes: named codes for the ways "
        "confident language outruns its evidence, in LLM and human prose. Overclaim is "
        "an agent-facing domain , it serves a rubric a model fetches and applies to a "
        "piece of text, judging whether confidence is earned rather than whether a "
        "claim is true.",
        "",
        "To use: pick the rubric matching the text's genre, paste it into a context "
        "window above the subject text, and apply it. Severity is scored relative to "
        "the declared frame (genre/audience/goal), so an overclaim in an analytical "
        "memo is a defect while the same line in sales copy may be legitimate framing.",
        "",
        "## Rubrics (paste-ready, per frame)",
    ]
    for genre in GENRES:
        lines.append(f"- [{genre}]({BASE_URL}/rubric/{genre}.md): {GENRE_BLURB[genre]}")
    lines += ["", "## Packs (source of truth, raw YAML)"]
    for name in V1_PACKS:
        lines.append(f"- [{name}]({BASE_URL}/packs/{name}.yaml): {PACK_BLURB[name]}")
    lines += [
        "",
        "## Docs",
        f"- [Code catalog]({BASE_URL}/codes/): every code with definition and examples",
        f"- [Design]({BASE_URL}/design/): why the ontology is the asset, the frame gate, prior art",
        "",
    ]
    with open(os.path.join(site, "llms.txt"), "w") as f:
        f.write("\n".join(lines))
    print("  wrote site/llms.txt")


def main() -> None:
    print("Building overclaim.org site...")
    generate_codes_catalog()
    sh(["mkdocs", "build", "--strict"])
    inject_raw_artifacts()
    print("Done. Output in site/.")


if __name__ == "__main__":
    main()
