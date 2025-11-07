# Dashboard-Konzept: Wissensbilanz österreichischer Universitäten

Version: 1.0
Datum: 2025-11-07
Technologie: HTML/CSS/JS (keine Frameworks)
Hosting: GitHub Pages

## Zielsetzung

Interaktives Single-Page Dashboard zur Visualisierung der Wissensbilanz-Daten österreichischer Universitäten (2022-2024) nach dem Information Seeking Mantra:

1. Overview first: Gesamtüberblick aller 22 Universitäten
2. Zoom and filter: Fokus auf spezifische Dimensionen
3. Details on demand: Drill-down zu Einzelwerten

## Zielgruppen

Primäre Nutzer:
- Vizerektorinnen und Vizerektoren (strategische Entscheidungen)
- Universitätsverwaltung (operative Planung)
- Controlling-Abteilungen (Kennzahlen-Monitoring)
- Abteilung I/2 BMBWF (Ministerium, Berichtswesen)

## User Stories

Als Vizerektorin möchte ich die Personalentwicklung meiner Universität im Vergleich zu ähnlichen Universitäten sehen, damit ich Personalstrategien entwickeln kann.

Als Controlling-Mitarbeiter möchte ich Studierendenzahlen nach Studiengruppen filtern, damit ich Kapazitätsplanungen erstellen kann.

Als Abteilungsleiterin I/2 möchte ich schnell auf aggregierte Kennzahlen aller Universitäten zugreifen, damit ich Berichte für das Ministerium erstellen kann.

Als Universitätsverwaltung möchte ich Zeitreihen von 2022 bis 2024 visualisieren, damit ich Trends erkennen kann.

Als Vizerektorin möchte ich Mobilitätskennzahlen nach Kontinenten aufschlüsseln, damit ich Internationalisierungsstrategien planen kann.

## Datenarchitektur

### JSON-Struktur

Initial Load (4 KB):
- docs/data/meta.json: Universitäten-Codex, Dimensionen, Klassifikationen
- docs/data/summary.json: Top-Level KPIs pro Universität (nur 2024-Werte)

Lazy Load (15-50 KB pro Kategorie):
- docs/data/categories/personal.json
- docs/data/categories/studierende.json
- docs/data/categories/neuzulassungen.json
- docs/data/categories/studien.json
- docs/data/categories/abschluesse.json
- docs/data/categories/mobilitaet.json
- docs/data/categories/infrastruktur.json

### Datenquellen-Mapping

| Excel-Dateien | JSON-Kategorie | Dashboard-Komponente |
|---------------|----------------|----------------------|
| 1-A-1 Personal - Köpfe.xlsx | personal.json | Personal-Ansicht |
| 1-A-1 Personal - VZÄ.xlsx | personal.json | Personal-Ansicht |
| Ordentliche Studierende nach Universitäten.xlsx | studierende.json | Studierende-Ansicht |
| Studierende nach Altersklassen.xlsx | studierende.json | Altersklassen-Filter |
| Studierende nach Universitätsreife.xlsx | studierende.json | Universitätsreife-Filter |
| Studierende nach Studiengruppen national.xlsx | studierende.json | Studiengruppen-Filter |
| Studierende nach Herkunftsbundesland.xlsx | studierende.json | Bundesländer-Filter |
| Studierende nach Herkunftskontinent.xlsx | studierende.json | Kontinente-Filter |
| Neuzugelassene Studierende.xlsx | neuzulassungen.json | Neuzulassungen-Ansicht |
| Studien nach Universitäten.xlsx | studien.json | Studien-Ansicht |
| Studienabschlüsse nach Universitäten.xlsx | abschluesse.json | Abschlüsse-Ansicht |
| Incoming-/Outgoing-Studierende.xlsx | mobilitaet.json | Mobilität-Ansicht |
| Gebäudeflächen.xlsx | infrastruktur.json | Infrastruktur-Ansicht |

### Datenfelder

Alle Kategorien enthalten:
- Universitätscode (UA-UW)
- Hierarchische Kategorien (aus Excel-Spalte 3)
- Zeitreihen 2022, 2023, 2024
- Numerische Werte (Float)

summary.json enthält nur 2024-Snapshots für schnellen Überblick:
```json
{
  "UA": {
    "personal_koepfe": 7640.0,
    "studierende": 89234.0
  }
}
```

## Farbkonzept

### Primärfarben (Universitäts-Kategorisierung)

Universitäten werden nach Typ farblich gruppiert:
- Volluniversitäten (UA-UF): #1f77b4 (Blau)
- Technische Universitäten (UG-UI): #ff7f0e (Orange)
- Künstlerische Universitäten (UJ-UM, UK, UL, UO, UQ): #2ca02c (Grün)
- Medizinische Universitäten (US-UU): #d62728 (Rot)
- Spezialisierte Universitäten (UN, UV, UW, UR): #9467bd (Violett)

### Sequentielle Skala (Zeitreihen)

Für Zeitreihen 2022-2024:
- 2022: #deebf7 (Hellblau)
- 2023: #9ecae1 (Mittelblau)
- 2024: #3182bd (Dunkelblau)

### Divergierende Skala (Vergleiche)

Für Abweichungen vom Durchschnitt:
- Überdurchschnittlich: #2ca02c bis #006d2c (Grüntöne)
- Durchschnitt: #f7f7f7 (Grau)
- Unterdurchschnittlich: #fc8d59 bis #d73027 (Rottöne)

### Kategoriale Farben (7 Datenkategorien)

- Personal: #1f77b4 (Blau)
- Studierende: #ff7f0e (Orange)
- Neuzulassungen: #2ca02c (Grün)
- Studien: #d62728 (Rot)
- Abschlüsse: #9467bd (Violett)
- Mobilität: #8c564b (Braun)
- Infrastruktur: #e377c2 (Pink)

### Neutralfarben (UI-Elemente)

- Hintergrund: #ffffff (Weiß)
- Sekundärer Hintergrund: #f8f9fa (Hellgrau)
- Borders: #dee2e6 (Grau)
- Text: #212529 (Dunkelgrau)
- Text sekundär: #6c757d (Mittelgrau)

## Layout-Struktur

### Header (fixiert, 80px)

- Logo/Titel: "Wissensbilanz österreichischer Universitäten"
- Zeitraum-Selektor: 2022 / 2023 / 2024 / Alle
- Kategorie-Navigation: 7 Buttons (Personal, Studierende, Neuzulassungen, Studien, Abschlüsse, Mobilität, Infrastruktur)

### Sidebar (links, 280px, scrollbar)

Filter-Panel:
- Universitäts-Auswahl (22 Checkboxen mit Typ-Gruppierung)
- Dimensions-Filter (kontextabhängig je nach aktiver Kategorie)
- Aggregations-Modus: Summe / Durchschnitt / Median
- Export-Button: CSV / JSON

### Main Content (dynamisch)

3-stufige Ansicht nach Information Seeking Mantra:

Stufe 1 - Overview:
- Karten-Grid aller 22 Universitäten
- Pro Karte: Universitätsname, aktueller Hauptwert, Sparkline (2022-2024)
- Sortierung: Alphabetisch / Nach Wert / Nach Veränderung

Stufe 2 - Zoom and Filter:
- Balkendiagramm der gefilterten Universitäten
- X-Achse: Universitäten
- Y-Achse: Wert der ausgewählten Kategorie
- Tooltips mit Details

Stufe 3 - Details on Demand:
- Tabelle mit vollständigen Daten
- Spalten: Universität, Kategorie, 2022, 2023, 2024, Veränderung absolut, Veränderung relativ
- Sortierbar nach allen Spalten
- In-Place-Editing für Notizen (Local Storage)

### Transitions

Zwischen Stufen:
- Fade-In/Fade-Out: 300ms
- Slide-Up beim Drill-Down: 400ms
- Breadcrumb-Navigation zum Zurückspringen

## Interaktionskonzept

### Navigation

Kategorie-Wechsel:
- Click auf Kategorie-Button in Header
- Lazy Load der entsprechenden JSON-Datei
- Transition zur Overview der Kategorie

Drill-Down:
- Click auf Universitäts-Karte → Zoom to Balkendiagramm
- Click auf Balken → Details-Tabelle
- Breadcrumb: Overview > Filtered > Details

Breadcrumb-Navigation:
- Click auf Breadcrumb-Element springt zurück zur entsprechenden Stufe

### Filterung

Universitäts-Filter:
- Checkboxen mit Typ-Gruppierung
- "Alle auswählen" / "Alle abwählen"
- Mindestens 1 Universität muss ausgewählt sein

Dimensions-Filter:
- Kontext-abhängig:
  - Personal: Nach Personalkategorie (UHSBV-Klassifikation)
  - Studierende: Nach Altersklasse / Universitätsreife / Studiengruppe / Bundesland / Kontinent
  - Neuzulassungen: Nach Studienart (Bachelor/Master/Diplom/Doktorat)
  - Studien: Nach ISCED-F 99 (99 Studienfelder)
  - Abschlüsse: Nach Studienart
  - Mobilität: Nach Programm (Erasmus, Joint Degree, Free Mover)
  - Infrastruktur: Nach Flächentyp
- Multi-Select möglich

Zeitraum-Filter:
- Single-Select: 2022 / 2023 / 2024
- Multi-Select: "Alle" für Zeitreihen

### Aggregation

Client-seitige Berechnung:
- Summe: Für absolute Zahlen (Köpfe, Studierende)
- Durchschnitt: Für Vergleiche zwischen Universitäten
- Median: Für robuste Mittelwerte

Anzeige:
- Hauptwert groß dargestellt
- Aggregationsmodus im Footer angezeigt
- Toggle-Buttons in Sidebar

### Export

CSV-Export:
- Aktuelle Ansicht mit allen Filtern
- Header: Universität, Kategorie, Jahr, Wert
- UTF-8 BOM für Excel-Kompatibilität

JSON-Export:
- Komplette gefilterte Daten
- Struktur identisch zu categories/*.json
- Für Re-Import oder weitere Verarbeitung

## Technische Implementierung

### Stack

- HTML5: Semantische Struktur
- CSS3: Grid, Flexbox, Custom Properties für Theming
- Vanilla JavaScript (ES6+): Keine Frameworks

### Libraries

Erlaubte Libraries:
- D3.js: Für komplexe Visualisierungen (Balkendiagramme, Sparklines)
- Chart.js: Alternative für einfachere Charts
- PapaParse: Für CSV-Export
- Keine UI-Frameworks (React, Vue, Angular verboten)

### Browser-Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Deployment

GitHub Pages:
- Repository: DHCraft/VedMedAI
- Branch: main
- Folder: docs/
- URL: https://dhcraft.github.io/VedMedAI/

Build Process:
- Keine Build-Tools erforderlich (kein Bundler)
- Direkte Bereitstellung von HTML/CSS/JS
- JSON-Dateien statisch gehostet

Cache-Strategie:
- meta.json: Cache 1 Tag
- summary.json: Cache 1 Tag
- categories/*.json: Cache 7 Tage
- Versionierung über Query-Parameter bei Updates

## Wartung und Erweiterung

Daten-Updates:
1. Neue Excel-Dateien in data/ ablegen
2. pre-processing/extract_to_json.py ausführen
3. docs/data/ committen und pushen
4. GitHub Pages aktualisiert automatisch

Neue Kategorien:
1. Kategorie in extract_to_json.py hinzufügen
2. Kategorie-Button in Header ergänzen
3. Lazy-Load-Logik erweitern
4. Filter-Panel anpassen

Neue Dimensionen:
1. meta.json erweitern
2. Dimensions-Filter in Sidebar ergänzen
3. Filter-Logik anpassen

## Offene Punkte

- Design-System finalisieren (Typography, Spacing)
- Icon-Set auswählen (Font Awesome vs. Material Icons vs. Custom SVG)
- Detailliertes Wireframe erstellen
- Prototype in Figma oder direkt als HTML-Mockup
