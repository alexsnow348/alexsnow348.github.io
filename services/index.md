---
layout: page
title: Services
description: "AI strategy, LLM application development, agentic workflow design, and MLOps consulting for German SMBs and cultural institutions. Based in Germany, serving the DACH region."
---

<style>
  .services-intro {
    font-size: 0.975rem;
    color: #444;
    line-height: 1.85;
    margin-bottom: 2.5rem;
    max-width: 560px;
  }

  .service-item {
    padding: 1.75rem 0;
    border-bottom: 1px solid #eee;
  }

  .service-item:first-of-type { border-top: 1px solid #eee; }

  .service-item h3 {
    font-size: 1rem;
    font-weight: 700;
    color: #111;
    margin: 0 0 0.5rem;
  }

  .service-item p {
    font-size: 0.875rem;
    color: #555;
    line-height: 1.8;
    margin: 0 0 0.85rem;
  }

  .service-tags {
    display: flex;
    gap: 0.4rem;
    flex-wrap: wrap;
  }

  .service-tag {
    font-size: 0.68rem;
    font-weight: 600;
    font-family: "Inter", sans-serif;
    padding: 0.2rem 0.55rem;
    border-radius: 3px;
    letter-spacing: 0.3px;
  }

  /* Tag colour categories */
  .tag-strategy {
    color: #92650a;
    background: #fef3d6;
  }
  .tag-tech {
    color: #1f6b5b;
    background: #d4f0e8;
  }
  .tag-data {
    color: #1a5c8a;
    background: #d6ecf8;
  }
  .tag-ops {
    color: #5a3d8a;
    background: #ece5f8;
  }
  .tag-ai {
    color: #8a3d3d;
    background: #f8e5e5;
  }
  .tag-default {
    color: #888;
    background: #f5f5f5;
  }

  .section-label {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #aaa;
    margin: 2.5rem 0 1.25rem;
    display: block;
    font-family: "Inter", sans-serif;
  }

  .engagement-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
  }

  .engagement-card {
    border: 1px solid #eee;
    border-radius: 8px;
    padding: 1.25rem;
    position: relative;
  }

  .engagement-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    border-radius: 8px 8px 0 0;
  }

  .engagement-card.model-sprint::before  { background: #CE942F; }
  .engagement-card.model-proto::before   { background: #318F79; }
  .engagement-card.model-full::before    { background: #4A90A4; }
  .engagement-card.model-retainer::before { background: #7B5EA7; }

  .engagement-card h4 {
    font-size: 0.85rem;
    font-weight: 700;
    color: #111;
    margin: 0 0 0.25rem;
  }

  .engagement-card .duration {
    font-size: 0.7rem;
    font-family: "Inter", sans-serif;
    font-weight: 600;
    color: #aaa;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.6rem;
    display: block;
  }

  .engagement-card p {
    font-size: 0.78rem;
    color: #777;
    margin: 0;
    line-height: 1.6;
  }

  .cta-block {
    margin-top: 2.5rem;
    padding-top: 2rem;
    border-top: 1px solid #eee;
  }

  .cta-block h3 {
    font-size: 1rem;
    font-weight: 700;
    color: #111;
    margin: 0 0 0.5rem;
  }

  .cta-block p {
    font-size: 0.875rem;
    color: #555;
    line-height: 1.75;
    margin-bottom: 1rem;
  }

  .cta-block a {
    font-size: 0.875rem;
    font-weight: 600;
    color: #111;
    text-decoration: none;
    border-bottom: 2px solid #CE942F;
    padding-bottom: 1px;
  }

  .cta-block a:hover { color: #CE942F; text-decoration: none; }

  .domain-label {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #CE942F;
    display: block;
    margin-bottom: 1.25rem;
    margin-top: 2.5rem;
    font-family: "Inter", sans-serif;
  }
</style>

<p class="services-intro">
  I work with small and medium-sized companies and cultural institutions in Germany and the DACH region to turn AI from a buzzword into competitive advantage — from identifying the right use cases to shipping production-ready systems.
</p>

<span class="domain-label">For German SMBs & Mittelstand</span>

<div class="service-item">
  <h3>AI Strategy & Roadmapping</h3>
  <p>Before writing a single line of code, we need clarity on where AI genuinely moves the needle. I run structured discovery sessions to map your workflows, data landscape, and competitive context — then produce a prioritised roadmap with realistic cost and timeline estimates.</p>
  <div class="service-tags">
    <span class="service-tag tag-strategy">Use Case Discovery</span>
    <span class="service-tag tag-strategy">Build vs. Buy Analysis</span>
    <span class="service-tag tag-strategy">ROI Estimation</span>
    <span class="service-tag tag-strategy">Risk Assessment</span>
  </div>
</div>

<div class="service-item">
  <h3>LLM Application Development</h3>
  <p>Custom LLM-powered applications: document intelligence, internal knowledge assistants, customer-facing chatbots, and automated report generation. Focus is on reliability and maintainability — not demos that fail under production load.</p>
  <div class="service-tags">
    <span class="service-tag tag-ai">RAG Pipelines</span>
    <span class="service-tag tag-ai">Document Processing</span>
    <span class="service-tag tag-ai">Chatbots</span>
    <span class="service-tag tag-tech">OpenAI / Anthropic / OSS</span>
    <span class="service-tag tag-tech">LangChain / LlamaIndex</span>
  </div>
</div>

<div class="service-item">
  <h3>Agentic Workflow Design</h3>
  <p>Autonomous AI agents for complex, multi-step business processes — data extraction, competitive monitoring, compliance checks, and custom automation. Designed for your specific industry and operational context.</p>
  <div class="service-tags">
    <span class="service-tag tag-ai">Multi-Agent Systems</span>
    <span class="service-tag tag-ops">Process Automation</span>
    <span class="service-tag tag-tech">LangGraph / CrewAI</span>
    <span class="service-tag tag-ops">Human-in-the-loop</span>
  </div>
</div>

<div class="service-item">
  <h3>MLOps & Model Deployment</h3>
  <p>End-to-end infrastructure to train, evaluate, monitor, and redeploy models reliably — using Databricks, Azure ML, or open-source MLflow stacks depending on your environment and budget.</p>
  <div class="service-tags">
    <span class="service-tag tag-data">Databricks</span>
    <span class="service-tag tag-data">MLflow</span>
    <span class="service-tag tag-ops">Model Monitoring</span>
    <span class="service-tag tag-ops">CI/CD for ML</span>
    <span class="service-tag tag-data">Azure ML</span>
  </div>
</div>

<div class="service-item">
  <h3>Workshops & Team Training</h3>
  <p>Tailored sessions for your team's technical level — from executive AI overviews to hands-on prompt engineering and LLM architecture workshops. Remote or on-site across the DACH region.</p>
  <div class="service-tags">
    <span class="service-tag tag-strategy">AI for Decision Makers</span>
    <span class="service-tag tag-ai">Prompt Engineering</span>
    <span class="service-tag tag-ai">LLM Architecture</span>
    <span class="service-tag tag-tech">Hands-On Labs</span>
  </div>
</div>

<span class="domain-label">For Museums, Galleries & Archives</span>

<div class="service-item">
  <h3>Collection Intelligence</h3>
  <p>AI-powered cataloguing, metadata enrichment, and tagging for artwork and artifact collections. Transform decades of unstructured records into searchable, queryable knowledge systems.</p>
  <div class="service-tags">
    <span class="service-tag tag-data">Metadata Enrichment</span>
    <span class="service-tag tag-ai">Auto-tagging</span>
    <span class="service-tag tag-tech">Collection Search</span>
  </div>
</div>

<div class="service-item">
  <h3>Visitor Experience & Accessibility</h3>
  <p>Multilingual chatbots and interactive guides that answer questions about exhibits, artists, and provenance. Auto-generated image descriptions for visually impaired visitors. Content generation from existing collection data.</p>
  <div class="service-tags">
    <span class="service-tag tag-ai">Visitor Chatbots</span>
    <span class="service-tag tag-tech">Audio Guides</span>
    <span class="service-tag tag-default">Multilingual Content</span>
    <span class="service-tag tag-default">Accessibility AI</span>
  </div>
</div>

<div class="service-item">
  <h3>Provenance & Archive Research</h3>
  <p>RAG systems that make historical documents, letters, and auction records searchable and queryable by curators and researchers — across thousands of scanned PDFs and digitised records.</p>
  <div class="service-tags">
    <span class="service-tag tag-ai">Document RAG</span>
    <span class="service-tag tag-data">Archive Digitisation</span>
    <span class="service-tag tag-default">Provenance Research</span>
  </div>
</div>

<div class="service-item">
  <h3>Conservation Support</h3>
  <p>Computer vision workflows for condition monitoring — detecting deterioration in high-resolution artwork scans and flagging items that need restoration attention.</p>
  <div class="service-tags">
    <span class="service-tag tag-tech">Computer Vision</span>
    <span class="service-tag tag-ops">Condition Monitoring</span>
    <span class="service-tag tag-default">Restoration Flagging</span>
  </div>
</div>

<span class="section-label">Engagement Models</span>

<div class="engagement-grid">
  <div class="engagement-card model-sprint">
    <h4>Discovery Sprint</h4>
    <span class="duration">1–2 weeks</span>
    <p>Structured assessment of your AI opportunities, data readiness, and a prioritised action plan.</p>
  </div>
  <div class="engagement-card model-proto">
    <h4>Prototype Build</h4>
    <span class="duration">2–6 weeks</span>
    <p>Working proof-of-concept scoped to validate the highest-value use case before full commitment.</p>
  </div>
  <div class="engagement-card model-full">
    <h4>Full Delivery</h4>
    <span class="duration">6–12 weeks</span>
    <p>End-to-end build — from architecture through deployment, monitoring, and handover documentation.</p>
  </div>
  <div class="engagement-card model-retainer">
    <h4>Ongoing Retainer</h4>
    <span class="duration">Monthly advisory</span>
    <p>Embedded advisory: model governance, team upskilling, architecture reviews, and strategic guidance.</p>
  </div>
</div>

<div class="cta-block">
  <h3>Ready to Get Started?</h3>
  <p>Let's have a 30-minute discovery call — no sales pitch, just an honest conversation about your situation and what's realistically possible with AI for your organisation. Pricing is scoped individually after that conversation.</p>
  <a href="https://www.linkedin.com/in/wuthmonehninhlaing/" target="_blank">Connect on LinkedIn →</a>
</div>
