#!/usr/bin/env python3
"""
Fetches markdown posts from the source repo's output/substack directory,
matches each post to a GitHub Release (by date + artist name), injects
Jekyll front matter, embeds the release video/image, writes the result
to the local _posts directory, and creates a Substack draft for new posts.
"""

import json
import os
import re
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

SOURCE_REPO = "alexsnowschool-business/alexsnowschool-business.github.io"
SOURCE_PATH = "output/substack"
POSTS_DIR = "_posts"


def safe_url(url):
    """Percent-encode any non-ASCII characters in a URL string."""
    return "".join(
        c if ord(c) < 128 else urllib.parse.quote(c, safe="")
        for c in url
    )


def fetch_json(url):
    req = urllib.request.Request(safe_url(url), headers={"User-Agent": "sync-script"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def normalize(s):
    """Lowercase ASCII slug: strip accents and non-alphanumeric chars."""
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s.lower())


def build_release_index():
    """
    Returns dict keyed by (tag_date, normalized_artist) →
    {"mp4": url_or_None, "jpg": url_or_None}.

    Release tag format:  reel-weekly-YYYY-MM-DD-*
    Release name format: Artist — Painting Title — YYYY-MM-DD
    """
    index = {}
    page = 1
    while True:
        batch = fetch_json(
            f"https://api.github.com/repos/{SOURCE_REPO}/releases"
            f"?per_page=100&page={page}"
        )
        if not batch:
            break
        for rel in batch:
            tag = rel.get("tag_name", "")
            date_m = re.search(r"\d{4}-\d{2}-\d{2}", tag)
            if not date_m:
                continue
            tag_date = date_m.group(0)

            parts = re.split(r"\s*—\s*", rel.get("name", ""))  # em dash —
            artist_key = normalize(parts[0]) if parts else ""
            if not artist_key:
                continue

            key = (tag_date, artist_key)
            if key in index:
                continue  # API returns newest-first; keep the first (newest)

            assets = {a["name"]: a["browser_download_url"] for a in rel.get("assets", [])}
            mp4 = assets.get("reel.mp4")
            jpg = assets.get("src_01.jpg")
            if mp4 or jpg:
                index[key] = {"mp4": mp4, "jpg": jpg}
        page += 1
    return index


def find_media(release_index, date, slug):
    """Return the best-matching release assets for a post, or None."""
    slug_norm = normalize(slug)
    for (rel_date, rel_artist), assets in release_index.items():
        if rel_date == date and rel_artist == slug_norm:
            return assets
    for (rel_date, rel_artist), assets in release_index.items():
        if rel_date == date and rel_artist and rel_artist in slug_norm:
            return assets
    return None


def build_media_block(assets):
    """Return markdown/HTML string for image + video, or empty string."""
    if not assets:
        return ""
    parts = []
    if assets.get("jpg"):
        parts.append(f'![]({assets["jpg"]})')
    if assets.get("mp4"):
        parts.append(
            '<video controls style="width:100%;max-width:720px">\n'
            f'  <source src="{assets["mp4"]}" type="video/mp4">\n'
            "</video>"
        )
    return "\n\n".join(parts) + "\n\n" if parts else ""


def insert_media_mid_content(content, media_block):
    """Splice media block before the second ## heading; fall back to midpoint."""
    if not media_block:
        return content
    lines = content.split("\n")
    h2_indices = [i for i, l in enumerate(lines) if re.match(r"^## ", l)]
    if len(h2_indices) >= 2:
        insert_at = h2_indices[1]
    elif h2_indices:
        insert_at = h2_indices[0]
    else:
        insert_at = len(lines) // 2
    lines.insert(insert_at, media_block)
    return "\n".join(lines)


def build_front_matter(title, date, slug, excerpt):
    title = title.replace('"', '\\"')
    excerpt = excerpt.replace('"', '\\"')
    return (
        "---\n"
        "layout: article\n"
        f'title: "{title}"\n'
        f"date: {date}\n"
        f"permalink: /articles/{date}-{slug}/\n"
        'categories: ["art-museum"]\n'
        'tags: ["Art Auction", "Collectors"]\n'
        "author: @thehammerprice\n"
        f'excerpt: "{excerpt}"\n'
        "---\n\n"
    )


# ---------------------------------------------------------------------------
# Substack
# ---------------------------------------------------------------------------

def md_to_tiptap(text):
    """Convert markdown to Substack's TipTap JSON format (draft body)."""
    nodes = []
    blocks = [b.strip() for b in re.split(r"\n\n+", text.strip()) if b.strip()]

    for block in blocks:
        # Skip raw HTML blocks (video/img tags)
        if block.lstrip().startswith("<"):
            continue

        # Headings
        m = re.match(r"^(#{1,3})\s+(.+)$", block)
        if m:
            nodes.append({
                "type": "heading",
                "attrs": {"level": len(m.group(1))},
                "content": [{"type": "text", "text": m.group(2).strip()}],
            })
            continue

        # Horizontal rule
        if re.match(r"^-{3,}$", block):
            nodes.append({"type": "horizontalRule"})
            continue

        # Paragraph — strip inline markdown symbols
        clean = re.sub(r"\*\*(.+?)\*\*", r"\1", block)
        clean = re.sub(r"\*(.+?)\*", r"\1", clean)
        clean = re.sub(r"`(.+?)`", r"\1", clean)
        clean = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", clean)
        clean = clean.replace("\n", " ").strip()
        if clean:
            nodes.append({
                "type": "paragraph",
                "content": [{"type": "text", "text": clean}],
            })

    return json.dumps({"type": "doc", "content": nodes})


def post_to_substack(title, subtitle, content, token, publication):
    """Create a draft post on Substack. Returns True on success."""
    try:
        import cloudscraper
        session = cloudscraper.create_scraper()
    except ImportError:
        print("  cloudscraper not installed — skipping Substack post.")
        return False

    url = f"https://{publication}.substack.com/api/v1/drafts"
    session.cookies.set("substack.sid", token, domain=f"{publication}.substack.com")

    resp = session.post(url, json={
        "draft_title": title,
        "draft_subtitle": subtitle,
        "draft_body": md_to_tiptap(content),
        "draft_bylines": [],
        "type": "newsletter",
        "draft_section_id": None,
    })

    if resp.status_code in (200, 201):
        post_id = resp.json().get("id")
        print(f"  Substack draft created (id={post_id}) — {title}")
        return True

    print(f"  Substack error {resp.status_code}: {resp.text[:200]}")
    if resp.status_code in (401, 403):
        print("  Token may have expired — update the SUBSTACK_TOKEN secret.")
    return False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    substack_token = os.environ.get("SUBSTACK_TOKEN", "").strip()
    substack_pub   = os.environ.get("SUBSTACK_PUBLICATION", "").strip()

    release_index = build_release_index()
    print(f"Loaded {len(release_index)} releases from source repo.")

    files = fetch_json(
        f"https://api.github.com/repos/{SOURCE_REPO}/contents/{SOURCE_PATH}"
    )
    existing  = set(os.listdir(POSTS_DIR))
    new_count = 0

    for f in files:
        name = f["name"]
        if not name.endswith(".md") or name.startswith("."):
            continue

        is_new = name not in existing

        if not is_new:
            out_path = os.path.join(POSTS_DIR, name)
            with open(out_path, encoding="utf-8") as fh:
                old = fh.read()
            if (
                'categories: ["art-museum"]' in old
                and 'tags: ["Art Auction"' in old
                and not re.search(r"^# ", old, re.MULTILINE)
            ):
                continue

        req = urllib.request.Request(
            safe_url(f["download_url"]), headers={"User-Agent": "sync-script"}
        )
        with urllib.request.urlopen(req) as r:
            content = r.read().decode("utf-8")

        m = re.match(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$", name)
        if not m:
            continue
        date, slug = m.group(1), m.group(2)

        # Title: first heading, else derive from slug
        title_m = re.search(r"^#{1,3}\s+(.+)$", content, re.MULTILINE)
        if title_m:
            title = title_m.group(1).strip()
        else:
            title = re.sub(r"\(.*?\)", "", slug).replace("-", " ").strip().title()

        # Remove the first H1 line — redundant with front matter title
        content = re.sub(r"^# .+\n?", "", content, count=1, flags=re.MULTILINE)

        # Excerpt: first non-heading, non-empty line — strip markdown for plain YAML
        lines = [l.strip() for l in content.splitlines() if l.strip() and not l.startswith("#")]
        excerpt = re.sub(r"[*_`]", "", lines[0][:200]) if lines else ""

        assets     = find_media(release_index, date, slug)
        media      = build_media_block(assets)
        front_matter = build_front_matter(title, date, slug, excerpt)
        body       = insert_media_mid_content(content, media)

        out_path = os.path.join(POSTS_DIR, name)
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(front_matter + body)

        label = "with media" if media else "no media"
        print(f"{'New' if is_new else 'Updated'}: {name} ({label})")

        # Post to Substack only for brand-new posts
        if is_new and substack_token and substack_pub:
            post_to_substack(title, excerpt, content, substack_token, substack_pub)

        new_count += 1

    print(f"Done. {new_count} post(s) processed.")


if __name__ == "__main__":
    main()
