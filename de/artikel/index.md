---
layout: page
title: Artikel
lang: de
lang_alt: /articles/
description: "Praxisnahe Perspektiven darauf, wie generative KI Museen, Galerien und Archive verändert — von der Sammlungskatalogisierung und Provenienzforschung bis zum Besuchererlebnis und zur Barrierefreiheit."
---

<style>
  .articles-intro {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.95rem;
    color: #555;
    line-height: 1.85;
    margin-bottom: 2.5rem;
    max-width: 560px;
  }

  .articles-label {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #aaa;
    display: block;
    margin-bottom: 1.25rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #eee;
  }

  .article-row {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 1rem;
    padding: 1rem 0;
    border-bottom: 1px solid #f5f5f5;
    align-items: start;
  }

  .article-row:last-child { border-bottom: none; }

  .article-date {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.72rem;
    color: #bbb;
    padding-top: 0.15rem;
    white-space: nowrap;
  }

  .article-content {}

  .article-title-link {
    font-family: "Cormorant Garamond", Georgia, serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: #111;
    text-decoration: none;
    line-height: 1.3;
    display: block;
    margin-bottom: 0.3rem;
    transition: color 0.15s ease;
  }

  .article-title-link:hover { color: #CE942F; text-decoration: none; }

  .article-excerpt {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.85rem;
    color: #777;
    line-height: 1.7;
    margin: 0 0 0.5rem;
  }

  .article-meta-row {
    display: flex;
    gap: 0.5rem;
    align-items: center;
    flex-wrap: wrap;
  }

  .article-tag {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.6rem;
    font-weight: 600;
    padding: 0.12rem 0.45rem;
    border-radius: 3px;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    background: #f5e6d8;
    color: #7a4a2e;
  }

  .article-read-time {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.68rem;
    color: #bbb;
  }

  .articles-empty {
    font-family: "JetBrains Mono", monospace;
    font-size: 0.875rem;
    color: #bbb;
    padding: 2rem 0;
  }
</style>

<p class="articles-intro">
  Praxisnahe Perspektiven darauf, wie generative KI Kultureinrichtungen verändert — von der Sammlungskatalogisierung und dem Besuchererlebnis bis zur Provenienzforschung und Barrierefreiheit. Auf Deutsch verfasst.
</p>

<span class="articles-label">KI × Kunst &amp; Museum</span>

{% assign art_posts_de = site.posts | where_exp: "post", "post.categories contains 'art-museum'" | where_exp: "post", "post.lang == 'de'" %}

{% if art_posts_de.size > 0 %}
  {% for post in art_posts_de %}
  <div class="article-row">
    {% assign de_month_key = post.date | date: "%m" %}
    <span class="article-date">{{ post.date | date: "%-d" }}. {{ site.data.de_months[de_month_key] }} {{ post.date | date: "%Y" }}</span>
    <div class="article-content">
      <a class="article-title-link" href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
      {% if post.excerpt %}
      <p class="article-excerpt">{{ post.excerpt | markdownify | strip_html | truncatewords: 30 }}</p>
      {% endif %}
      <div class="article-meta-row">
        {% if post.tags %}
          {% for tag in post.tags %}
          <span class="article-tag">{{ tag }}</span>
          {% endfor %}
        {% endif %}
        {% if post.read_time %}
        <span class="article-read-time">{{ post.read_time }} Min. Lesezeit</span>
        {% endif %}
        {% if post.lang_alt %}
        <a class="article-read-time" href="{{ site.baseurl }}{{ post.lang_alt }}">In English</a>
        {% endif %}
      </div>
    </div>
  </div>
  {% endfor %}
{% else %}
  <p class="articles-empty">Noch keine Artikel — der erste folgt in Kürze.</p>
{% endif %}
