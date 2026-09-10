---
layout: article
title: "RAG-Systeme für die Provenienzforschung: Restitutionsarchive durchsuchbar machen"
date: 2026-09-10
categories: ["art-museum"]
tags: ["RAG", "Provenienz", "Archive", "LLM"]
read_time: 7
author: Alex Snow
lang: de
lang_alt: /art-museum/2026/05/08/rag-provenance-research-german-museums/
permalink: /de/artikel/rag-provenienzforschung-deutsche-museen/
excerpt: "Deutschland verwahrt einige der bedeutendsten — und fragmentiertesten — Aufzeichnungen zur NS-Raubkunst. RAG-Systeme lösen nicht die moralische Komplexität der Restitution, aber sie können Jahre archivarischer Recherche auf Wochen verdichten."
---

Deutschland verwahrt einige der bedeutendsten — und fragmentiertesten — Aufzeichnungen zur NS-Raubkunst. Händlerinventare, Auktionskataloge, Transportmanifeste, Korrespondenz zwischen Galerien und Parteifunktionären: Diese Dokumente existieren verstreut über Hunderte Archive, viele nur teilweise digitalisiert, verfasst in epochentypischem Deutsch, das sich gegen die klassische Stichwortsuche sträubt.

RAG-Systeme (Retrieval-Augmented Generation) lösen nicht die moralische Komplexität der Restitution. Aber sie können Jahre archivarischer Recherche auf Wochen verdichten.

<!-- more -->

**Das Wichtigste in Kürze:**

- Provenienzforschung zur NS-Raubkunst scheitert nicht am fehlenden Willen, sondern an der Auffindbarkeit — Aufzeichnungen sind über Archive verstreut, größtenteils gescannt und verweisen nicht aufeinander.
- Ein RAG-System braucht drei Bausteine: Fraktur-fähige OCR und Textzerlegung, semantische (nicht nur stichwortbasierte) Suche, und Antworterzeugung mit Zitatnachweis zur Quelle.
- Semantische Suche erfasst epochentypische Begriffsvarianten (z. B. „Verkauf", „Übergabe" oder „Einlieferung"), die eine Stichwortsuche übersieht.
- RAG liefert Belege — es trifft keine Restitutionsentscheidungen. Diese bleiben Sache menschlicher juristischer und historischer Urteilskraft.

## Warum Provenienzforschung noch immer stockt

Die Washingtoner Prinzipien von 1998 verpflichteten unterzeichnende Staaten — darunter Deutschland — dazu, NS-Raubkunst in öffentlichen Sammlungen zu identifizieren und gemeinsam mit Erben nach gerechten Lösungen zu suchen. Über 25 Jahre später ist der Rückstau weiterhin enorm. Das Deutsche Zentrum Kulturgutverluste in Magdeburg koordiniert einen Großteil dieser Arbeit, doch die eigentliche Recherchelast liegt bei den einzelnen Institutionen mit begrenztem Forschungspersonal.

Das Kernproblem ist nicht der Wille — es ist die Auffindbarkeit.

Ein einzelner Restitutionsanspruch kann es erfordern, folgende Quellen querzuvergleichen:
- Händlerunterlagen von Galerien wie Flechtheim, Cassirer oder Thannhauser
- Transportunterlagen des ERR (Einsatzstab Reichsleiter Rosenberg)
- Auktionskataloge von Lempertz, Dorotheum oder Sotheby's
- Nachkriegsunterlagen der Treuhandverwaltung
- Alliierte Rückgabequittungen des MFA&A (Monuments Men)
- Private Korrespondenz aus dem Nachlass der Künstlerin oder des Künstlers

Diese Quellen sind über Bundesarchiv, Landesarchive, private Stiftungen und internationale Institutionen verstreut. Die meisten liegen als gescannte PDFs vor. Keine spricht mit der anderen.

## Wie RAG in der Praxis konkret aussieht

Ein Retrieval-Augmented-Generation-System für die Provenienzforschung besteht aus drei Komponenten:

**1. Erfassung und Zerlegung.** Gescannte Dokumente durchlaufen OCR (mit Fraktur-Unterstützung — unverzichtbar für Dokumente vor 1945), werden in semantisch kohärente Abschnitte zerlegt und in eine Vektordatenbank eingebettet. Tesseract mit Fraktur-Modellen oder kommerzielle Alternativen wie Azure Document Intelligence übernehmen die OCR-Schicht.

**2. Retrieval.** Wenn eine Forscherin das System befragt — „Finde alle Verweise auf Paul Cassirer und die Sammlung Liebermann zwischen 1933 und 1939" —, ruft das System die relevantesten Dokumentfragmente über den gesamten Bestand hinweg per semantischer Ähnlichkeit ab, nicht nur per Stichwortsuche. So werden auch Verweise erfasst, wenn die Terminologie variiert (derselbe Vorgang kann in unterschiedlichen Dokumenten als „Verkauf", „Übergabe" oder „Einlieferung" bezeichnet sein).

**3. Antworterzeugung mit Zitatnachweis.** Das LLM verdichtet abgerufene Fragmente zu einer strukturierten Antwort — mit Verweisen auf Quelldokument, Seite und Archiv. Die Forscherin kann jede Aussage gegen das Originalscan prüfen. Das ist nicht verhandelbar: Das Halluzinationsrisiko bedeutet, dass kein Provenienzbefund allein auf einer Modellausgabe beruhen darf.

## Ein konkretes Beispiel

Stellen Sie sich ein Regionalmuseum im Rheinland vor, das ein Ölgemälde aus der Mitte des 19. Jahrhunderts mit einer Lücke in der Besitzgeschichte zwischen 1933 und 1948 verwahrt. Eine Forscherin, die ein RAG-System über einen Bestand digitalisierter Händlerunterlagen, ERR-Dokumentation und Nachkriegsansprüche nutzt, könnte:

1. Anfragen: *„Alle Unterlagen, die [Werktitel] oder [Künstlername] in Händlerinventaren oder Übertragungsdokumenten 1933–1945 erwähnen"*
2. Abrufen: Drei Fundstellen — einen ERR-Inventareintrag von 1942, einen Lempertz-Katalogeintrag von 1943 und eine alliierte Rückgabequittung von 1946
3. Verdichten: Eine strukturierte Provenienz-Zeitleiste mit Quellenangaben für jeden Schritt
4. Identifizieren: Die wahrscheinliche Verlagerungskette — und die Familie, deren Anspruch geprüft werden sollte

Ohne das System könnte dieselbe Recherche Monate manueller Archivbesuche in Anspruch nehmen. Damit lässt sich derselbe Rechercheumfang in Tagen bewältigen — Zeit, die die Forscherin stattdessen in Interpretation und Verifikation investieren kann, statt in Dokumentenrecherche.

## Praktische Erwägungen beim Aufbau

**Fraktur-OCR-Qualität ist der Engpass.** Deutsche Dokumente vor 1941 verwenden Frakturschrift, mit der Standard-OCR-Engines schlecht zurechtkommen. Planen Sie ausreichend Zeit für die Qualitätsbewertung der OCR und Korrekturpipelines vor der Indexierung ein.

**Auf Ebene der Dokumenteinheit zerlegen, nicht der Seite.** Ein einzelner Inventareintrag kann sich über mehrere Seiten erstrecken, oder eine einzelne Seite kann mehrere unabhängige Einträge enthalten. Semantische Zerlegung — entlang logischer Dokumentgrenzen — verbessert die Retrieval-Präzision deutlich.

**Metadaten-Filterung ist ebenso wichtig wie semantische Suche.** Jedes Fragment sollte strukturierte Metadaten tragen: Archiv, Dokumenttyp, Zeitraum, Ursprungsinstitution. Forschende müssen sowohl nach Quellenart filtern können („zeige mir nur ERR-Unterlagen") als auch inhaltlich abfragen.

**Der deutsche Rechtsrahmen bestimmt, was gespeichert werden darf.** Personenbezogene Daten in Archivunterlagen — Namen, Adressen, finanzielle Details — unterliegen selbst in historischen Dokumenten der DSGVO. Eine rechtliche Prüfung der Datenverarbeitungsvereinbarungen mit den ursprünglichen Archiven ist vor der Erfassung unerlässlich.

**Provenienzspezifisches Feintuning hilft.** Generische LLMs sind nicht auf epochentypisches deutsches Verwaltungsdeutsch trainiert. Few-Shot-Beispiele korrekt formatierter Provenienzzusammenfassungen plus ein kontrolliertes Vokabular epochentypischer Terminologie verbessern die Ausgabequalität erheblich.

## Was das nicht ersetzt

RAG liefert Belege. Es trifft keine juristischen Entscheidungen, bewertet nicht die Glaubwürdigkeit konkurrierender Ansprüche und wägt keine moralischen Argumente ab. Die Entscheidungen zur Restitution — wem was gehört, was eine „faire und gerechte Lösung" im Einzelfall bedeutet — bleiben fest in der Domäne menschlicher Urteilskraft, juristischer Expertise und Verhandlung.

Was die Technologie leistet, ist Forschenden und Institutionen die Fähigkeit zu geben, die Belege zu finden, die diese Urteile erst möglich machen. In einem Bereich, in dem Gerechtigkeit über 80 Jahre lang auch deshalb aufgeschoben wurde, weil die Archive unzugänglich waren, zählt das.

## Häufig gestellte Fragen

**Kann KI Restitutionsentscheidungen für Raubkunst treffen?**
Nein. RAG-Systeme finden und zitieren relevante Belege aus Archiven, aber juristische Entscheidungen, Glaubwürdigkeitsbewertungen und Verhandlungen über eine „faire und gerechte Lösung" bleiben vollständig Sache menschlicher Urteilskraft.

**Warum ist Fraktur-OCR für die Provenienzforschung wichtig?**
Die meisten deutschen Dokumente vor 1945 verwenden Frakturschrift, mit der Standard-OCR schlecht zurechtkommt. Zeit für Fraktur-fähige OCR — etwa Tesseracts Fraktur-Modelle — und Qualitätskorrektur einzuplanen ist vor der Indexierung von Archiven unerlässlich.

**Wie unterscheidet sich RAG von der Stichwortsuche bei der Archivrecherche?**
RAG sucht per semantischer Ähnlichkeit und erfasst dadurch auch Verweise bei unterschiedlicher Terminologie — derselbe Vorgang kann in verschiedenen Dokumenten als „Verkauf", „Übergabe" oder „Einlieferung" erscheinen —, was eine Stichwortsuche übersehen würde.

**Um wie viel schneller ist RAG-gestützte Provenienzforschung im Vergleich zu manueller Archivarbeit?**
Recherchen, die Monate manueller Archivbesuche erfordern könnten, lassen sich oft in Tagen bewältigen — Zeit, die Forschende dann in Interpretation und Verifikation statt in Dokumentenrecherche investieren können.

Dieser Beitrag ist Teil eines größeren Musters — siehe auch, [wie GenAI die Sammlungskatalogisierung]({% post_url 2026-09-10-ki-museumssammlung-katalogisierung %}) grundlegender verändert.

---

*Ich arbeite mit Museen und Archiven in ganz Deutschland an praktischer KI-Infrastruktur für Sammlungsforschung und Barrierefreiheit. Wenn Ihre Institution auf digitalisierten Archiven sitzt, die niemand effektiv durchsuchen kann, [lassen Sie uns sprechen.](https://www.linkedin.com/in/wuthmonehninhlaing/)*
