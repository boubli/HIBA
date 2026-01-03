# Roadcamp Wiki — HIBA

## Overview

This wiki documents the Roadcamp demo, roadmap, development notes, and contribution guidelines for the HIBA project.

## Contents

- Overview — project purpose and values
- Demo — how to run the web demo and local collector
- Roadmap — phases, milestones, and status
- Contributing — how to submit stories, code, and translations
- Data & Privacy — how captured data is handled

## Demo (roadcamp/index.html)

Quick steps:

1. Open `roadcamp/index.html` in your browser.
2. Optionally add your Groq API key in the UI to try remote reasoning features.
3. Use the interface to send messages and view Hiba's reasoning traces.

## Roadmap

- Phase 1 — Dataset standardisation (complete)
- Phase 2 — Reasoning enhancement (`<thinking>` tags) (complete)
- Phase 3 — Fine-tuning on Qwen 2.5 (in progress)
- Phase 4 — Multi-modal integration (planned)
- Phase 5 — Public release & community stories (planned)

## Development Notes

- Demo assets live in `roadcamp/assets`.
- Frontend entry point: `roadcamp/index.html` and `roadcamp/app.js`.
- Local collector / responder logic: `roadcamp/responses.js`.

## Contributing

We welcome stories, code, and translations.

- To submit a story: use the demo's submit form or open an issue with the story text.
- For code: fork the repo, open a pull request, and reference a related issue.
- For translations: add a PR that adds translated content and updates the demo labels.

## Data & Privacy

The demo stores collected entries locally by default. Do not submit private or sensitive PII.

---

If you need a dedicated GitHub Wiki page, I can scaffold `.github/wiki` content or enable the repository Wiki and push a starter page.
