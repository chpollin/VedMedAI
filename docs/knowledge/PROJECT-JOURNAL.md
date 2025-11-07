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
