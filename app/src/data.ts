import type { Manifest, RawItem, VaultMap, WikiPage } from "./types";

export type Corpus = {
  manifest: Manifest;
  wiki: WikiPage[];
  raw: RawItem[];
  vaultMap: VaultMap | null;
  wikiById: Map<string, WikiPage>;
  rawById: Map<string, RawItem>;
};

let cache: Corpus | null = null;

async function loadJson<T>(url: string): Promise<T> {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to load ${url}: ${res.status}`);
  }
  return res.json() as Promise<T>;
}

export async function loadCorpus(): Promise<Corpus> {
  if (cache) {
    return cache;
  }
  const [manifest, wiki, raw] = await Promise.all([
    loadJson<Manifest>("data/manifest.json"),
    loadJson<WikiPage[]>("data/wiki-pages.json"),
    loadJson<RawItem[]>("data/raw-items.json"),
  ]);

  let vaultMap: VaultMap | null = null;
  try {
    vaultMap = await loadJson<VaultMap>("data/vault-map.json");
  } catch {
    vaultMap = null;
  }

  const wikiById = new Map(wiki.map((p) => [p.id, p]));
  const rawById = new Map(raw.map((p) => [p.id, p]));
  cache = { manifest, wiki, raw, vaultMap, wikiById, rawById };
  return cache;
}

export function resolveWikiLink(target: string, wikiById: Map<string, WikiPage>): string | null {
  const clean = target
    .replace(/^wiki\//, "")
    .replace(/^\//, "")
    .split("#")[0]
    .split("|")[0]
    .trim();
  if (!clean) {
    return null;
  }
  const candidates = [
    clean,
    clean.replace(/\.md$/, ""),
    clean.endsWith(".md") ? clean.slice(0, -3) : `${clean}`,
  ];
  for (const c of candidates) {
    if (wikiById.has(c)) {
      return c;
    }
  }
  const normalized = clean.toLowerCase().replace(/\s+/g, "-");
  for (const [id] of wikiById) {
    if (id.endsWith(`/${normalized}`) || id === normalized) {
      return id;
    }
  }
  return null;
}
