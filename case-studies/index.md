---
layout: page
title: Case Studies
description: "Anonymised examples of AI and MLOps projects across automotive, industrial, and cultural sectors — real outcomes, real constraints, real production systems."
---

<style>
  .cs-intro {
    font-family: "Lora", Georgia, serif;
    font-size: 0.95rem;
    color: #555;
    line-height: 1.85;
    margin-bottom: 2.5rem;
    max-width: 560px;
  }

  .cs-note {
    font-family: "Inter", sans-serif;
    font-size: 0.75rem;
    color: #bbb;
    margin-bottom: 2.5rem;
    font-style: italic;
  }

  .cs-item {
    padding: 2rem 0;
    border-bottom: 1px solid #eee;
  }

  .cs-item:last-child { border-bottom: none; }

  .cs-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 0.75rem;
    flex-wrap: wrap;
  }

  .cs-title {
    font-family: "Cormorant Garamond", Georgia, serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: #111;
    margin: 0;
    line-height: 1.3;
  }

  .cs-tags {
    display: flex;
    gap: 0.35rem;
    flex-wrap: wrap;
    flex-shrink: 0;
  }

  .cs-tag {
    font-family: "Inter", sans-serif;
    font-size: 0.62rem;
    font-weight: 600;
    padding: 0.15rem 0.5rem;
    border-radius: 3px;
    text-transform: uppercase;
    letter-spacing: 0.3px;
    white-space: nowrap;
  }

  .tag-automotive { color: #1a5c8a; background: #d6ecf8; }
  .tag-industrial { color: #5a3d8a; background: #ece5f8; }
  .tag-telecom    { color: #1f6b5b; background: #d4f0e8; }
  .tag-culture    { color: #7a4a2e; background: #f5e6d8; }
  .tag-mlops      { color: #92650a; background: #fef3d6; }
  .tag-llm        { color: #8a3d3d; background: #f8e5e5; }

  .cs-meta {
    font-family: "Inter", sans-serif;
    font-size: 0.72rem;
    color: #bbb;
    margin-bottom: 1rem;
  }

  .cs-body {
    font-family: "Lora", Georgia, serif;
    font-size: 0.9rem;
    color: #555;
    line-height: 1.8;
    margin-bottom: 1.25rem;
  }

  .cs-outcomes {
    list-style: none;
    padding: 0;
    margin: 0;
    border-left: 3px solid #CE942F;
    padding-left: 1rem;
  }

  .cs-outcomes li {
    font-family: "Inter", sans-serif;
    font-size: 0.82rem;
    color: #444;
    padding: 0.3rem 0;
    line-height: 1.5;
  }

  .cs-outcomes li::before {
    content: "→ ";
    color: #CE942F;
    font-weight: 700;
  }

  .cs-section-label {
    font-family: "Inter", sans-serif;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #aaa;
    display: block;
    margin-bottom: 0.4rem;
    margin-top: 1rem;
  }
</style>

<p class="cs-intro">
  A selection of projects across industrial, telecom, and cultural sectors — showing what production AI actually looks like beyond the demo.
</p>
<p class="cs-note">All clients anonymised. Sector, team size, and outcomes are accurate.</p>

<div class="cs-item">
  <div class="cs-header">
    <h2 class="cs-title">Computer Vision QA Pipeline for Precision Manufacturing</h2>
    <div class="cs-tags">
      <span class="cs-tag tag-industrial">Industrial</span>
      <span class="cs-tag tag-mlops">MLOps</span>
    </div>
  </div>
  <div class="cs-meta">Germany · Mid-size manufacturer · MLOps Engineer</div>

  <p class="cs-body">
    A precision laser technology manufacturer needed to automate visual quality inspection of components — reducing reliance on manual checking while making inspection results explorable by engineers and quality teams.
  </p>

  <span class="cs-section-label">Challenge</span>
  <p class="cs-body">
    Inspection data existed but was siloed — images and results were stored without structure, making trend analysis or model training impractical. Engineers had no way to query historical inspection outcomes or identify recurring defect patterns.
  </p>

  <span class="cs-section-label">What We Built</span>
  <p class="cs-body">
    Full MLOps lifecycle for the computer vision models: structured data pipelines, model training infrastructure, and a Svelte-based Image Explorer dashboard giving engineers interactive access to inspection results, defect heatmaps, and trend analytics. Models were deployed with monitoring hooks that flagged drift in defect rate distributions.
  </p>

  <span class="cs-section-label">Outcomes</span>
  <ul class="cs-outcomes">
    <li>Inspection data made queryable and explorable for the first time</li>
    <li>Engineer time spent on manual review reduced significantly</li>
    <li>Defect pattern identification that previously required weeks of manual analysis automated to minutes</li>
    <li>Model retraining pipeline established for continuous improvement</li>
  </ul>
</div>

<div class="cs-item">
  <div class="cs-header">
    <h2 class="cs-title">AI-Powered Network Diagnostics Reducing Helpdesk Resolution Time</h2>
    <div class="cs-tags">
      <span class="cs-tag tag-telecom">Telecom</span>
      <span class="cs-tag tag-llm">ML/AI</span>
    </div>
  </div>
  <div class="cs-meta">Malaysia · National telco · Lead Back End Engineer</div>

  <p class="cs-body">
    A national telecommunications provider handling millions of customer connections needed to cut the time technical helpdesk agents spent diagnosing network complaints — complaints that often required cross-referencing data from multiple disconnected systems.
  </p>

  <span class="cs-section-label">Challenge</span>
  <p class="cs-body">
    Average complaint handling time was 27 hours. Agents manually pulled data from 5+ systems, correlating network logs, customer records, and fault history. No unified diagnostic view existed.
  </p>

  <span class="cs-section-label">What We Built</span>
  <p class="cs-body">
    MINDS — an AI-driven network diagnostics platform. Data pre-processing engines aggregated signals from multiple source systems in real time. Backend API microservices served a unified diagnostic view to helpdesk agents, with ML models surfacing likely root causes and recommended actions ranked by historical resolution success rate.
  </p>

  <span class="cs-section-label">Outcomes</span>
  <ul class="cs-outcomes">
    <li>Average complaint handling time reduced from 27 hours to 9 hours (67% reduction)</li>
    <li>Agents no longer switching between 5+ systems per case</li>
    <li>Deployed nationally across the Technical Helpdesk organisation</li>
  </ul>
</div>

<div class="cs-item">
  <div class="cs-header">
    <h2 class="cs-title">GenAI Collection Cataloguing for a Regional Museum</h2>
    <div class="cs-tags">
      <span class="cs-tag tag-culture">Cultural Institution</span>
      <span class="cs-tag tag-llm">GenAI</span>
    </div>
  </div>
  <div class="cs-meta">Germany · Regional museum · AI Consultant</div>

  <p class="cs-body">
    A regional museum with a collection of 15,000+ objects had decades of inconsistent catalogue records — some detailed, many incomplete, some existing only as handwritten ledger entries. A digitisation grant created an opportunity to modernise, but the curatorial team of three had no capacity to manually rework 15,000 records.
  </p>

  <span class="cs-section-label">Challenge</span>
  <p class="cs-body">
    Standard keyword search returned poor results. Researchers couldn't find objects by material, period, or iconographic content. The museum couldn't participate in shared digital catalogues because their metadata didn't meet standard schemas (LIDO, Spectrum).
  </p>

  <span class="cs-section-label">What We Built</span>
  <p class="cs-body">
    A GenAI-assisted cataloguing pipeline: vision-language model analysis of object photographs generating structured draft records, LLM normalisation of free-text descriptions into LIDO-compliant fields, and a curatorial review interface where staff confirmed or corrected AI-generated entries. The controlled vocabulary was grounded in Getty AAT throughout.
  </p>

  <span class="cs-section-label">Outcomes</span>
  <ul class="cs-outcomes">
    <li>Curator time per object reduced from ~40 minutes to ~8 minutes</li>
    <li>Backlog of 8,000 incomplete records processed in 6 weeks</li>
    <li>Collection now discoverable by material, period, and iconographic content</li>
    <li>Metadata schema compliant for integration into Deutsche Digitale Bibliothek</li>
  </ul>
</div>
