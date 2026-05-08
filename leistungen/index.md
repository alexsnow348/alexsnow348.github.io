---
layout: page
title: Leistungen
lang: de
lang_alt: /services/
description: "KI-Strategie, LLM-Entwicklung, agentische Systeme und MLOps-Beratung für deutsche KMU und Kultureinrichtungen. Praxisnah, produktionsreif, auf Ihr Unternehmen zugeschnitten."
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

  .tag-strategy { color: #92650a; background: #fef3d6; }
  .tag-tech     { color: #1f6b5b; background: #d4f0e8; }
  .tag-data     { color: #1a5c8a; background: #d6ecf8; }
  .tag-ops      { color: #5a3d8a; background: #ece5f8; }
  .tag-ai       { color: #8a3d3d; background: #f8e5e5; }
  .tag-default  { color: #888;    background: #f5f5f5; }

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
    top: 0; left: 0; right: 0;
    height: 3px;
    border-radius: 8px 8px 0 0;
  }

  .engagement-card.model-sprint::before   { background: #CE942F; }
  .engagement-card.model-proto::before    { background: #318F79; }
  .engagement-card.model-full::before     { background: #4A90A4; }
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
</style>

<p class="services-intro">
  Ich helfe kleinen und mittelständischen Unternehmen sowie Kultureinrichtungen in Deutschland und der DACH-Region dabei, KI vom Buzzword zum echten Wettbewerbsvorteil zu machen — von der Identifikation der richtigen Anwendungsfälle bis hin zu produktionsreifen Systemen.
</p>

<span class="domain-label">Für deutsche KMU & Mittelstand</span>

<div class="service-item">
  <h3>KI-Strategie & Roadmapping</h3>
  <p>Bevor eine einzige Zeile Code geschrieben wird, brauchen wir Klarheit darüber, wo KI wirklich einen Unterschied macht. Ich führe strukturierte Discovery-Sessions durch, um Ihre Prozesse, Datenlage und den Wettbewerbskontext zu analysieren — und erstelle dann eine priorisierte Roadmap mit realistischen Kosten- und Zeitschätzungen.</p>
  <div class="service-tags">
    <span class="service-tag tag-strategy">Use-Case-Analyse</span>
    <span class="service-tag tag-strategy">Build vs. Buy</span>
    <span class="service-tag tag-strategy">ROI-Schätzung</span>
    <span class="service-tag tag-strategy">Risikoabwägung</span>
  </div>
</div>

<div class="service-item">
  <h3>LLM-Anwendungsentwicklung</h3>
  <p>Maßgeschneiderte LLM-gestützte Anwendungen: Dokumentenintelligenz, interne Wissensassistenten, kundenorientierte Chatbots und automatisierte Berichterstellung. Fokus auf Zuverlässigkeit und Wartbarkeit — keine Demos, die unter Produktionslast versagen.</p>
  <div class="service-tags">
    <span class="service-tag tag-ai">RAG-Pipelines</span>
    <span class="service-tag tag-ai">Dokumentenverarbeitung</span>
    <span class="service-tag tag-ai">Chatbots</span>
    <span class="service-tag tag-tech">OpenAI / Anthropic / OSS</span>
    <span class="service-tag tag-tech">LangChain / LlamaIndex</span>
  </div>
</div>

<div class="service-item">
  <h3>Agentische Workflow-Entwicklung</h3>
  <p>Autonome KI-Agenten für komplexe, mehrstufige Geschäftsprozesse — Datenextraktion, Wettbewerbsbeobachtung, Compliance-Prüfungen und individuelle Automatisierung. Passgenau für Ihre Branche und Ihren Betriebskontext entwickelt.</p>
  <div class="service-tags">
    <span class="service-tag tag-ai">Multi-Agenten-Systeme</span>
    <span class="service-tag tag-ops">Prozessautomatisierung</span>
    <span class="service-tag tag-tech">LangGraph / CrewAI</span>
    <span class="service-tag tag-ops">Human-in-the-loop</span>
  </div>
</div>

<div class="service-item">
  <h3>MLOps & Modell-Deployment</h3>
  <p>End-to-End-Infrastruktur zum zuverlässigen Training, zur Evaluierung, Überwachung und zum Re-Deployment von Modellen — mit Databricks, Azure ML oder Open-Source-MLflow-Stacks, je nach Ihrer Umgebung und Ihrem Budget.</p>
  <div class="service-tags">
    <span class="service-tag tag-data">Databricks</span>
    <span class="service-tag tag-data">MLflow</span>
    <span class="service-tag tag-ops">Modell-Monitoring</span>
    <span class="service-tag tag-ops">CI/CD für ML</span>
    <span class="service-tag tag-data">Azure ML</span>
  </div>
</div>

<div class="service-item">
  <h3>Workshops & Teamtraining</h3>
  <p>Maßgeschneiderte Sessions für das technische Niveau Ihres Teams — von KI-Überblicken für Führungskräfte bis hin zu praxisorientierten Prompt-Engineering- und LLM-Architektur-Workshops. Remote oder vor Ort in der DACH-Region.</p>
  <div class="service-tags">
    <span class="service-tag tag-strategy">KI für Entscheider</span>
    <span class="service-tag tag-ai">Prompt Engineering</span>
    <span class="service-tag tag-ai">LLM-Architektur</span>
    <span class="service-tag tag-tech">Hands-On Labs</span>
  </div>
</div>

<span class="domain-label">Für Museen, Galerien & Archive</span>

<div class="service-item">
  <h3>Sammlungsintelligenz</h3>
  <p>KI-gestützte Katalogisierung, Metadaten-Anreicherung und Verschlagwortung für Kunst- und Objektsammlungen. Jahrzehnte unstrukturierter Datensätze werden in durchsuchbare, abfragbare Wissenssysteme verwandelt.</p>
  <div class="service-tags">
    <span class="service-tag tag-data">Metadaten-Anreicherung</span>
    <span class="service-tag tag-ai">Auto-Tagging</span>
    <span class="service-tag tag-tech">Sammlungssuche</span>
  </div>
</div>

<div class="service-item">
  <h3>Besuchererlebnis & Barrierefreiheit</h3>
  <p>Mehrsprachige Chatbots und interaktive Guides, die Fragen zu Exponaten, Künstlern und Provenienz beantworten. Automatisch generierte Bildbeschreibungen für sehbehinderte Besucher. Inhaltsgenerierung auf Basis vorhandener Sammlungsdaten.</p>
  <div class="service-tags">
    <span class="service-tag tag-ai">Besucher-Chatbots</span>
    <span class="service-tag tag-tech">Audioguides</span>
    <span class="service-tag tag-default">Mehrsprachige Inhalte</span>
    <span class="service-tag tag-default">Barrierefreiheits-KI</span>
  </div>
</div>

<div class="service-item">
  <h3>Provenienz- & Archivforschung</h3>
  <p>RAG-Systeme, die historische Dokumente, Briefe und Auktionsunterlagen für Kuratoren und Forscher durchsuchbar und abfragbar machen — über Tausende von gescannten PDFs und digitalisierten Akten hinweg.</p>
  <div class="service-tags">
    <span class="service-tag tag-ai">Dokument-RAG</span>
    <span class="service-tag tag-data">Archiv-Digitalisierung</span>
    <span class="service-tag tag-default">Provenienzforschung</span>
  </div>
</div>

<div class="service-item">
  <h3>Konservierungsunterstützung</h3>
  <p>Computer-Vision-Workflows zur Zustandsüberwachung — Erkennung von Schäden in hochauflösenden Kunstwerk-Scans und Markierung von Objekten, die restauriert werden müssen.</p>
  <div class="service-tags">
    <span class="service-tag tag-tech">Computer Vision</span>
    <span class="service-tag tag-ops">Zustandsmonitoring</span>
    <span class="service-tag tag-default">Restaurierungshinweise</span>
  </div>
</div>

<span class="section-label">Zusammenarbeitsmodelle</span>

<div class="engagement-grid">
  <div class="engagement-card model-sprint">
    <h4>Discovery Sprint</h4>
    <span class="duration">1–2 Wochen</span>
    <p>Strukturierte Analyse Ihrer KI-Potenziale, Datenreife und ein priorisierter Aktionsplan.</p>
  </div>
  <div class="engagement-card model-proto">
    <h4>Prototyp-Entwicklung</h4>
    <span class="duration">2–6 Wochen</span>
    <p>Funktionsfähiger Proof-of-Concept, um den wertvollsten Anwendungsfall vor dem Vollprojekt zu validieren.</p>
  </div>
  <div class="engagement-card model-full">
    <h4>Vollständige Umsetzung</h4>
    <span class="duration">6–12 Wochen</span>
    <p>End-to-End-Entwicklung — von der Architektur über das Deployment bis zur Übergabe-Dokumentation.</p>
  </div>
  <div class="engagement-card model-retainer">
    <h4>Laufendes Retainer</h4>
    <span class="duration">Monatliche Beratung</span>
    <p>Eingebettete Begleitung: Modell-Governance, Team-Upskilling, Architektur-Reviews und strategische Beratung.</p>
  </div>
</div>

<div class="cta-block">
  <h3>Bereit für den ersten Schritt?</h3>
  <p>Lassen Sie uns 30 Minuten sprechen — kein Verkaufsgespräch, sondern ein ehrlicher Austausch über Ihre Situation und was mit KI realistisch möglich ist. Die Preisgestaltung wird individuell nach diesem Gespräch festgelegt.</p>
  <a href="https://www.linkedin.com/in/wuthmonehninhlaing/" target="_blank">Auf LinkedIn verbinden →</a>
</div>
