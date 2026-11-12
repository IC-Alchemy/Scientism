import { useEffect, useMemo, useState } from "react";
import { Link, Navigate, Route, Routes, useNavigate, useParams, useSearchParams } from "react-router-dom";
import Fuse from "fuse.js";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { loadCorpus, type Corpus } from "./data";
import type { RawItem, WikiPage } from "./types";
import { makeMarkdownComponents, preprocessWikilinks } from "./wikilinks";

const CATEGORY_LABELS: Record<string, string> = {
  concept: "Concepts",
  entity: "Entities",
  source: "Sources",
  synthesis: "Synthesis",
  comparison: "Comparisons",
  meta: "Vault meta",
  raw: "Raw corpus",
};

function useCorpus() {
  const [corpus, setCorpus] = useState<Corpus | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadCorpus()
      .then(setCorpus)
      .catch((e: Error) => setError(e.message));
  }, []);

  return { corpus, error, loading: !corpus && !error };
}

function Shell({ children }: { children: React.ReactNode }) {
  return (
    <div className="shell">
      <header className="topbar">
        <Link to="/" className="brand">
          Scientism Wiki
        </Link>
        <nav className="topnav">
          <Link to="/browse">Browse</Link>
          <Link to="/search">Search</Link>
          <Link to="/raw">Raw corpus</Link>
          <Link to="/map">Vault map</Link>
          <Link to="/log">Log</Link>
        </nav>
      </header>
      <main className="main">{children}</main>
    </div>
  );
}

function HomePage({ corpus }: { corpus: Corpus }) {
  const { manifest, vaultMap } = corpus;
  const topSynthesis = corpus.wiki
    .filter((p) => p.category === "synthesis" && p.summary)
    .slice(0, 8);

  return (
    <div className="home">
      <section className="hero card">
        <p className="eyebrow">Research vault · exported {manifest.generated}</p>
        <h1>{manifest.title}</h1>
        <p className="lede">{manifest.description}</p>
        <dl className="stats">
          <div>
            <dt>Wiki pages</dt>
            <dd>{manifest.stats.wiki_pages}</dd>
          </div>
          <div>
            <dt>Source summaries</dt>
            <dd>{manifest.categories.source ?? 0}</dd>
          </div>
          <div>
            <dt>Raw files</dt>
            <dd>{manifest.stats.raw_items}</dd>
          </div>
          <div>
            <dt>Readable raw markdown</dt>
            <dd>{manifest.stats.raw_markdown}</dd>
          </div>
        </dl>
      </section>

      {vaultMap && (
        <section className="card">
          <h2>{vaultMap.title}</h2>
          <p className="muted">{vaultMap.summary}</p>
          <Link to="/map" className="button">
            Open architecture map
          </Link>
        </section>
      )}

      <section className="card">
        <h2>Entry points</h2>
        <ul className="link-grid">
          <li>
            <Link to="/page/index">Wiki index</Link>
          </li>
          <li>
            <Link to="/page/synthesis%2Fviral-disease-causation-evidence-ladder">
              Viral disease causation ladder
            </Link>
          </li>
          <li>
            <Link to="/page/concepts%2Fscientism">Concept: Scientism</Link>
          </li>
          <li>
            <Link to="/page/synthesis%2Fscientism-research-program-overview">
              Research program overview
            </Link>
          </li>
        </ul>
      </section>

      <section className="card">
        <h2>Recent synthesis highlights</h2>
        <ul className="page-list">
          {topSynthesis.map((p) => (
            <li key={p.id}>
              <Link to={`/page/${encodeURIComponent(p.id)}`}>{p.title}</Link>
              {p.summary && <p className="muted">{p.summary}</p>}
            </li>
          ))}
        </ul>
      </section>

      <section className="card muted-block">
        <h2>Mission (from vault rules)</h2>
        <p>
          This vault studies scientism as an epistemic problem: extending scientific findings,
          methods, or institutions beyond what underlying evidence strictly supports. Only direct
          experiments count as evidence here; authority summaries and consensus are not substitutes
          for named endpoints and results.
        </p>
      </section>
    </div>
  );
}

function BrowsePage({ corpus }: { corpus: Corpus }) {
  const [category, setCategory] = useState<string>("all");
  const categories = Object.entries(corpus.manifest.categories).sort((a, b) => b[1] - a[1]);

  const pages =
    category === "all"
      ? corpus.wiki
      : corpus.wiki.filter((p) => p.category === category);

  return (
    <div className="browse layout-split">
      <aside className="sidebar card">
        <h2>Categories</h2>
        <button
          type="button"
          className={category === "all" ? "filter active" : "filter"}
          onClick={() => setCategory("all")}
        >
          All wiki ({corpus.wiki.length})
        </button>
        {categories.map(([cat, count]) => (
          <button
            key={cat}
            type="button"
            className={category === cat ? "filter active" : "filter"}
            onClick={() => setCategory(cat)}
          >
            {CATEGORY_LABELS[cat] ?? cat} ({count})
          </button>
        ))}
      </aside>
      <section className="card">
        <h1>{category === "all" ? "All wiki pages" : CATEGORY_LABELS[category] ?? category}</h1>
        <ul className="page-list compact">
          {pages.map((p) => (
            <li key={p.id}>
              <Link to={`/page/${encodeURIComponent(p.id)}`}>{p.title}</Link>
              {p.summary && <span className="muted"> — {p.summary}</span>}
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}

function SearchPage({ corpus }: { corpus: Corpus }) {
  const [q, setQ] = useState("");
  const fuse = useMemo(
    () =>
      new Fuse(corpus.wiki, {
        keys: [
          { name: "title", weight: 0.45 },
          { name: "summary", weight: 0.25 },
          { name: "body", weight: 0.2 },
          { name: "tags", weight: 0.1 },
        ],
        threshold: 0.38,
        ignoreLocation: true,
      }),
    [corpus.wiki],
  );

  const results = q.trim() ? fuse.search(q.trim(), { limit: 40 }).map((r) => r.item) : [];

  return (
    <div className="search card">
      <h1>Search the wiki</h1>
      <input
        type="search"
        className="search-input"
        placeholder="Title, summary, tags, or full text…"
        value={q}
        onChange={(e) => setQ(e.target.value)}
        autoFocus
      />
      {q.trim() && (
        <p className="muted">
          {results.length} result{results.length === 1 ? "" : "s"}
        </p>
      )}
      <ul className="page-list">
        {results.map((p) => (
          <li key={p.id}>
            <Link to={`/page/${encodeURIComponent(p.id)}`}>{p.title}</Link>
            <p className="muted">{p.summary || p.path}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

function PageView({ corpus }: { corpus: Corpus }) {
  const { pageId } = useParams();
  const id = pageId ? decodeURIComponent(pageId) : "";
  const page = corpus.wikiById.get(id);

  if (!page) {
    return (
      <div className="card">
        <h1>Page not found</h1>
        <p className="muted">
          No wiki page for <code>{id}</code>
        </p>
        <Link to="/browse">Back to browse</Link>
      </div>
    );
  }

  return <DocumentView page={page} corpus={corpus} kind="wiki" />;
}

function DocumentView({
  page,
  corpus,
  kind,
}: {
  page: WikiPage | RawItem;
  corpus: Corpus;
  kind: "wiki" | "raw";
}) {
  const body = "body" in page && page.body ? page.body : "_No body text exported for this file._";
  const md = preprocessWikilinks(body);
  const components = makeMarkdownComponents(corpus.wikiById);

  return (
    <article className="doc card">
      <header className="doc-header">
        <p className="eyebrow">
          {kind === "wiki" ? CATEGORY_LABELS[page.category] ?? page.category : "Raw source"} ·{" "}
          {page.path}
        </p>
        <h1>{page.title}</h1>
        {page.summary && <p className="lede">{page.summary}</p>}
        <div className="badges">
          {"updated" in page && page.updated && <span className="badge">Updated {page.updated}</span>}
          {"claim_status" in page && page.claim_status && (
            <span className="badge">{String(page.claim_status)}</span>
          )}
          {"source_tier" in page && page.source_tier && (
            <span className="badge">{String(page.source_tier)}</span>
          )}
          {"kind" in page && <span className="badge">{page.kind}</span>}
        </div>
      </header>
      <div className="markdown-body">
        <ReactMarkdown remarkPlugins={[remarkGfm]} components={components}>
          {md}
        </ReactMarkdown>
      </div>
    </article>
  );
}

function RawListPage({ corpus }: { corpus: Corpus }) {
  const readable = corpus.raw.filter((r) => r.body);
  const other = corpus.raw.filter((r) => !r.body);

  return (
    <div className="browse">
      <section className="card">
        <h1>Raw corpus (immutable sources)</h1>
        <p className="muted">
          Markdown and HTML sources are readable in the app. Binary files (PDF, images) are listed
          with size only — open them from the repository clone.
        </p>
        <h2>Readable ({readable.length})</h2>
        <ul className="page-list compact">
          {readable.map((r) => (
            <li key={r.id}>
              <Link to={`/raw/item?p=${encodeURIComponent(r.path)}`}>{r.title}</Link>
              <span className="muted"> · {r.path}</span>
            </li>
          ))}
        </ul>
        <h2>Other files ({other.length})</h2>
        <ul className="page-list compact">
          {other.map((r) => (
            <li key={r.id}>
              <span>{r.title}</span>
              <span className="muted">
                {" "}
                · {r.kind} · {(r.size_bytes / 1024).toFixed(1)} KB · {r.path}
              </span>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}

function RawPageView({ corpus }: { corpus: Corpus }) {
  const [search] = useSearchParams();
  const path = search.get("p") ?? "";
  const item = corpus.raw.find((r) => r.path === path);

  if (!item) {
    return (
      <div className="card">
        <h1>Raw file not found</h1>
        <Link to="/raw">Back to raw list</Link>
      </div>
    );
  }

  if (!item.body) {
    return (
      <div className="card">
        <h1>{item.title}</h1>
        <p className="muted">
          This file ({item.kind}, {(item.size_bytes / 1024).toFixed(1)} KB) is not inlined in the
          app bundle. Path: <code>raw/{item.path}</code>
        </p>
        <Link to="/raw">Back to raw list</Link>
      </div>
    );
  }

  return <DocumentView page={item} corpus={corpus} kind="raw" />;
}

function VaultMapPage({ corpus }: { corpus: Corpus }) {
  const map = corpus.vaultMap;
  if (!map) {
    return (
      <div className="card">
        <h1>Vault map unavailable</h1>
      </div>
    );
  }

  const byLayer = map.layers.map((layer) => ({
    ...layer,
    nodes: map.nodes.filter((n) => n.layer === layer.key),
  }));

  return (
    <div className="map">
      <section className="card">
        <h1>{map.title}</h1>
        <p className="muted">{map.subtitle}</p>
        <p>{map.summary}</p>
        <p className="meta-row">{map.meta.join(" · ")}</p>
      </section>
      {byLayer.map((layer) => (
        <section key={layer.key} className="card">
          <h2 style={{ color: layer.color }}>{layer.label}</h2>
          <ul className="page-list">
            {layer.nodes.map((n) => {
              const wikiPath = n.files?.[0]?.replace(/^wiki\//, "").replace(/\.md$/, "");
              return (
                <li key={n.id}>
                  {wikiPath ? (
                    <Link to={`/page/${encodeURIComponent(wikiPath)}`}>{n.label}</Link>
                  ) : (
                    <strong>{n.label}</strong>
                  )}
                  {n.hint && <span className="muted"> — {n.hint}</span>}
                  {n.description && <p className="muted">{n.description}</p>}
                </li>
              );
            })}
          </ul>
        </section>
      ))}
    </div>
  );
}

function LogPage({ corpus }: { corpus: Corpus }) {
  const log = corpus.wikiById.get("log");
  if (!log?.body) {
    return <div className="card"><h1>Log not found</h1></div>;
  }
  return <DocumentView page={log} corpus={corpus} kind="wiki" />;
}

export function App() {
  const { corpus, error, loading } = useCorpus();
  const navigate = useNavigate();

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === "k") {
        e.preventDefault();
        navigate("/search");
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [navigate]);

  if (loading) {
    return (
      <Shell>
        <p className="loading">Loading corpus…</p>
      </Shell>
    );
  }

  if (error || !corpus) {
    return (
      <Shell>
        <p className="error">Failed to load wiki data: {error}</p>
      </Shell>
    );
  }

  return (
    <Shell>
      <Routes>
        <Route path="/" element={<HomePage corpus={corpus} />} />
        <Route path="/browse" element={<BrowsePage corpus={corpus} />} />
        <Route path="/search" element={<SearchPage corpus={corpus} />} />
        <Route path="/page/:pageId" element={<PageView corpus={corpus} />} />
        <Route path="/raw" element={<RawListPage corpus={corpus} />} />
        <Route path="/raw/item" element={<RawPageView corpus={corpus} />} />
        <Route path="/map" element={<VaultMapPage corpus={corpus} />} />
        <Route path="/log" element={<LogPage corpus={corpus} />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Shell>
  );
}
