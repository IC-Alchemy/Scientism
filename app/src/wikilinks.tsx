import type { Components } from "react-markdown";
import { Link } from "react-router-dom";
import { resolveWikiLink } from "./data";
import type { WikiPage } from "./types";

const WIKI_LINK = /\[\[([^\]]+)\]\]/g;

export function preprocessWikilinks(markdown: string): string {
  return markdown.replace(WIKI_LINK, (_match, inner: string) => {
    const pipe = inner.indexOf("|");
    const target = pipe >= 0 ? inner.slice(0, pipe).trim() : inner.trim();
    const label = pipe >= 0 ? inner.slice(pipe + 1).trim() : target.split("/").pop() ?? target;
    const safeTarget = encodeURIComponent(target);
    const safeLabel = label.replace(/]/g, "\\]");
    return `[${safeLabel}](wikilink:${safeTarget})`;
  });
}

export function makeMarkdownComponents(
  wikiById: Map<string, WikiPage>,
): Components {
  return {
    a({ href, children, ...props }) {
      if (href?.startsWith("wikilink:")) {
        const target = decodeURIComponent(href.slice("wikilink:".length));
        const resolved = resolveWikiLink(target, wikiById);
        if (resolved) {
          return (
            <Link to={`/page/${encodeURIComponent(resolved)}`} className="wikilink">
              {children}
            </Link>
          );
        }
        return <span className="wikilink-missing">{children}</span>;
      }
      if (href?.startsWith("http://") || href?.startsWith("https://")) {
        return (
          <a href={href} target="_blank" rel="noreferrer noopener" {...props}>
            {children}
          </a>
        );
      }
      if (href?.startsWith("#")) {
        return (
          <a href={href} {...props}>
            {children}
          </a>
        );
      }
      return (
        <a href={href} {...props}>
          {children}
        </a>
      );
    },
  };
}
