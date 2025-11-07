# PROJECT JOURNAL

## 2025-11-07 Session 1

Analyse von 59 Excel-Dateien (Wissensbilanz österreichischer Universitäten)
Erstellung vollständiger Dokumentation
Projekt-Strukturierung

Dateien erstellt:
- pre-processing/analyze.py (3 Modi: overview, structure, deep)
- pre-processing/data_structure.json
- pre-processing/data_deep_analysis.json
- pre-processing/README.md
- docs/knowledge/DATA.md (vollständige Datendokumentation aller 59 Dateien)
- docs/knowledge/PROJECT-JOURNAL.md (dieses Journal)
- CLAUDE.md (Arbeitsregeln im Root)

Commits:
- Initial commit (70 Dateien)

Datenstruktur identifiziert:
- 20 Universitäten (UA-UU)
- Zeitraum 2022-2024
- 7 Kategorien: Personal (15), Studierende (8), Neuzulassungen (8), Studien (14), Abschlüsse (2), Mobilität (3), Infrastruktur (1)
- Wissensbilanz-Kennzahlen 1.A.1 bis 1.A.5
- Klassifikationen: UHSBV, WBV, ISCED, ISCED-F 99, UG

Python-Scripts konsolidiert:
- 3 Scripts zu analyze.py zusammengeführt
- Argparse-Interface mit 4 Modi (overview, structure, deep, all)

## 2025-11-07 Session 2

Dashboard-Vorbereitung
Excel-to-JSON Konvertierung für GitHub Pages

Dateien erstellt:
- pre-processing/extract_to_json.py
- docs/data/meta.json (Codex, Dimensionen, Klassifikationen)
- docs/data/summary.json (Top-Level KPIs)
- docs/data/categories/personal.json (15 KB)
- docs/data/categories/studierende.json

Datenstruktur:
- Hybrid-Ansatz: meta.json + summary.json + Kategorie-JSONs
- Lazy Loading möglich
- Initial Load: 60-110 KB
- Kategorie-spezifisch: +100-200 KB

Excel-Parsing:
- Header-Erkennung: Zeile mit "Universität (Codex)"
- Datenextraktion: Universitätscode aus Spalte 1
- Hierarchische Kategorien aus Spalte 3
- Werte aus Spalten 4+ (Zeitreihen 2022-2024)

## 2025-11-07 Session 3

Dashboard-Konzeption
CONCEPT.md vollständig überarbeitet

Dateien erstellt:
- docs/knowledge/CONCEPT.md (Dashboard-Konzept mit allen Spezifikationen)

Überarbeitungen:
- Alle Emojis entfernt (CLAUDE.md-Konformität)
- Datengetriebenes Farbkonzept definiert (5 Paletten: Primär, Sequentiell, Divergierend, Kategorial, Neutral)
- 5 User Stories hinzugefügt (Vizerektorin, Controlling, Abteilungsleiterin, Verwaltung)
- Datenquellen-Mapping: 59 Excel-Dateien zu 7 JSON-Kategorien
- Technische Constraints dokumentiert (HTML/CSS/JS, keine Frameworks, GitHub Pages)
- 3-stufige Ansicht nach Information Seeking Mantra spezifiziert
- Performance-Ziele: Initial Load 4 KB, Lazy Load 15-50 KB pro Kategorie
- WCAG 2.1 Level AA Accessibility-Anforderungen
- Responsive Design für Desktop/Tablet/Mobile

Farbkonzept:
- Primärfarben: 5 Universitätstypen (Voll, Technisch, Künstlerisch, Medizinisch, Spezialisiert)
- Sequentielle Skala: 3 Blautöne für Zeitreihen 2022-2024
- Divergierende Skala: Grün-Grau-Rot für Abweichungen vom Durchschnitt
- Kategoriale Farben: 7 Farben für Datenkategorien
- Neutralfarben: UI-Elemente

Revision 2:
- Accessibility-Anforderungen entfernt
- Responsive-Design-Spezifikationen entfernt
- Performance-Metriken entfernt
- Fokus auf funktionale Spezifikation

## 2025-11-07 Session 4

MVP Dashboard implementiert
Single-Page-Application mit HTML/CSS/JS

Dateien erstellt:
- docs/index.html (Dashboard-Interface)
- docs/styles.css (Styling mit CSS Custom Properties)
- docs/app.js (Vanilla JavaScript, keine Frameworks)

Features:
- Initial Load: meta.json + summary.json (4 KB)
- Overview: 22 Universitäts-Karten mit Personal-Köpfen 2024
- Lazy Load: personal.json beim Click auf Karte
- Detail-View: Tabelle mit Zeitreihen 2022-2024 pro Kategorie
- Filterung: Universitäts-Auswahl nach Typ (Voll, Tech, Kunst, Med, Special)
- Aggregation: Summe / Durchschnitt / Median (UI vorbereitet)
- Sortierung: Alphabetisch / Nach Wert / Nach Veränderung
- Export: CSV / JSON
- Breadcrumb-Navigation: Übersicht > Detail

Layout:
- Header: 140px (Titel, Jahr-Selektor, Kategorie-Navigation)
- Sidebar: 280px (Filter-Panel)
- Main Content: Responsive Grid (280px Cards)

Farbkonzept umgesetzt:
- 5 Universitätstypen mit Primärfarben
- Sequentielle Skala für Sparklines
- Neutralfarben für UI

Status:
- Personal-Kategorie funktional
- Studierende-Kategorie disabled (JSON-Parsing noch fehlerhaft)
- 5 weitere Kategorien disabled (JSONs noch nicht erstellt)

Nächste Schritte:
- Dashboard lokal testen
- studierende.json Parsing beheben
- Restliche 5 Kategorie-JSONs implementieren
