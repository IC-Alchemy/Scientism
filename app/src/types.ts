export type WikiPage = {
  id: string;
  path: string;
  layer: "wiki";
  title: string;
  category: string;
  summary: string;
  tags: string[];
  updated: string;
  claim_status?: string;
  claim_type?: string;
  source_tier?: string;
  sources?: string | number;
  body: string;
};

export type RawItem = {
  id: string;
  path: string;
  layer: "raw";
  title: string;
  category: string;
  summary: string;
  kind: string;
  size_bytes: number;
  body?: string;
};

export type Manifest = {
  generated: string;
  title: string;
  description: string;
  stats: {
    wiki_pages: number;
    raw_items: number;
    raw_markdown: number;
  };
  index_excerpt: string;
  categories: Record<string, number>;
};

export type VaultMap = {
  title: string;
  subtitle: string;
  summary: string;
  meta: string[];
  layers: { key: string; label: string; color: string }[];
  nodes: {
    id: string;
    label: string;
    hint?: string;
    layer: string;
    description?: string;
    files?: string[];
  }[];
};
