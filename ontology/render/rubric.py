#!/usr/bin/env python3
"""
Render the overclaim ontology into a context-window rubric.

The ontology YAML is the source of truth; the LLM is the detector. This script
emits a paste-ready markdown rubric for a declared frame {genre, audience, goal},
applying the frame gate (Rule 1): codes suppressed in the genre are dropped, codes
marked advisory are downgraded one severity notch and annotated.

Usage:
  python render/rubric.py --genre advocacy --audience "dairy execs" --goal "shift buying disposition"
  python render/rubric.py --genre analytical --pack core
  python render/rubric.py --genre sales --include-suppressed   # show everything, annotated
"""
from __future__ import annotations

import argparse
import os
from typing import Any, Dict, List

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ONTOLOGY_DIR = os.path.normpath(os.path.join(HERE, "..", "ontology"))
# Draft layout keeps core.yaml at the package root, not under ontology/.
FALLBACK_DIR = os.path.normpath(os.path.join(HERE, ".."))

SEVERITY_ORDER = ["clarify", "constrain", "revise", "block"]
SEVERITY_TO_DECISION = {
    "block": "BLOCK",
    "revise": "REVISE",
    "constrain": "CONSTRAIN",
    "clarify": "CLARIFY",
    None: "AUTHORIZE",
}
AXIS_TITLES = {
    "preflight": "Framing (preflight)",
    "input": "Input framing",
    "evidence": "Evidence",
    "narrative": "Narrative drift",
    "communication": "Communication",
    "risk": "Risk",
}
AXIS_ORDER = ["preflight", "input", "evidence", "narrative", "communication", "risk"]


def _pack_path(name: str) -> str:
    bases = [
        ONTOLOGY_DIR, os.path.join(ONTOLOGY_DIR, "packs"),
        FALLBACK_DIR, os.path.join(FALLBACK_DIR, "packs"),
    ]
    for base in bases:
        cand = os.path.join(base, f"{name}.yaml")
        if os.path.exists(cand):
            return cand
    raise FileNotFoundError(f"pack not found: {name}.yaml (searched {bases})")


def load_packs(names: List[str]) -> Dict[str, Any]:
    merged: Dict[str, Any] = {"codes": [], "states": {}, "version": None, "packs": []}
    for name in names:
        data = yaml.safe_load(open(_pack_path(name)))
        merged["codes"].extend(data.get("codes", []))
        merged["states"].update(data.get("states", {}))
        merged["packs"].append(f"{data.get('pack', name)} {data.get('version', '')}".strip())
    return merged


def _downgrade(severity: str) -> str:
    i = SEVERITY_ORDER.index(severity) if severity in SEVERITY_ORDER else 0
    return SEVERITY_ORDER[max(0, i - 1)]


def _disposition(code: Dict[str, Any], genre: str) -> str:
    # Missing genre defaults to defect (apply at full severity).
    return (code.get("applies_in_frames") or {}).get(genre, "defect")


def render(packs: Dict[str, Any], genre: str, audience: str, goal: str,
           include_suppressed: bool) -> str:
    codes = packs["codes"]
    active: List[Dict[str, Any]] = []
    suppressed: List[str] = []
    for c in codes:
        disp = _disposition(c, genre)
        if disp == "suppressed" and not include_suppressed:
            suppressed.append(c["code"])
            continue
        eff = c["default_severity"]
        if disp == "advisory":
            eff = _downgrade(eff)
        c = dict(c, _effective_severity=eff, _disposition=disp)
        active.append(c)

    out: List[str] = []
    out.append(f"# Overclaim Rubric ({', '.join(packs['packs'])})")
    out.append("")
    out.append("You are an output-governance reviewer. Apply the codes below to the "
               "SUBJECT TEXT the user provides next. Do not judge truth. Judge whether "
               "confidence is earned, whether claims are framed honestly, and whether "
               "stated certainty matches the evidence shown.")
    out.append("")
    out.append("## Declared frame")
    out.append(f"- genre: {genre}")
    out.append(f"- audience: {audience or '(unspecified)'}")
    out.append(f"- goal: {goal or '(unspecified)'}")
    out.append("")
    out.append("Severity is scored relative to this frame. Codes shown as "
               "`[advisory]` are softened (one notch down) because the genre tolerates "
               "them; flag them only when egregious.")
    if suppressed:
        out.append(f"Suppressed for this genre (expected, not flagged): "
                   f"{', '.join(sorted(suppressed))}.")
    out.append("")
    out.append("## How to apply")
    out.append("1. Split the subject text into claims or sentences.")
    out.append("2. For each, cite any codes that fire and quote the trigger phrase.")
    out.append("3. A code is CLEARED if a state under its `cleared by` is satisfied "
               "*visibly in the text* (an explicit hedge, not an assumed one). Report "
               "cleared codes as cleared; do not silently drop them.")
    out.append("4. End with an aggregated decision; the highest active severity wins.")
    out.append("")
    decisions = "AUTHORIZE < CLARIFY < CONSTRAIN < REVISE < BLOCK"
    out.append(f"Decision ladder (low to high): {decisions}.")
    out.append("")

    if packs["states"]:
        out.append("## States that clear codes")
        for name, desc in packs["states"].items():
            out.append(f"- **{name}**: {str(desc).strip()}")
        out.append("")

    out.append("## Codes active in this frame")
    out.append("")
    by_axis: Dict[str, List[Dict[str, Any]]] = {}
    for c in active:
        by_axis.setdefault(c["axis"], []).append(c)
    ordered_axes = [a for a in AXIS_ORDER if a in by_axis] + \
                   [a for a in by_axis if a not in AXIS_ORDER]
    for axis in ordered_axes:
        out.append(f"### {AXIS_TITLES.get(axis, axis.title())}")
        for c in by_axis[axis]:
            tag = " [advisory]" if c["_disposition"] == "advisory" else ""
            out.append(f"- **{c['code']}** (severity: {c['_effective_severity']}{tag})")
            out.append(f"  - {str(c['definition']).strip()}")
            out.append(f"  - Fails: {str(c['example_fail']).strip()}")
            out.append(f"  - OK: {str(c['example_ok']).strip()}")
            cb = c.get("cleared_by") or []
            if cb:
                out.append(f"  - Cleared by: {', '.join(cb)}")
        out.append("")

    out.append("## Output format")
    out.append("For each claim: `claim -> [CODE: trigger phrase] (cleared? note)`.")
    out.append("Then: **Aggregated decision** + one-line rationale naming the "
               "highest-severity active finding. If two or three real commitments or "
               "well-substantiated claims carry the piece, say so; separate them from "
               "warm or confident filler.")
    out.append("")
    out.append("Paste the SUBJECT TEXT now.")
    return "\n".join(out)


def main() -> None:
    ap = argparse.ArgumentParser(description="Render the overclaim ontology as a rubric.")
    ap.add_argument("--pack", action="append", default=None,
                    help="pack name(s) to load; repeatable (default: core)")
    ap.add_argument("--genre", default="analytical",
                    help="declared genre: analytical | advocacy | sales | status | persuasion")
    ap.add_argument("--audience", default="")
    ap.add_argument("--goal", default="")
    ap.add_argument("--include-suppressed", action="store_true",
                    help="show codes suppressed in this genre, annotated")
    args = ap.parse_args()

    packs = load_packs(args.pack or ["core"])
    print(render(packs, args.genre, args.audience, args.goal, args.include_suppressed))


if __name__ == "__main__":
    main()
