# ARCHITECTURE - System-Architektur

Version: 1.0
Datum: 2025-11-07
Basis: 74 Excel-Dateien, Dashboard MVP, 7 Kategorie-JSONs

## DATENFLUSS

```
Excel (data/)
  -> Python Parsing (pre-processing/extract_to_json.py)
    -> JSON (docs/data/)
      -> JavaScript (docs/app.js)
        -> HTML (docs/index.html)
```

### 1. Excel → Python (Parsing)

Input: 74 Excel-Dateien
Output: JSON-Dateien (meta, summary, 7 categories)

Script: pre-processing/extract_to_json.py

Parsing-Funktionen:
- read_excel_file: Standard-Struktur (Universitätscode Spalte 1, Kategorien Spalte 3, Zeitreihen in Spalten)
- read_name_based_file: Name-basiert (Universitätsname Spalte 0, Frauen/Männer/Gesamt Spalten)
- read_infrastruktur_file: Spezial (Universitätsname Spalte 0, Jahr-Spalten 2006-2023)

Extraktion-Funktionen:
- extract_meta: Codex, Dimensionen, Klassifikationen
- extract_summary: Top-Level KPIs (7 pro Uni, nur 2024/2023 Werte)
- extract_personal: Köpfe + VZÄ (185 KB, Zeitreihen 2022-2024)
- extract_studierende: Ordentliche Studierende (3,2 KB)
- extract_neuzulassungen: Neuzugelassene (3,3 KB)
- extract_studien: Ordentliche Studien (3,5 KB)
- extract_abschluesse: Studienabschlüsse (3,7 KB)
- extract_mobilitaet: Outgoing-Studierende (2,9 KB)
- extract_infrastruktur: Nutzfläche m² (69 Zeilen)

### 2. JSON (Datenmodell)

#### meta.json (4 KB)
- universities: 22 Codes (UA-UW) mit Namen
- dimensions: Altersklassen, Universitätsreife, Studiengruppen, Bundesländer, Kontinente
- years: [2022, 2023, 2024]
- stichtage: Personal (31.12.), Studierende WS (15.11.), SS (15.05.)
- klassifikationen: UHSBV, WBV, ISCED, ISCED-F 99, UG

#### summary.json (176 Zeilen, 22 Universitäten)
7 KPIs pro Uni (nur aktuellste Werte):
- personal_koepfe (2024)
- studierende (2024)
- neuzulassungen (2024)
- studien (2024)
- abschluesse (2024)
- mobilitaet (2024)
- infrastruktur (2023)

Struktur:
```json
{
  "UA": {
    "personal_koepfe": 7640.0,
    "studierende": 79149.0,
    "neuzulassungen": 14312.0,
    "studien": 89584.1465299998,
    "abschluesse": 9429.985000000011,
    "mobilitaet": 1518.0,
    "infrastruktur": 364488.0
  }
}
```

#### categories/personal.json (185 KB)
Struktur:
```json
{
  "koepfe": {
    "UA": {
      "Wissenschaftliches und künstlerisches Personal": {
        "Wintersemester 2024 (Stichtag: 31.12.2024)": 7640.0,
        "Wintersemester 2023 (Stichtag: 31.12.2023)": 7503.0,
        "Wintersemester 2022 (Stichtag: 31.12.2022)": 7535.0
      },
      "Professorinnen und Professoren": { ... }
    }
  },
  "vzae": { ... }
}
```

#### categories/studierende.json (3,2 KB)
#### categories/neuzulassungen.json (3,3 KB)
#### categories/studien.json (3,5 KB)
#### categories/abschluesse.json (3,7 KB)
#### categories/mobilitaet.json (2,9 KB)

Struktur (Name-basiert):
```json
{
  "gesamt": {
    "UA": {
      "Ordentliche Studierende": {
        "Frauen": 43523.0,
        "Männer": 35626.0,
        "Gesamt": 79149.0
      }
    }
  }
}
```

#### categories/infrastruktur.json (69 Zeilen)
Struktur (Jahr-basiert):
```json
{
  "gesamt": {
    "UA": {
      "Nutzfläche m²": {
        "Stichtag 31.12.2023": 364488.0,
        "Stichtag 31.12.2022": 365200.47,
        "Stichtag 31.12.2021": 388221.75,
        ...
        "Stichtag 31.12.2006": 319128.26
      }
    }
  }
}
```

### 3. JavaScript → HTML (Dashboard)

#### State-Management (docs/app.js)

State:
- meta: Universitäten-Codex, Dimensionen
- summary: Top-Level KPIs (7 pro Uni)
- categoryData: Aktuelle Kategorie-Daten (Lazy Load)
- sparklineData: Zeitreihen 2022-2024 + maxValue pro Kategorie
- selectedYear: 2024 (UI-Filter)
- selectedCategory: personal (aktive Kategorie)
- selectedUniversities: Set (22 Universitäten)
- aggregationMode: sum (Summe/Durchschnitt/Median)
- sortMode: alpha (Alphabetisch/Wert/Veränderung)

#### Initialisierung

1. loadInitialData: Lädt meta.json + summary.json (4 KB)
2. loadCategoryData: Lädt personal.json (185 KB) - Lazy Load
3. extractSparklineData: Extrahiert erste Kategorie aus categoryData, berechnet maxValue
4. renderUniversityFilters: Filter-Checkboxen (22 Universitäten, gruppiert nach Typ)
5. renderOverview: Karten-Grid (22 Universitäten mit Sparklines)

#### Lazy Loading

Category Switch:
1. User klickt Kategorie-Button
2. state.categoryData = null
3. state.sparklineData = null
4. loadCategoryData(category) → fetch category.json
5. extractSparklineData(category) → erste Kategorie, maxValue berechnen
6. renderOverview() → Karten neu rendern mit neuen Sparklines

Detail-Click:
1. User klickt Universitätskarte
2. if (!state.categoryData) → loadCategoryData(category)
3. renderDetailView(code) → Tabelle mit Zeitreihen 2022-2024

#### Sparkline-Extraktion

Algorithmus:
1. categoryMapping: personal → 'koepfe', studierende → 'gesamt', etc.
2. Für jede Universität: erste Kategorie aus categoryData[dataKey][code]
3. extractYearValues: Sucht "2022", "2023", "2024" in Jahr-Labels
4. maxValue: Math.max über alle y2022, y2023, y2024 Werte
5. Speichert in state.sparklineData[code] = {y2022, y2023, y2024}

Rendering:
- Höhe als Prozent: (value / maxValue) * 100
- Sequentielle Blau-Skala: sparkline-bar:nth-child(1/2/3) → seq-2022/2023/2024
- Tooltips: title="2022: 7 535"

#### Performance

Initial Load:
- meta.json (4 KB)
- summary.json (176 Zeilen, ~3 KB)
- personal.json (185 KB)
- Total: ~192 KB

Category Switch:
- Lazy Load: 3-185 KB je nach Kategorie
- Sparkline-Extraktion: O(n) über 22 Universitäten
- Render: 22 Karten mit 3 Sparkline-Balken

## KOMPONENTEN-HIERARCHIE

```
index.html
  Header
    Year-Selector (2024/2023/2022/Alle)
    Category-Navigation (7 Buttons)
  Main-Container
    Sidebar (280px)
      Filter-Panel
        Universität-Checkboxen (22)
        Aggregation-Buttons (Summe/Durchschnitt/Median)
        Export-Buttons (CSV/JSON)
    Content (flex)
      Overview-View
        University-Grid (280px Karten, Auto-Fill)
          University-Card (22)
            Card-Header (Uni-Name + Typ-Icon)
            Value (48px KPI)
            Label (12px)
            Sparkline (3 Balken)
      Detail-View
        Detail-Table (Zeitreihen 2022-2024)
```

## DESIGN-SYSTEM

### CSS Custom Properties (70 Tokens)

Neutral-Palette (9 Stufen): UI-Elemente
Primary-Palette (6 Stufen): Aktive Buttons (neutral-900 statt Blau)
Uni-Typen (5 Farben): Farbige Icons (voll, tech, kunst, med, special)
Sequentielle Skala (3 Blautöne): Sparklines 2022-2024
Divergierende Skala (7 Stufen): Abweichungen Grün-Grau-Rot
Kategorie-Farben (7 Farben): Tabs

Typografie: Inter, 6 Größen (Body 14px, Small 12px, KPI 48px)
Spacing: 6 Stufen (xs 4px bis xxl 32px)
Radius: Card 8px, Button 6px

### Icons (Font Awesome 6)

Uni-Typen: fa-university (Blau), fa-microchip (Orange), fa-palette (Grün), fa-user-md (Rot), fa-graduation-cap (Violett)
Kategorien: fa-users, fa-user-graduate, fa-user-plus, fa-book, fa-certificate, fa-plane, fa-building

## TECHNOLOGIE-STACK

Frontend:
- HTML5 (semantisch, ARIA-Labels)
- CSS3 (Custom Properties, Flexbox, Grid)
- Vanilla JavaScript (ES6+, async/await, fetch)
- Font Awesome 6 (CDN)

Backend:
- Python 3.x (pandas, openpyxl)
- JSON (UTF-8, ensure_ascii=False)

Hosting:
- GitHub Pages (Static Site, /docs Ordner)
- Keine Backend-Logik erforderlich

## DATEI-STRUKTUR

```
VedMedAI/
├── data/                              74 Excel-Dateien (read-only)
├── pre-processing/
│   ├── analyze.py                     Analyse-Script (overview, structure, deep)
│   ├── extract_to_json.py             JSON-Generierung (main)
│   └── README.md                      Script-Dokumentation
├── docs/
│   ├── index.html                     Dashboard-Interface
│   ├── styles.css                     Design-System (501 Zeilen)
│   ├── app.js                         Dashboard-Logik (519 Zeilen)
│   ├── data/
│   │   ├── meta.json                  Codex + Dimensionen (4 KB)
│   │   ├── summary.json               Top-Level KPIs (176 Zeilen)
│   │   └── categories/
│   │       ├── personal.json          185 KB
│   │       ├── studierende.json       3,2 KB
│   │       ├── neuzulassungen.json    3,3 KB
│   │       ├── studien.json           3,5 KB
│   │       ├── abschluesse.json       3,7 KB
│   │       ├── mobilitaet.json        2,9 KB
│   │       └── infrastruktur.json     69 Zeilen
│   └── knowledge/
│       ├── ARCHITECTURE.md            System-Architektur (dieses Dokument)
│       ├── CONCEPT.md                 Dashboard-Konzept
│       ├── DESIGN.md                  Design-System Version 1.1
│       ├── DATA.md                    Datendokumentation (74 Dateien)
│       └── PROJECT-JOURNAL.md         Session-Protokoll
├── CLAUDE.md                          Arbeitsregeln
└── .gitignore
```

## ERWEITERBARKEIT

### Neue Kategorien hinzufügen

1. Excel-Parsing: Neue extract_* Funktion in extract_to_json.py
2. JSON-Generierung: categories/{kategorie}.json
3. summary.json: Neue KPI hinzufügen
4. app.js: categoryConfig erweitern
5. index.html: Neuen Button hinzufügen
6. styles.css: Neue Kategorie-Farbe (optional)

### Neue Universitäten hinzufügen

1. meta.json: universities Mapping erweitern
2. Alle extract_* Funktionen: name_to_code erweitern
3. Automatisch in allen JSONs verfügbar

### Neue Dimensionen hinzufügen

1. Excel-Parsing: Spalten-Detection erweitern
2. JSON-Struktur: Neue Subkeys
3. app.js: renderDetailView erweitern
4. Keine Änderungen in Übersichts-Karten nötig

## CONSTRAINTS

Technisch:
- Keine Frameworks (Vanilla JS, kein React/Vue)
- Keine Backend-API (Static Site)
- GitHub Pages kompatibel
- Browser: Chrome, Firefox, Safari, Edge (letzte 2 Versionen)

Performance:
- Initial Load: < 1 Sekunde (192 KB)
- Category Switch: < 500 ms (Lazy Load)
- Sparkline-Render: < 100 ms (22 Karten)

Daten:
- Excel-Dateien read-only (keine Änderungen)
- JSON-Generierung manuell (python extract_to_json.py)
- Keine Echtzeit-Updates (statische Daten)

## WISSENSBILANZ-MAPPING

7 Dashboard-Kategorien → 74 Excel-Dateien:

Personal (1-A-1):
- 1-A-1 Personal - Köpfe.xlsx
- 1-A-1 Personal - VZÄ.xlsx

Studierende:
- Ordentliche Studierende nach Universitäten.xlsx
- Ordentliche Studierende an Universitäten - Zeitreihe Wintersemester.xlsx
- Ordentliche Studierende nach Altersklassen.xlsx
- Ordentliche Studierende nach Form der Universitätsreife.xlsx
- Inländische ordentliche Studierende nach regionaler Herkunft.xlsx

Neuzulassungen:
- Ordentliche Neuzugelassene nach Universitäten.xlsx
- Ordentliche Neuzugelassene - Zeitreihe.xlsx
- Ordentliche Neuzugelassene nach Altersklassen.xlsx
- Ordentliche Neuzugelassene nach Form der Universitätsreife.xlsx
- Inländische ordentliche Neuzugelassene nach regionaler Herkunft.xlsx

Studien:
- Ordentliche Studien nach Universitäten.xlsx
- Ordentliche Studien - Zeitreihe Wintersemester.xlsx
- Ordentliche Studien nach nationalen Gruppen.xlsx
- Ordentliche Studien nach internationalen Gruppen.xlsx
- Ordentliche Studien nach Studienart.xlsx
- Ordentliche Studien nach Form der Universitätsreife.xlsx

Abschlüsse:
- Studienabschlüsse nach Universitäten.xlsx
- Studienabschlüsse - Zeitreihe Studienjahr.xlsx

Mobilität:
- Studierendenmobilität nach Universitäten - Outgoing.xlsx
- Studierendenmobilität - Outgoing - Zeitreihe.xlsx
- Studierendenmobilität nach Kontinenten - Outgoing.xlsx

Infrastruktur:
- Nutzfläche nach Universitäten.xlsx

Neue Kennzahlen (noch nicht implementiert):
- 1-A-2 bis 1-A-5 (Personal + Gleichstellung)
- 2-A-1 bis 2-A-9 (Studien + Studierende)
- 2-B-1 (Doktoratsstudierende)
- 3-A-1 bis 3-A-3 (Studienabschlüsse)
