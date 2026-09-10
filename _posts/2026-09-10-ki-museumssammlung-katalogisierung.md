---
layout: article
title: "Wie GenAI die Katalogisierung von Museumssammlungen verändert"
date: 2026-09-10
categories: ["art-museum"]
tags: ["GenAI", "Sammlungen", "RAG", "Metadaten"]
read_time: 6
author: Alex Snow
lang: de
lang_alt: /art-museum/2026/05/08/genai-in-museum-collection-cataloguing/
permalink: /de/artikel/ki-museumssammlung-katalogisierung/
excerpt: "Die meisten Museumssammlungen sitzen auf jahrzehntealten, inkonsistenten Metadaten — Freitextbeschreibungen, Abkürzungen, fehlende Felder. GenAI automatisiert nicht nur den Rückstau, sondern verändert, was überhaupt möglich ist."
---

Die meisten Museumssammlungen sitzen auf jahrzehntealten, inkonsistenten Metadaten — Freitextbeschreibungen, hausinternen Abkürzungen, fehlenden Feldern und Datensätzen, die nur in physischen Karteien existieren. Die klassische Antwort war langsame, teure manuelle Katalogisierung. GenAI verändert diese Gleichung.

<!-- more -->

**Das Wichtigste in Kürze:**

- Vision-Language-Modelle können aus Objektfotos strukturierte Metadatenentwürfe erzeugen — Material, Technik, Datierung, Zustand — zur kuratorischen Prüfung, nicht zum Ersatz der Kuratorin.
- LLM-Pipelines können jahrzehntealte Freitextbeschreibungen in standardisierte Felder überführen und dabei unklare Einträge für die menschliche Prüfung markieren, statt zu raten.
- RAG macht Provenienzarchive per natürlicher Sprache abfragbar und ersetzt so manuelles Querverweisen über verstreute Dokumente hinweg.
- Beginnen Sie mit einem begrenzten Pilotprojekt von 500–2.000 Objekten, behalten Sie einen menschlichen Prüfschritt bei, und klären Sie EU-Datenresidenz-Anforderungen, bevor Sie einen Modellanbieter wählen.

## Das Ausmaß des Problems

Allein Deutschland hat über 6.800 Kultureinrichtungen. Die Staatlichen Museen zu Berlin verwahren über fünf Millionen Objekte. Das Germanische Nationalmuseum in Nürnberg — weitere drei Millionen. Für kleinere Regionalmuseen kann bereits eine Sammlung von 20.000 Objekten Jahrzehnte an Katalogisierungsrückstand bedeuten, weil den meisten Häusern schlicht das kuratorische Personal fehlt, um Schritt zu halten.

Die Folge: Objekte liegen im Depot, unauffindbar für Forschende und die Öffentlichkeit gleichermaßen. Was sich nicht durchsuchen lässt, lässt sich weder erforschen noch verleihen, digitalisieren oder zugänglich machen.

## Was GenAI hier tatsächlich leistet

Generative KI ersetzt keine Kuratorinnen und Kuratoren. Sie übernimmt die arbeitsintensive Vorarbeit, damit sich das kuratorische Personal auf Interpretation und Kontext konzentrieren kann.

**Metadatenanreicherung aus Bildmaterial.** Aktuelle Vision-Language-Modelle (Claude, GPT-5, Gemini) können hochauflösende Fotografien von Objekten analysieren und strukturierte Datensatzentwürfe erzeugen — Material, Technik, Datierungsschätzung, ikonografische Elemente, Zustandsnotizen. Eine Kuratorin prüft und bestätigt, statt von Grund auf zu schreiben.

**Normalisierung von Altbeständen.** Jahrzehntealte Freitextbeschreibungen lassen sich über eine LLM-Pipeline verarbeiten, um Felder wie Urheber, Datierungsspanne, Provenienz, Maße und Erwerbsquelle zu extrahieren und zu standardisieren. Das Modell markiert unklare Einträge zur menschlichen Prüfung, statt zu raten.

**Mehrsprachige Metadatengenerierung.** Für Häuser, die internationale Forschende oder Touristen ansprechen wollen, kann GenAI aus einem einzigen maßgeblichen Datensatz deutsche, englische und französische Metadatenvarianten erzeugen — konsistent im Ton und fachlich präzise.

**RAG-gestützte Provenienzforschung.** Retrieval-Augmented-Generation-Systeme machen Tausende gescannter Auktionsprotokolle, Händlerrechnungen und Korrespondenzen abfragbar. Eine Kuratorin fragt: „Zeige mir alle Einträge, die die Galerie Flechtheim zwischen 1925 und 1933 erwähnen" — das System durchsucht digitalisierte Archive und liefert relevante Fundstellen. Ich gehe darauf in [meinem Beitrag zu RAG in der Provenienzforschung]({% post_url 2026-09-10-rag-provenienzforschung-deutsche-museen %}) genauer ein.

## Ein realistischer Umsetzungspfad

Die Lücke zwischen einem Proof of Concept und einer produktionsreifen Katalogisierungs-Pipeline ist erheblich. Ein paar Prinzipien, die sich institutionsübergreifend bewährt haben:

1. **Mit einer begrenzten Teilsammlung beginnen.** Wählen Sie 500–2.000 Objekte mit einigermaßen brauchbaren Bestandsdaten. Damit kalibrieren Sie die Ausgabequalität des Modells und etablieren einen Prüfworkflow, bevor Sie skalieren.

2. **Einen menschlichen Prüfschritt einbauen.** Keine KI-Ausgabe sollte direkt in einen öffentlichen Katalog gelangen. Der Mehrwert liegt darin, die Zeit pro Objekt von 45 auf 10 Minuten zu reduzieren — nicht darin, die Kuratorin zu ersetzen.

3. **Zuerst das kontrollierte Vokabular definieren.** GenAI erzeugt inkonsistente Terminologie, wenn sie nicht eingegrenzt wird. Wer das bevorzugte Vokabular der Institution (etwa Getty AAT) als Kontext einspeist, verbessert die Konsistenz deutlich.

4. **Datenresidenz spielt in Deutschland eine Rolle.** DSGVO und institutionelle Datenrichtlinien verlangen häufig, dass Sammlungsdaten — insbesondere Provenienzangaben — die EU-Infrastruktur nicht verlassen. Azure OpenAI, Mistral und andere in Deutschland bzw. der EU gehostete Alternativen sind neben US-basierten APIs eine Prüfung wert.

## Was das über die Katalogisierung hinaus ermöglicht

Eine gut strukturierte digitale Sammlung ist nicht nur ein kuratorisches Gut — sie ist Infrastruktur. Sobald Metadaten konsistent und maschinenlesbar sind, lässt sich damit:

- Semantische Suche für Forschende ermöglichen (Suche nach Konzept, nicht nur nach Schlagwort)
- Barrierefreie Bildbeschreibungen für sehbehinderte Besucher erzeugen
- [Mehrsprachige Besucher-Chatbots]({% post_url 2026-09-10-mehrsprachige-besucher-chatbots-deutsche-museen %}) auf Basis der eigenen Sammlungsdaten aufbauen
- Für Sonderausstellungen relevante Sammlungsobjekte automatisch aufzeigen

Der Rückstau ist der Engpass. GenAI macht seine Auflösung realistisch.

## Häufig gestellte Fragen

**Kann GenAI Kuratorinnen und Kuratoren bei der Katalogisierung ersetzen?**

Nein. Sie übernimmt die arbeitsintensive Vorarbeit — Entwürfe, Feldnormalisierung, Übersetzung —, während das kuratorische Personal prüft, korrigiert und Interpretation hinzufügt. Ziel ist weniger Zeit pro Objekt, nicht der Wegfall kuratorischer Urteilskraft.

**Welche KI-Modelle können Metadaten aus Objektfotografien erzeugen?**

Aktuelle Vision-Language-Modelle wie Claude, GPT-5 und Gemini können hochauflösende Bilder analysieren und strukturierte Datensatzentwürfe erzeugen — jede Ausgabe braucht jedoch vor Veröffentlichung eine kuratorische Prüfung.

**Müssen Sammlungsdaten die EU verlassen, um GenAI zu nutzen?**

Nein — DSGVO und institutionelle Richtlinien verlangen für Provenienzdaten häufig EU-Datenresidenz, daher lohnt sich neben US-basierten APIs auch die Prüfung von Azure OpenAI, Mistral und anderen EU-gehosteten Optionen.

**Wie groß sollte ein erstes Katalogisierungs-Pilotprojekt sein?**

500–2.000 Objekte mit einigermaßen vollständigen Bestandsdaten — genug, um die Ausgabequalität zu kalibrieren und einen Prüfworkflow aufzubauen, bevor auf die gesamte Sammlung skaliert wird.

Wenn Ihre Institution über gar kein eigenes Tech-Team verfügt, [beginnen Sie hier]({% post_url 2026-09-10-ki-start-kleines-museum-ohne-tech-team %}) mit einem niedrigschwelligeren Einstieg.

---

*Interessiert, wie das für Ihre Institution funktionieren könnte? Ich arbeite mit Museen und Archiven in ganz Deutschland und der DACH-Region zusammen. [Lassen Sie uns sprechen.](https://www.linkedin.com/in/wuthmonehninhlaing/)*
