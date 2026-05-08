---
layout: article
title: "RAG Systems for Provenance Research: Making Restitution Archives Searchable"
date: 2026-05-08
categories: ["art-museum"]
tags: ["RAG", "Provenance", "Archives", "LLM"]
read_time: 7
author: Alex Snow
excerpt: "Germany holds some of the world's most significant — and most fragmented — records on Nazi-era art displacement. RAG systems don't solve the moral complexity of restitution, but they can collapse the years of archival research into weeks."
---

Germany holds some of the world's most significant — and most fragmented — records on Nazi-era art displacement. Dealers' inventories, auction catalogues, transportation manifests, correspondence between galleries and party officials: these documents exist across hundreds of archives, many only partially digitised, written in period-specific German that resists standard keyword search.

RAG (Retrieval-Augmented Generation) systems don't solve the moral complexity of restitution. But they can collapse years of archival research into weeks.

<!-- more -->

## Why Provenance Research Is Still Broken

The Washington Principles of 1998 committed signatory nations — including Germany — to identifying Nazi-looted art in public collections and pursuing fair solutions with heirs. Over 25 years later, the backlog remains enormous. The Deutsches Zentrum Kulturgutverluste (German Lost Art Foundation) in Magdeburg coordinates much of this work, but the investigative burden falls on individual institutions with limited research staff.

The core problem is not will — it is findability.

A single restitution claim might require a researcher to cross-reference:
- Dealer records from galleries like Galerie Flechtheim, Cassirer, or Thannhauser
- ERR (Einsatzstab Reichsleiter Rosenberg) transport records
- Auction catalogues from Lempertz, Dorotheum, or Sotheby's
- Post-war claims records from the Treuhandverwaltung
- Allied repatriation receipts from the MFA&A (Monuments Men)
- Private correspondence in the artist's estate

These sources are scattered across Bundesarchiv, state archives, private foundations, and international institutions. Most are scanned PDFs. None speak to each other.

## What RAG Actually Looks Like in Practice

A Retrieval-Augmented Generation system for provenance research has three components:

**1. Ingestion and chunking.** Scanned documents are processed through OCR (with Fraktur support — essential for pre-1945 German documents), split into semantically coherent chunks, and embedded into a vector database. Tesseract with Fraktur models, or commercial alternatives like Azure Document Intelligence, handle the OCR layer.

**2. Retrieval.** When a researcher queries the system — "find all references to Paul Cassirer and the Liebermann collection between 1933 and 1939" — the system retrieves the most relevant document fragments across the entire corpus using semantic similarity, not just keyword matching. This captures references even when terminology varies (the same transaction might be described as a "Verkauf", "Übergabe", or "Einlieferung" in different documents).

**3. Generation with citation.** The LLM synthesises retrieved fragments into a structured response — with citations pointing back to the source document, page, and archive. The researcher can verify every claim against the original scan. This is non-negotiable: hallucination risk means no provenance finding should ever rest solely on model output.

## A Concrete Example

Imagine a regional museum in the Rhineland holding a mid-19th century oil painting with a gap in its ownership record between 1933 and 1948. A researcher using a RAG system over a corpus of digitised dealer records, ERR documentation, and post-war claims files could:

1. Query: *"Any records mentioning [painting title] or [artist name] in dealer inventories or transfer documents from 1933–1945"*
2. Retrieve: Three fragments — an ERR inventory entry from 1942, a Lempertz catalogue entry from 1943, and a post-war Allied receipt from 1946
3. Synthesise: A structured provenance timeline with source citations for each step
4. Identify: The likely displacement chain — and the family whose claim should be investigated

Without the system, the same research might take months of manual archive visits. With it, the researcher can cover the same ground in days, and spend their time on interpretation and verification rather than document retrieval.

## Building This: Practical Considerations

**Fraktur OCR quality is the bottleneck.** Pre-1941 German documents use Fraktur typeface, which standard OCR engines handle poorly. Budget significant time for OCR quality assessment and correction pipelines before indexing.

**Chunk at the document unit level, not the page.** A single inventory entry might span multiple pages, or a single page might contain unrelated entries. Semantic chunking — splitting at logical document boundaries — dramatically improves retrieval precision.

**Metadata filtering is as important as semantic search.** Every chunk should carry structured metadata: archive, document type, date range, institution of origin. Researchers need to filter by source type ("show me only ERR records") as well as query by content.

**German legal context shapes what you can store.** Personal data in archive records — names of individuals, addresses, financial details — falls under GDPR even in historical documents. Legal review of data processing agreements with the originating archives is essential before ingestion.

**Provenance-specific fine-tuning helps.** General-purpose LLMs are not trained on period German administrative language. Few-shot examples of correctly formatted provenance summaries, plus a controlled vocabulary of period-accurate terminology, significantly improve output quality.

## What This Doesn't Replace

RAG surfaces evidence. It does not make legal determinations, assess the credibility of competing claims, or weigh moral arguments. The decisions about restitution — who owns what, what "fair and just solution" means in a given case — remain firmly in the domain of human judgement, legal expertise, and negotiation.

What the technology does is give researchers and institutions the ability to find the evidence that makes those judgements possible. In a domain where justice has been deferred for 80 years partly because the archives are impenetrable, that matters.

---

*I work with museums and archives across Germany to build practical AI infrastructure for collection research and accessibility. If your institution is sitting on digitised archives that no one can effectively search, [let's talk.](https://www.linkedin.com/in/wuthmonehninhlaing/)*
