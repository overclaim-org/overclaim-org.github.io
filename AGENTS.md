# AGENTS.md

Operational guidance for the public Overclaim site repository.

## Project Shape

- This repo publishes overclaim.org, an agent-facing static site.
- The YAML packs under `ontology/` are the source of truth.
- `build.py` renders human docs, raw rubric Markdown, raw packs, and `llms.txt`.
- The Python build code is a renderer, not a detector. Do not add subject-text
  detection or keyword scoring to it.

## Public Repo Hygiene

- Keep public commits under the `overclaim-guy <overclaim-guy@users.noreply.github.com>` identity.
- Do not add local workspace names, private account names, personal email aliases,
  machine paths, or assistant/tool-specific private guidance references.
- Do not add generated co-author trailers to public commits.
- If history has to be rewritten, verify both file contents and commit messages
  before force-pushing.

## Validation

- Run `python3 build.py` before publishing site changes when dependencies are
  available.
- If the full build is unavailable, run the narrowest relevant check and say so in
  the handoff.
