#!/usr/bin/env python3
"""Build the homepage using only the Python standard library."""
import argparse
from datetime import date
from html import escape
import json
from pathlib import Path
import re
import shutil
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]


def text(value):
    return escape(str(value), quote=True)


def link_url(value):
    if urlparse(value).scheme not in {"https", "mailto"}:
        raise ValueError(f"Expected an HTTPS or mailto link: {value}")
    return text(value)


def asset(value):
    path = (ROOT / value).resolve()
    if not path.is_relative_to(ROOT / "assets") or not path.is_file():
        raise ValueError(f"Missing or invalid asset: {value}")
    return text(value)


def publication(paper, owner):
    title = text(paper["title"])
    links = paper["links"]
    if not links:
        raise ValueError(f"Publication has no source link: {paper['title']}")
    url = link_url(links[0]["url"])
    if paper.get("image"):
        visual = (f'<img class="pub-image" src="{asset(paper["image"])}" '
                  f'alt="{text(paper.get("image_alt", paper["title"]))}" '
                  'loading="lazy" decoding="async" width="332" height="220">')
    else:
        visual = f'<span class="paper-label">{text(paper.get("short_title", paper["venue"]))}</span>'
    authors = ", ".join(
        f"<strong>{text(author)}</strong>" if author.rstrip("*†‡ ") == owner else text(author)
        for author in paper["authors"]
    )
    resources = "".join(f'<a href="{link_url(item["url"])}">[{text(item["label"])}]</a>' for item in links)
    distinction = f' <span class="distinction">{text(paper["distinction"])}</span>' if paper.get("distinction") else ""
    notes = f'<p class="pub-notes">{text(paper["notes"])}</p>' if paper.get("notes") else ""
    alternate_titles = text(" ".join(paper.get("alternative_titles", [])))
    return f'''<article class="publication" data-category="{text(paper['category'])}" data-search="{alternate_titles}">
        <a class="pub-image-link" href="{url}" aria-label="Read {title}">{visual}</a>
        <div class="pub-content">
          <h3><a class="paper-title" href="{url}">{title}</a></h3>
          <p class="authors">{authors}</p>
          <p class="venue"><em>{text(paper['venue'])}</em> · {text(paper['year'])}{distinction}</p>
          <nav class="pub-links" aria-label="Resources for {title}">{resources}</nav>
          {notes}
        </div>
      </article>'''


def build(output):
    profile = json.loads((ROOT / "data/profile.json").read_text(encoding="utf-8"))
    papers = json.loads((ROOT / "data/publications.json").read_text(encoding="utf-8"))
    papers.sort(key=lambda paper: paper["year"], reverse=True)
    name = profile["name"]
    scholar = link_url(profile["scholar_url"])
    profile_links = [{"label": "Google Scholar", "url": profile["scholar_url"]}]
    if profile.get("email"):
        profile_links.insert(0, {"label": "Email", "url": "mailto:" + profile["email"]})
    if profile.get("github_url"):
        profile_links.append({"label": "GitHub", "url": profile["github_url"]})
    profile_links.extend(profile.get("links", []))
    present_categories = list(dict.fromkeys(paper["category"] for paper in papers))
    preferred_categories = profile.get("publication_category_order", [])
    categories = [category for category in preferred_categories if category in present_categories]
    categories.extend(category for category in present_categories if category not in categories)
    controls = ""
    empty = ""
    if papers:
        buttons = '<button class="filter" type="button" data-filter="all" aria-pressed="true">All</button>'
        buttons += "".join(f'<button class="filter" type="button" data-filter="{text(category)}" aria-pressed="false">{text(category)}</button>' for category in categories)
        controls = f'''<div class="publication-tools" hidden>
        <div class="filters" role="group" aria-label="Filter publications by topic">{buttons}</div>
        <label class="search" for="publication-search"><span class="sr-only">Search publications</span>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/></svg>
          <input id="publication-search" type="search" placeholder="Search title, author, year…" autocomplete="off">
        </label>
      </div><p class="result-count" id="result-count" role="status" aria-live="polite" hidden></p>'''
        empty = '''<div class="empty-state" id="empty-state" hidden>No publications match your search.
        <button class="filter" id="reset-filters" type="button">Reset filters</button></div>'''
        publications = "\n".join(publication(paper, name) for paper in papers)
    else:
        publications = f'''<div class="scholar-card">
          <div class="scholar-symbol" aria-hidden="true"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="m2 9 10-6 10 6-10 6L2 9Z"/><path d="M6 12v6c4 3 8 3 12 0v-6M22 9v9"/></svg></div>
          <div><h3>Research &amp; publications</h3><p>Explore my publications, coauthors, and citation information on Google Scholar.</p>
          <a href="{scholar}">View Google Scholar profile <span aria-hidden="true">↗</span></a></div>
        </div>'''
    image = profile.get("portrait")
    portrait = (f'<img class="portrait" src="{asset(image)}" alt="{text(name)}" width="150" height="150" fetchpriority="high">'
                if image else '<div class="portrait monogram" aria-hidden="true">ZL</div>')
    interests = profile.get("interests", [])
    interests_html = '<ul class="interests" aria-label="Research interests">' + "".join(f"<li>{text(item)}</li>" for item in interests) + '</ul>' if interests else ""
    extra = ""
    for section in profile.get("sections", []):
        extra += f'<section><div class="section-heading"><h2>{text(section["title"])}</h2></div><ul class="service-list">'
        extra += "".join(f'<li>{text(item)}</li>' for item in section["items"]) + '</ul></section>'
    site_url = profile.get("site_url", "")
    canonical = f'<link rel="canonical" href="{link_url(site_url)}">\n  <meta property="og:url" content="{link_url(site_url)}">' if site_url else ""
    structured = {"@context": "https://schema.org", "@type": "Person", "name": name, "sameAs": [item["url"] for item in profile_links if item["url"].startswith("https:")]}
    if site_url:
        structured["url"] = site_url
    values = {
        "name": text(name),
        "native_name": f' <span class="native-name" lang="zh-CN">({text(profile["native_name"])})</span>' if profile.get("native_name") else "",
        "description": text(profile["description"]),
        "canonical": canonical,
        "structured_data": json.dumps(structured, ensure_ascii=False).replace("<", "\\u003c"),
        "profile_links": "".join(f'<a href="{link_url(item["url"])}">{text(item["label"])}</a>' for item in profile_links),
        "bio": "".join(f'<p>{text(paragraph)}</p>' for paragraph in profile["bio"]),
        "interests": interests_html,
        "portrait": portrait,
        "publications_heading": text(profile.get("publications_heading", "Publications")),
        "scholar_url": scholar,
        "publication_controls": controls,
        "publications": publications,
        "publication_empty_state": empty,
        "additional_sections": extra,
        "year": str(date.today().year),
    }
    template = (ROOT / "templates/index.html").read_text(encoding="utf-8")
    html = re.sub(r"\{\{(\w+)\}\}", lambda match: values[match[1]], template)
    html = "\n".join(line.rstrip() for line in html.splitlines()) + "\n"
    output.mkdir(parents=True, exist_ok=True)
    (output / "index.html").write_text(html, encoding="utf-8")
    if output.resolve() != ROOT:
        shutil.copytree(ROOT / "assets", output / "assets", dirs_exist_ok=True)
        (output / ".nojekyll").touch()
    if site_url:
        (output / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{text(site_url)}</loc></url></urlset>\n', encoding="utf-8")
        (output / "robots.txt").write_text(f'User-agent: *\nAllow: /\nSitemap: {site_url.rstrip("/")}/sitemap.xml\n', encoding="utf-8")
    print(f"Built {output / 'index.html'} ({len(papers)} publications)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT)
    build(parser.parse_args().output.resolve())
