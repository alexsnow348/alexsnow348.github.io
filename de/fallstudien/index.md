---
layout: page
title: Fallstudien
lang: de
lang_alt: /case-studies/
description: "Anonymisierte Projektbeispiele aus Industrie, Telekommunikation und Kultureinrichtungen — echte Ergebnisse, echte Rahmenbedingungen, echte Produktionssysteme."
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

  .cs-tags { display: flex; gap: 0.35rem; flex-wrap: wrap; flex-shrink: 0; }

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

  .cs-outcomes li::before { content: "→ "; color: #CE942F; font-weight: 700; }

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
  Eine Auswahl von Projekten aus Industrie, Telekommunikation und dem Kulturbereich — was KI in der Produktion tatsächlich bedeutet, jenseits der Demo.
</p>
<p class="cs-note">Alle Kunden anonymisiert. Branche, Teamgröße und Ergebnisse sind korrekt.</p>

<div class="cs-item">
  <div class="cs-header">
    <h2 class="cs-title">Computer-Vision-QA-Pipeline für die Präzisionsfertigung</h2>
    <div class="cs-tags">
      <span class="cs-tag tag-industrial">Industrie</span>
      <span class="cs-tag tag-mlops">MLOps</span>
    </div>
  </div>
  <div class="cs-meta">Deutschland · Mittelständisches Unternehmen · MLOps Engineer</div>

  <p class="cs-body">
    Ein Hersteller von Präzisionslasertechnologie wollte die visuelle Qualitätsprüfung von Bauteilen automatisieren — mit dem Ziel, die manuelle Prüfung zu reduzieren und Inspektionsergebnisse für Ingenieure und Qualitätsteams zugänglich zu machen.
  </p>

  <span class="cs-section-label">Herausforderung</span>
  <p class="cs-body">
    Inspektionsdaten existierten, waren aber isoliert — Bilder und Ergebnisse wurden unstrukturiert gespeichert, was Trendanalysen oder Modelltraining unpraktisch machte. Ingenieure hatten keine Möglichkeit, historische Inspektionsergebnisse abzufragen oder wiederkehrende Fehlermuster zu identifizieren.
  </p>

  <span class="cs-section-label">Was wir gebaut haben</span>
  <p class="cs-body">
    Vollständiger MLOps-Lebenszyklus für die Computer-Vision-Modelle: strukturierte Datenpipelines, Modelltrainings-Infrastruktur und ein Svelte-basiertes Image-Explorer-Dashboard, das Ingenieuren interaktiven Zugriff auf Inspektionsergebnisse, Defekt-Heatmaps und Trendanalysen ermöglicht. Modelle wurden mit Monitoring-Hooks bereitgestellt, die Drift in Fehlerratenverteilungen erkannten.
  </p>

  <span class="cs-section-label">Ergebnisse</span>
  <ul class="cs-outcomes">
    <li>Inspektionsdaten erstmals abfragbar und explorierbar</li>
    <li>Deutliche Reduzierung der manuellen Prüfzeit durch Ingenieure</li>
    <li>Fehlermusteridentifikation von wochenlanger manueller Analyse auf Minuten reduziert</li>
    <li>Retraining-Pipeline für kontinuierliche Verbesserung etabliert</li>
  </ul>
</div>

<div class="cs-item">
  <div class="cs-header">
    <h2 class="cs-title">KI-gestützte Netzwerkdiagnose reduziert Helpdesk-Bearbeitungszeit</h2>
    <div class="cs-tags">
      <span class="cs-tag tag-telecom">Telekommunikation</span>
      <span class="cs-tag tag-llm">ML/KI</span>
    </div>
  </div>
  <div class="cs-meta">Malaysia · Nationaler Telekommunikationsanbieter · Lead Back End Engineer</div>

  <p class="cs-body">
    Ein nationaler Telekommunikationsanbieter wollte die Zeit reduzieren, die technische Helpdesk-Mitarbeiter für die Diagnose von Netzwerkbeschwerden aufwenden — Beschwerden, die oft die manuelle Abfrage mehrerer unverbundener Systeme erforderten.
  </p>

  <span class="cs-section-label">Herausforderung</span>
  <p class="cs-body">
    Die durchschnittliche Bearbeitungszeit betrug 27 Stunden. Mitarbeiter zogen manuell Daten aus 5+ Systemen und korrelierten Netzwerkprotokolle, Kundendaten und Fehlerhistorie. Eine einheitliche Diagnoseansicht existierte nicht.
  </p>

  <span class="cs-section-label">Was wir gebaut haben</span>
  <p class="cs-body">
    MINDS — eine KI-gestützte Netzwerkdiagnoseplattform. Datenvorverarbeitungs-Engines aggregierten Signale aus mehreren Quellsystemen in Echtzeit. Backend-API-Microservices lieferten Helpdesk-Mitarbeitern eine einheitliche Diagnoseansicht, ergänzt durch ML-Modelle, die wahrscheinliche Grundursachen und empfohlene Maßnahmen nach historischer Lösungserfolgsrate priorisierten.
  </p>

  <span class="cs-section-label">Ergebnisse</span>
  <ul class="cs-outcomes">
    <li>Durchschnittliche Bearbeitungszeit von 27 auf 9 Stunden reduziert (67% Reduktion)</li>
    <li>Mitarbeiter wechseln nicht mehr zwischen 5+ Systemen pro Fall</li>
    <li>National im gesamten Technical Helpdesk eingesetzt</li>
  </ul>
</div>

<div class="cs-item">
  <div class="cs-header">
    <h2 class="cs-title">GenAI-gestützte Sammlungskatalogisierung für ein Regionalmuseum</h2>
    <div class="cs-tags">
      <span class="cs-tag tag-culture">Kultureinrichtung</span>
      <span class="cs-tag tag-llm">GenAI</span>
    </div>
  </div>
  <div class="cs-meta">Deutschland · Regionalmuseum · KI-Berater</div>

  <p class="cs-body">
    Ein Regionalmuseum mit einer Sammlung von über 15.000 Objekten hatte Jahrzehnte inkonsistenter Katalogdatensätze — einige detailliert, viele unvollständig, manche nur als handschriftliche Inventareinträge vorhanden. Das kuratorische Team hatte keine Kapazität, 15.000 Datensätze manuell zu überarbeiten.
  </p>

  <span class="cs-section-label">Herausforderung</span>
  <p class="cs-body">
    Die Standardsuche lieferte schlechte Ergebnisse. Forscher konnten Objekte nicht nach Material, Epoche oder ikonografischem Inhalt finden. Das Museum konnte nicht an gemeinsamen digitalen Katalogen teilnehmen, da ihre Metadaten nicht den Standardschemata (LIDO, Spectrum) entsprachen.
  </p>

  <span class="cs-section-label">Was wir gebaut haben</span>
  <p class="cs-body">
    Eine GenAI-gestützte Katalogisierungspipeline: Vision-Language-Modell-Analyse von Objektfotografien zur Erstellung strukturierter Entwurfsdatensätze, LLM-Normalisierung von Freitextbeschreibungen in LIDO-konforme Felder und eine kuratorische Überprüfungsoberfläche. Das kontrollierte Vokabular basierte durchgehend auf dem Getty AAT.
  </p>

  <span class="cs-section-label">Ergebnisse</span>
  <ul class="cs-outcomes">
    <li>Kuratorische Zeit pro Objekt von ~40 auf ~8 Minuten reduziert</li>
    <li>Rückstand von 8.000 unvollständigen Datensätzen in 6 Wochen bearbeitet</li>
    <li>Sammlung jetzt nach Material, Epoche und ikonografischem Inhalt durchsuchbar</li>
    <li>Metadatenschema konform für die Integration in die Deutsche Digitale Bibliothek</li>
  </ul>
</div>
