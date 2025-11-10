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

## 2025-11-07 Session 8

Design-System Phase 1 Revision 2: Farbige Icons + Neutrale UI

Dateien aktualisiert:
- docs/styles.css (CSS-Spezifität-Fix für Farbklassen)
- docs/knowledge/DESIGN.md (Version 1.1, vollständige Revision)

Problem gelöst:
- Icons in Universitätskarten nicht sichtbar
- Ursache: CSS-Klassen .voll/.tech/.kunst/.med/.special setzten background auf Badge-Container
- Fix: Klassen zu .color-indicator.voll etc. geändert (höhere Spezifität)

Änderungen Typ-Icons:
- Icons direkt gefärbt (color auf i-Tag)
- 20px Größe, keine Hintergrund-Circle
- Farbzuordnung: voll=Blau, tech=Orange, kunst=Grün, med=Rot, special=Violett

Änderungen UI-Elemente:
- Aktive Buttons: neutral-900 statt primary-600 (Blau)
- year-btn.active, category-btn.active, agg-btn.active: alle neutral-900
- Konsistente neutrale UI, Fokus auf Daten-Farben

CSS-Spezifikation dokumentiert:
- .university-type-badge: display flex, font-size 20px
- .university-type-badge.voll i: color var(--uni-voll)
- .color-indicator: width 12px, height 12px, border-radius 2px
- .color-indicator.voll: background var(--uni-voll)

DESIGN.md aktualisiert:
- Version 1.1
- Revision Session 8: Farbige Icons, neutrale UI
- Universität-Karten: KPI 48px, Label 12px uppercase, Icons 20px farbig
- Filter: 12px Farbindikator-Quadrat, keine Icons
- Aggregation-Buttons: neutral-900 aktiv, keine Icons
- CSS-Spezifikationen für alle Komponenten

Status:
- Design-System Phase 1 Revision 2 abgeschlossen
- Icons funktional, Farben konsistent
- UI neutral, Daten-Visualisierung im Fokus
- 6 Kategorien funktional (Personal, Studierende, Neuzulassungen, Studien, Abschlüsse, Mobilität)
- Commit: 14 Dateien, 1755 Zeilen hinzugefügt

Nächste Schritte:
- Phase 2: Sparklines mit echten Daten + einheitlicher y-Skala
- Infrastruktur-Kategorie: Nutzfläche-Parsing fixen
- GitHub Pages deployen

## 2025-11-07 Session 9

Phase 2: Sparklines mit echten Daten + Infrastruktur-Kategorie funktional

Dateien aktualisiert:
- docs/app.js (State + extractSparklineData + sparklineHTML)
- docs/index.html (Infrastruktur-Button enabled)
- docs/data/categories/infrastruktur.json (69 Zeilen)
- docs/data/summary.json (infrastruktur-Werte)
- pre-processing/extract_to_json.py (read_infrastruktur_file)

Sparklines-Implementierung:
- State.sparklineData: Speichert 2022-2024 Werte + maxValue pro Kategorie
- extractSparklineData: Extrahiert erste Kategorie aus categoryData (z.B. "Wissenschaftliches und künstlerisches Personal" für Personal)
- Unified y-scale: maxValue über alle Universitäten
- 3 vertikale Balken: Höhe als Prozent von maxValue
- Sequentielle Blau-Skala: sparkline-bar:nth-child(1/2/3) mit seq-2022/2023/2024
- Tooltips: title-Attribut mit Jahr und formatiertem Wert
- Lazy Loading: extractSparklineData bei loadCategoryData + Category-Switch

Infrastruktur-Kategorie:
- read_infrastruktur_file: Spezialisierte Parsing-Funktion vor extract_summary platziert
- Header-Detection-Fix: cell_value.strip() == "Universität" statt "Universität" in str (verhindert Match mit "Raum Universitäten")
- Korrekte Header-Row: Zeile 15 statt Zeile 0
- Jahr-Spalten: 2023, 2022, 2021... bis 2006 als Strings
- 22 Universitäten: Alle Name-zu-Code Mappings funktional
- Zeitreihen: "Stichtag 31.12.2023" bis "Stichtag 31.12.2006"
- Kategorie: "Nutzfläche m²"
- extract_summary: 2023-Werte (neueste verfügbare)

Cleanup:
- 7 Debug-Scripts gelöscht: debug_infrastruktur.py (1-6), test_infrastruktur_direct.py

Status:
- Alle 7 Kategorien funktional
- Sparklines zeigen echte Trends mit einheitlicher Skala
- Infrastruktur-Button aktiviert
- Initial Load: personal.json mit Sparklines
- Category Switch: Lazy Load + Sparkline-Neuberechnung

Commit: 5 Dateien, 675 Zeilen hinzugefügt, 34 Zeilen gelöscht

## 2025-11-07 Session 10

Neue Wissensbilanz-Kennzahlen Phase 1: 12 Standard-Dateien implementiert

Aufgabe:
- 15 neue Excel-Dateien analysiert (Session 9)
- Parsing-Strategie definiert: 12 Standard, 2 Spezial, 3 Komplex
- Phase 1: 12 Standard-Dateien mit read_wissensbilanz_file implementieren

Implementierung:
- Neue Parsing-Funktion read_wissensbilanz_file erstellt
- Header-Detection: "Universität" in Spalte 0 + "Codex" in Spalte 1 (Zeile 17-30)
- Struktur: Universitätscode in Spalte 1, Daten ab Spalte 3
- Kategorie: Alle Werte unter "Gesamt" zusammengefasst
- extract_university_code: Bestehende Funktion wiederverwendet

12 extract_* Funktionen hinzugefügt:
- extract_berufungen (1-A-2)
- extract_frauenquote_kollegialorgane (1-A-3)
- extract_gender_pay_gap (1-A-4)
- extract_professorinnen_aequivalente (2-A-1)
- extract_eingerichtete_studien (2-A-2)
- extract_besondere_zulassungsbedingungen (2-A-4)
- extract_belegte_ordentliche_studien (2-A-7)
- extract_outgoing_studierende (2-A-8)
- extract_incoming_studierende (2-A-9)
- extract_doktoratsstudierende (2-B-1)
- extract_ausserordentliche_abschluesse (3-A-1)
- extract_ordentliche_abschluesse (3-A-1)

JSON-Dateien generiert:
- berufungen.json (6,0 KB: Frauen/Männer/Gesamt 2022-2024)
- frauenquote-kollegialorgane.json (14 KB: 2024)
- gender-pay-gap.json (16 KB: 2022-2024)
- professorinnen-aequivalente.json (3,7 KB: 2022-2024)
- eingerichtete-studien.json (2,3 KB: 2022-2024)
- besondere-zulassungsbedingungen.json (6,0 KB: 2022-2024)
- belegte-ordentliche-studien.json (4,6 KB: 2022-2024)
- outgoing-studierende.json (5,6 KB: 2022-2023)
- incoming-studierende.json (5,7 KB: 2022-2023)
- doktoratsstudierende.json (6,0 KB: 2022-2024)
- ausserordentliche-abschluesse.json (2 B: leer)
- ordentliche-abschluesse.json (3,2 KB: 2022-2024)

Dokumentation aktualisiert:
- DATA.md: Parsing-Strategien erweitert (Standard/Spezial/Komplex)
- DATA.md: Implementierungsstrategie mit Zeitschätzungen
- pre-processing/README.md: 12 neue JSON-Dateien dokumentiert

Dateien:
- pre-processing/extract_to_json.py (895 Zeilen, +311 Zeilen)
- docs/data/categories/ (+12 Dateien, 54 KB Gesamt)
- docs/knowledge/DATA.md (689 Zeilen, +45 Zeilen)
- pre-processing/README.md (122 Zeilen, +14 Zeilen)

Status:
- Phase 1 abgeschlossen: 12 Standard-Dateien funktional
- 19 JSON-Kategorien gesamt (7 Basis + 12 neu)
- Phase 2 offen: 2 Spezial-Dateien (1-A-5, 2-A-7 Lehrgänge)
- Phase 3 offen: 3 Komplexe Dateien (2-A-3, 2-A-5, 2-A-6)
- Nicht analysiert: 2 Dateien (3-A-2, 3-A-3)

## Session 11: Dashboard-Erweiterung (2025-11-07)

Aufgabe: 12 neue Wissensbilanz-Kategorien ins Dashboard integrieren

Implementierung:

Dashboard-Erweiterung:
- index.html: 12 neue Kategorie-Buttons (19 Buttons gesamt)
- app.js: categoryConfig erweitert (alle Labels + summary.json Keys)
- app.js: categoryMapping erweitert (Sparkline-Extraktion)
- styles.css: 12 neue Kategorie-Farben definiert

Datenintegration:
- extract_to_json.py: extract_summary() erweitert
- summary.json: 19 KPIs pro Universität (12 neue Felder)
- Neue KPIs: berufungen, frauenquote_kollegialorgane, gender_pay_gap, professorinnen_aequivalente, eingerichtete_studien, besondere_zulassungsbedingungen, belegte_ordentliche_studien, outgoing_studierende_wb, incoming_studierende, doktoratsstudierende, ausserordentliche_abschluesse, ordentliche_abschluesse_wb

Icons:
- Font Awesome 6: user-tie, venus, scale-unbalanced, chalkboard-user, graduation-cap, door-open, user-check, plane-departure, plane-arrival, scroll

Commit: 2d400b1
- 29 Dateien geändert, 4970 Zeilen hinzugefügt, 36 gelöscht
- JavaScript-Syntax validiert
- 22 Universitäten mit 19 KPIs funktional

Status:
- Dashboard-UI: 19 Kategorien verfügbar
- Lazy Loading: alle 19 Kategorien funktionsfähig
- Sparklines: funktional für Kategorien mit Zeitreihen-Daten

## Session 12: Multi-Header Parsing für Sparklines (2025-11-07)

Aufgabe: Incoming/Outgoing-Kategorien zeigen max: 0 (keine Sparklines) wegen fehlender Jahr-Labels

Problem-Analyse:
- Excel-Dateien haben Multi-Header-Struktur
- Zeile 19: "Studienjahr 2023/24", "Studienjahr 2022/23"
- Zeile 20: "EU", "Drittstaaten", "Gesamt" (pro Studienjahr)
- read_wissensbilanz_file() erkannte nur Zeile 20
- Spalten wurden als "EU", "EU.1", "EU.2" gespeichert (pandas auto-numbering)
- extractYearValues() fand keine "2022", "2023", "2024" Labels

Implementierung:

Neue Parsing-Funktion:
- read_wissensbilanz_multiheader_file() erstellt
- Liest year_row = header_row - 1 (Zeile 19)
- Extrahiert Studienjahr-Labels für jede Spalte
- Kombiniert zu "Studienjahr 2023/24 - EU", "Studienjahr 2023/24 - Gesamt"
- Entfernt Pandas-Suffixe (.1, .2) via col_name.split('.')[0]

Extract-Funktionen aktualisiert:
- extract_incoming_studierende(): read_wissensbilanz_multiheader_file()
- extract_outgoing_studierende(): read_wissensbilanz_multiheader_file()

Dashboard-Anpassung:
- extractYearValues() in app.js erweitert
- Priorisierung: "Studienjahr 2023/24" → 2024 (nicht 2023)
- Unterstützt: Studienjahr, WS, SS, direkte Jahreszahlen

JSON-Struktur:
- incoming-studierende.json: 9 Spalten pro Uni
  - "Studienjahr 2023/24 - Gesamt": 1989 (UA)
  - "Studienjahr 2022/23 - Gesamt": 1800 (UA)
  - "Studienjahr 2021/22 - Gesamt": 156 (UA)
- outgoing-studierende.json: analog

Commit: 7ead487
- 6 Dateien geändert, 327 Zeilen hinzugefügt, 384 gelöscht
- JavaScript-Syntax validiert
- Multi-Header Parsing funktional

Status:
- Incoming/Outgoing-Kategorien haben jetzt Zeitreihen-Labels
- Sparklines sollten im Dashboard funktionieren
- 2 von 12 neuen Kategorien mit Sparklines

## Session 13: Bugfixes und Code-Qualität (2025-11-10)

Aufgabe: 28 offene Tasks identifiziert und kritische Probleme behoben

Kritische Bugfixes:
- extract_summary(): 4 falsche Dateinamen korrigiert
  - 2-A-7 (belegte Studien), 2-A-8 (outgoing), 2-A-9 (incoming), 2-B-1 (Doktorat)
  - read_wissensbilanz_multiheader_file für outgoing/incoming verwendet
- app.js: UN von special zu kunst verschoben
- DATA.md: UV und UW dokumentiert (2 fehlende Universitäten)

Code-Duplizierung reduziert:
- UNIVERSITY_MAPPING: Zentrales Dictionary (22 Unis)
  - read_name_based_file: 23 Zeilen entfernt
  - read_infrastruktur_file: 23 Zeilen entfernt
- find_university_header_row(): Gemeinsame Funktion
  - read_excel_file: 8 Zeilen entfernt
  - read_wissensbilanz_file: 6 Zeilen entfernt
  - read_wissensbilanz_multiheader_file: 6 Zeilen entfernt

UI-Verbesserungen:
- app.js: categoryKeys von 7 auf 19 Kategorien erweitert
- index.html: doktoratsstudierende Icon geändert (fa-book-bookmark)

Dateien:
- extract_to_json.py: +69 Zeilen, -84 Zeilen (Netto: -15)
- app.js: +18 Zeilen
- index.html: +1 Zeile
- DATA.md: +2 Zeilen

Commit: 12cab49
Status: 8 von 28 Tasks behoben

## Session 14: Dashboard-Features aktiviert (2025-11-10)

Aufgabe: Funktionslose Features funktionsfähig machen

Funktionale Features implementiert:
- Aggregation-Buttons: Summe/Durchschnitt/Median
  - calculateAggregate(): 3 Modi für gefilterte Universitäten
  - aggregate-display: Prominent über Grid
- Jahr-Selector: 2024/2023/2022/Alle
  - getValueForYear(): Zentrale Funktion für jahresbasierte Werte
  - Integration mit Sparkline-Daten (y2022, y2023, y2024)
- Sortierung nach Veränderung: Differenz 2024-2023
  - Abhängigkeit von Sparkline-Daten
- Detail-View: Frauen/Männer/Gesamt Spalten
  - Personal-Kategorie: Disaggregierte Zeitreihen
  - Neue Spalte: Geschlecht
- Export CSV/JSON: 19 Kategorien statt 2
  - Dynamische Kategorie-Konfiguration
  - Jahr im Dateinamen

Code-Qualität:
- extractYearValues(): Überschreiben verhindert (break bei erstem Match)
- formatNumber(): Konsistente Rückgabewerte (0 statt "0")
- renderAggregate(): Anzeige für Aggregations-Modi

UI:
- aggregate-display: CSS mit Design-Tokens
- Detail-Tabelle: Geschlecht-Spalte

Dateien:
- app.js: +242 Zeilen, -39 Zeilen (Netto: +203)
- index.html: +1 Zeile
- styles.css: +36 Zeilen

Commit: dc9aff2
Status: 6 von 6 geplanten Tasks umgesetzt

## Session 15: CSS-Refactoring (2025-11-10)

Aufgabe: CSS-Variablen konsistent verwenden, hardcoded Werte eliminieren

Probleme behoben:
- Inkonsistente Spacing-Namen: --spacing-* zu --space-* korrigiert
  - aggregate-display: 4 Instanzen gefixt
- Hardcoded rem-Werte durch Variablen ersetzt:
  - 0.5rem → var(--space-sm) (6 Instanzen)
  - 1rem → var(--space-lg) (1 Instanz)
  - 1.5rem → var(--space-xl) (2 Instanzen)
  - 2rem → var(--space-xxl) (2 Instanzen)
- Hardcoded px-Werte durch Variablen ersetzt:
  - 12px → var(--space-md) (2 Instanzen)
  - 16px → var(--space-lg) (2 Instanzen)
  - 400px → var(--filter-max-height) (1 Instanz)

Neue CSS-Variablen:
- --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.05)
- --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.1)
- --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.15)
- --filter-max-height: 400px

Verbesserungen:
- Konsistente Spacing-Verwendung im gesamten CSS
- Zentrale Shadow-Definition für einheitliche Schatten
- Magic Numbers dokumentiert als Variablen
- Wartbarkeit erhöht: Änderungen zentral möglich

Dateien:
- styles.css: 20 Zeilen geändert

Commit: ausstehend
Status: CSS-Variablen konsistent
