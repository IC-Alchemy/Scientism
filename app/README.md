# Scientism Wiki Browser

Static web app that bundles the entire `wiki/` corpus, readable `raw/` markdown, operation log, and vault architecture map.

## Commands

```bash
npm install
npm run dev      # http://127.0.0.1:5173
npm run build    # exports corpus, then builds to dist/
```

Corpus export: `python3 ../scripts/export_app_corpus.py`

## Routes

- **Home** — stats and entry points
- **Browse** — all pages by category
- **Search** — full-text (Ctrl/Cmd+K)
- **Page** — rendered markdown with `[[wikilink]]` resolution
- **Raw corpus** — immutable `raw/` sources
- **Vault map** — architecture from `scientism-vault-map.data.json`
- **Log** — `wiki/log.md`
