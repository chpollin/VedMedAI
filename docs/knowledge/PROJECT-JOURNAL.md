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

Commits:
- MVP Dashboard (5 Dateien, 1311 Zeilen)

Test:
- Dashboard lokal funktional
- Alle Features getestet und funktionieren
- Export CSV/JSON erfolgreich

Nächste Schritte:
- studierende.json Parsing beheben
- Restliche 5 Kategorie-JSONs implementieren
- GitHub Pages deployen

## 2025-11-07 Session 5

Datenaufbereitung Phase 1 abgeschlossen
Alle Kategorie-JSONs erstellt und summary.json erweitert

Dateien aktualisiert:
- pre-processing/extract_to_json.py (read_name_based_file Funktion hinzugefügt)
- docs/data/summary.json (7 KPIs pro Uni: personal_koepfe, studierende, neuzulassungen, studien, abschluesse, mobilitaet, infrastruktur)
- docs/data/categories/studierende.json (3,2 KB)
- docs/data/categories/neuzulassungen.json (3,3 KB)
- docs/data/categories/studien.json (3,5 KB)
- docs/data/categories/abschluesse.json (3,7 KB)
- docs/data/categories/mobilitaet.json (2,9 KB)
- docs/data/categories/infrastruktur.json (2 Bytes - leer)

Parsing-Verbesserungen:
- read_name_based_file: Generische Funktion für Name-zu-Code Mapping
- Frauen/Männer/Gesamt Spalten-Erkennung
- Anwendung auf studierende, neuzulassungen, studien, abschluesse, mobilitaet

Status:
- personal.json: 185 KB (koepfe + vzae, vollständig)
- studierende.json: 3,2 KB (nur gesamt-Werte, zeitreihe/altersklassen/universitaetsreife/bundeslaender fehlen)
- neuzulassungen.json: 3,3 KB (nur gesamt-Werte)
- studien.json: 3,5 KB (nur gesamt-Werte)
- abschluesse.json: 3,7 KB (nur gesamt-Werte)
- mobilitaet.json: 2,9 KB (nur gesamt-Werte)
- infrastruktur.json: leer (Nutzfläche-Excel hat andere Struktur)

summary.json: 176 Zeilen, 22 Universitäten mit 6-7 KPIs

Dashboard-Integration:
- docs/index.html: 6 Kategorie-Buttons aktiviert (personal, studierende, neuzulassungen, studien, abschluesse, mobilitaet)
- docs/app.js: Erweiterte Funktionen für alle Kategorien
  - createUniversityCard: categoryConfig für alle 7 Kategorien
  - sortUniversities: categoryKeys für alle 7 Kategorien
  - renderDetailView: Generische Tabellen-Ausgabe für alle Kategorien (Frauen/Männer/Gesamt)
- Infrastruktur-Button bleibt disabled (JSON leer)

Dokumentation:
- pre-processing/README.md aktualisiert (alle 7 Kategorie-JSONs dokumentiert)

Status:
- Phase 1 abgeschlossen: Alle Kategorie-JSONs erstellt
- Phase 2 teilweise: Dashboard-Integration für 6 Kategorien funktional
- Nächste Schritte:
  - infrastruktur.json Parsing fixen
  - Dashboard lokal testen
  - Commit und Push

## 2025-11-07 Session 6

Design-System Phase 1: CSS Design-Tokens und Font Awesome Integration

Dateien aktualisiert:
- docs/index.html (Font Awesome 6 CDN, Icons in Kategorie-Tabs)
- docs/styles.css (komplettes Design-Token-System, 70 Variablen)
- docs/app.js (uniTypeIcons mapping, Icons in Filter und Karten)

CSS Design-Tokens implementiert:
- Neutral-Palette: 9 Stufen (0-900) für UI-Elemente
- Primary-Palette: 6 Stufen + Akzentfarben (success, danger, warning)
- Uni-Typen: 5 kategoriale Farben (voll, tech, kunst, med, special)
- Sequenzielle Skala: 3 Blautöne für Zeitreihen 2022-2024
- Divergierende Skala: 7 Stufen Grün-Grau-Rot für Abweichungen
- Kategorie-Farben: 7 Farben für Datenkategorien
- Typografie-Tokens: font-family, 6 Größen
- Spacing-Tokens: 6 Stufen (xs-xxl)
- Radius-Tokens: card, button

Font Awesome 6 Icons integriert:
- Kategorie-Tabs: fa-users, fa-user-graduate, fa-user-plus, fa-book, fa-certificate, fa-plane, fa-building
- Uni-Typen: fa-university, fa-microchip, fa-palette, fa-user-md, fa-graduation-cap
- Filter-Checkboxen: Icons mit Typ-Farbe
- Universität-Karten: Typ-Badge mit Icon und Label

Sparklines-Farben angepasst:
- Sequenzielle Blau-Skala statt uniforme Opacity
- sparkline-bar:nth-child(1): seq-2022
- sparkline-bar:nth-child(2): seq-2023
- sparkline-bar:nth-child(3): seq-2024

Dateigröße:
- index.html: 95 Zeilen
- styles.css: 501 Zeilen (vorher 430)
- app.js: 529 Zeilen (vorher 520)

Status:
- DESIGN.md Phase 1 abgeschlossen
- Font Awesome 6 CDN funktional
- Design-Tokens konsistent in allen Dateien
- JavaScript-Syntax validiert
- Nächste Schritte: Phase 2 (Sparklines mit einheitlicher y-Skala)

## 2025-11-07 Session 7

Design-System Phase 1 Revision: Interface professionalisiert

Dateien aktualisiert:
- docs/app.js (Karten-HTML vereinfacht, Filter-Icons entfernt)
- docs/styles.css (KPI-Hierarchie verstärkt, Typ-Icon neutral)

Änderungen Universität-Karten:
- Typ-Badge entfernt: nur Icon (neutral-400), kein farbiger Badge mehr
- Uni-Code entfernt: redundant, bringt keinen Mehrwert
- KPI-Wert größer: 48px statt 32px, line-height: 1
- Label kleiner: 12px statt 14px, uppercase, letter-spacing
- Sparklines entfernt: Platzhalter-Daten nicht sinnvoll, bis Phase 2

Änderungen Filter-Sidebar:
- Filter-Icons entfernt: nur Farbindikator + Name
- Weniger visuelles Rauschen

Begründung:
- Kognitive Ökonomie: neutrale UI, Fokus auf Daten-Werte
- Perzeptuelle Hierarchie: KPI dominiert, Label sekundär
- Sparklines erst mit echten Daten + einheitlicher y-Skala sinnvoll
- Farbige Badges konkurrierten mit Daten-Visualisierung

Vorher:
- Typ-Badge farbig mit Icon + Text
- Uni-Code rechts oben
- KPI 32px, Label 14px
- Sparklines mit unterschiedlichen Höhen
- Filter mit Farbindikator + Icon + Text

Nachher:
- Typ-Icon grau, Tooltip mit Label
- Kein Uni-Code
- KPI 48px, Label 12px uppercase
- Keine Sparklines
- Filter mit Farbindikator + Text

Status:
- Phase 1 Revision abgeschlossen
- Interface professioneller, weniger überladen
- Nächste Schritte: Phase 2 (echte Sparkline-Daten mit einheitlicher y-Skala)
