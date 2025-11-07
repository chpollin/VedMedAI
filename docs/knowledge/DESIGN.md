# DESIGN - Dashboard Wissensbilanz

Version: 1.1
Datum: 2025-11-07
Basis: CONCEPT.md + Wahrnehmungsforschung (Cleveland, Tufte, Bertin, Ware)
Revision: Session 8 - Farbige Icons, neutrale UI

## Zielsetzung

Visuelles Design-System f�r Dashboard mit 22 Universit�ten, 7 Datenkategorien, 3 Jahren.
Fokus: Vergleichbarkeit, perzeptuelle Pr�zision, kognitive �konomie.

## Designprinzipien

1. Overview first: Small Multiples Grid aller Universit�ten
2. Zoom and Filter: Interaktive Sidebar, sofortige Reaktion
3. Details on Demand: Drill-down mit Tabellen und Export
4. Perzeptuelle Pr�zision: Balken statt Torten, gemeinsame Basislinie
5. Kognitive �konomie: Neutrale UI, starke Daten-Kontraste
6. Einheitliche Farblogik: Trennung kategorial / sequenziell / divergierend
7. Vergleichbarkeit: Einheitliche Skalen pro Kennzahl
8. Accessibility: WCAG AA, Tastatur, Screenreader, Farbfehlsicht

## Farbsystem

### UI-Palette (Layout, Text, Rahmen)

```css
--neutral-0:   #FFFFFF;
--neutral-50:  #F6F7F9;
--neutral-100: #EEF1F5;
--neutral-200: #E2E8F0;
--neutral-300: #CBD5E1;
--neutral-400: #94A3B8;
--neutral-500: #64748B;
--neutral-700: #334155;
--neutral-900: #0F172A;
--border:      #E2E8F0;
--focus:       #3B82F6;
```

### Prim�r/Akzent (Buttons, aktive Zust�nde)

```css
--primary-50:  #EFF6FF;
--primary-100: #DBEAFE;
--primary-200: #BFDBFE;
--primary-400: #60A5FA;
--primary-600: #2563EB;
--primary-700: #1D4ED8;
--success:     #10B981;
--danger:      #EF4444;
--warning:     #F59E0B;
```

### Kategoriale Palette (Universit�tstypen - aus CONCEPT.md)

5 Typen, farbfehlsicht-angepasst:

```css
--uni-voll:    #2563EB; /* Volluniversit�ten UA-UF */
--uni-tech:    #EA580C; /* Technische UG-UI */
--uni-kunst:   #059669; /* K�nstlerische UJ-UQ */
--uni-med:     #DC2626; /* Medizinische US-UU */
--uni-special: #7C3AED; /* Spezialisierte UN,UV,UW,UR */
```

Mapping:
- UA,UB,UC,UD,UE,UF: voll
- UG,UH,UI: tech
- UJ,UK,UL,UM,UO,UQ: kunst
- US,UT,UU: med
- UN,UV,UW,UR: special

### Sequenzielle Skala (Zeitreihen 2022-2024)

Monochrom Blau f�r Zeitverlauf:

```css
--seq-2022: #DBEAFE; /* �ltestes Jahr */
--seq-2023: #93C5FD;
--seq-2024: #2563EB; /* aktuelles Jahr */
```

Einsatz: Sparklines, Mini-Charts, Zeitreihen-Balken.

### Divergierende Skala (Abweichung vom Referenzwert)

Symmetrisch um Null, nur bei klarem Referenzwert:

```css
--div-neg-3: #991B1B;
--div-neg-2: #DC2626;
--div-neg-1: #FCA5A5;
--div-mid:   #E5E7EB;
--div-pos-1: #86EFAC;
--div-pos-2: #10B981;
--div-pos-3: #047857;
```

Einsatz: Abweichung vom �sterreich-Schnitt oder Peer-Gruppe (wenn aktiviert).

### Kategoriale Datenkategorien (7 Tabs)

```css
--cat-personal:       #2563EB; /* Blau */
--cat-studierende:    #EA580C; /* Orange */
--cat-neuzulassungen: #059669; /* Gr�n */
--cat-studien:        #DC2626; /* Rot */
--cat-abschluesse:    #7C3AED; /* Violett */
--cat-mobilitaet:     #0891B2; /* Cyan */
--cat-infrastruktur:  #DB2777; /* Pink */
```

Einsatz: Tabs, Badges, Legenden. Nicht f�r quantitative Skalen.

## Typografie

Schrift: Inter (System-Fallback: ui-sans-serif, system-ui, -apple-system)

Gr��en:
- Body: 14px
- Small: 12px
- H1: 24px
- H2: 20px
- H3: 16px
- KPI: 32px

Zahlenformat:
- Tausender: schmales Leerzeichen (1 723)
- Prozent: 12,3 %
- Einheiten: K�pfe / VZ� / m�

## Layout

Raster: 8px-Grid (Spacings: 4, 8, 12, 16, 24, 32)
Eckenradius: 8px (Karten), 6px (Buttons)
Schatten: dezent, nur f�r Elevation

### Struktur

Header: 140px fixiert
- Zeile 1: Titel, Jahr-Selektor (2022/2023/2024/Alle)
- Zeile 2: 7 Kategorie-Tabs

Sidebar: 280px links, fixiert beim Scrollen
- Universit�ts-Filter (22 Checkboxen, gruppiert nach Typ)
- Aggregation: Summe/Durchschnitt/Median
- Export: CSV/JSON

Main Content:
- Overview: Karten-Grid (280px Breite, Auto-Fill)
- Vergleich: Horizontale Balken (nach Filter-Auswahl)
- Details: Tabelle mit Zeitreihen

## Komponenten

### Universit�ts-Karte

Gr��e: 280px Breite, flexibel H�he
Padding: 24px
Gap: 24px

Inhalt:
- Kopf: Uni-Name + Typ-Icon (farbig, 20px)
- KPI: 48px Wert (line-height 1)
- Label: 12px uppercase, letter-spacing 0.5px, neutral-400

Icons (Font Awesome 6):
- Volluni: fa-university (uni-voll Blau)
- Tech: fa-microchip (uni-tech Orange)
- Kunst: fa-palette (uni-kunst Gr�n)
- Med: fa-user-md (uni-med Rot)
- Special: fa-graduation-cap (uni-special Violett)

Hover: Elevation (0 4px 12px rgba(0,0,0,0.1)), translateY(-2px)
Click: �ffnet Detail-Ansicht mit Tabelle

CSS-Spezifikation:
- .university-type-badge: display flex, align center, font-size 20px
- .university-type-badge.voll i: color var(--uni-voll)
- .university-value: font-size 48px, font-weight 700, line-height 1
- .university-label: font-size 12px, color neutral-400, text-transform uppercase

### Sparkline

Typ: 3 vertikale Balken oder Linie
Farben: --seq-2022, --seq-2023, --seq-2024
H�he: 40px
Breite: 100% (innerhalb Karte)

Wichtig: Einheitliche y-Skala pro Kennzahl und Filterset
Tooltip: Min/Max-Werte

### Tabs (Kategorie-Navigation)

Aktiv: Unterstreichung 3px + Farbe --cat-[name]
Inaktiv: --neutral-500
Hover: --neutral-700
Icon: Font Awesome 6 vor Label

Icons:
- Personal: fa-users
- Studierende: fa-user-graduate
- Neuzulassungen: fa-user-plus
- Studien: fa-book
- Abschl�sse: fa-certificate
- Mobilit�t: fa-plane
- Infrastruktur: fa-building

### Filter

Universit�ts-Checkboxen:
- Gruppiert nach Typ (5 Gruppen)
- Farbindikator: 12px Quadrat (border-radius 2px) in Typ-Farbe
- Label: Uni-Name
- Keine Icons (kognitive �konomie)

CSS-Spezifikation:
- .color-indicator: width 12px, height 12px, border-radius 2px, margin-right 0.5rem
- .color-indicator.voll: background var(--uni-voll)

Aggregation-Buttons:
- Radio-Style (nur einer aktiv)
- Aktiv: --neutral-900 Hintergrund (nicht Blau)
- Keine Icons

### Buttons

Prim�r:
- Hintergrund: --primary-600
- Text: wei�
- Hover: --primary-700
- Icon: Font Awesome vor Text

Sekund�r:
- Border: --neutral-300
- Text: --neutral-700
- Hover: --neutral-100

### Tooltip

Hintergrund: --neutral-900
Text: wei�, 12px
Padding: 8px 12px
Radius: 6px
Schatten: 0 2px 8px rgba(0,0,0,0.15)
Delay: 150ms

## Visualisierung

### Diagrammwahl

Kategorie-Vergleich: Horizontale Balken, sortiert absteigend
Zeitverlauf: Linie (Sparklines) oder S�ulen (max 3 Jahre)
Teile-zu-Ganze: Gestapelte Balken (nur wenn Summe fix)
Keine Torten/Donuts

### Kodierung

Balken: Gemeinsame Basislinie, L�nge = Wert
Zeit: Sequenzielle Blau-Skala
Abweichung: Divergierende Gr�n-Rot-Skala (nur mit Referenz)
Kategorie: Okabe-Ito-kompatible Palette

Achsen: --neutral-300, d�nn, wenige Ticks
Labels: Nur wo n�tig, Tooltip f�r exakte Werte

### Vergleichsansicht

Horizontale Balken:
- X-Achse: Wert (0 bis Max)
- Y-Achse: Universit�ten (sortiert)
- Farbe: Uni-Typ oder neutral
- Hover: Tooltip mit Frauen/M�nner/Gesamt

Sortierung: Alphabetisch / Nach Wert / Nach Ver�nderung

## Interaktion

Direkte Manipulation: �nderungen wirken sofort (<150ms)
Filter: Apply-less, Reaktion in Echtzeit
URL-State: Filterzustand in Query-Parameter
Breadcrumb: �bersicht > Kategorie > Detail
Undo: Browser-History

Tastatur:
- Tab: Logische Reihenfolge
- Enter/Space: Aktivierung
- ESC: Overlay schlie�en
- Fokus-Ring: --focus, 2px Offset

## Barrierefreiheit

Kontrast: WCAG AA f�r Text (4.5:1) und UI (3:1)
Farbe: Nie alleinige Kodierung, immer + Text/Icon/Pattern
Motion: Respektiert prefers-reduced-motion
ARIA: Diagramme mit title/desc, Tabellen mit scope

Farbfehlsicht:
- Rot-Gr�n: Divergierende Skala mit Helligkeitsunterschied
- Uni-Typen: Zus�tzlich Icons

## Design-Tokens (JSON)

```json
{
  "color": {
    "neutral": {"0":"#FFFFFF","50":"#F6F7F9","100":"#EEF1F5","200":"#E2E8F0","300":"#CBD5E1","400":"#94A3B8","500":"#64748B","700":"#334155","900":"#0F172A"},
    "primary": {"50":"#EFF6FF","100":"#DBEAFE","200":"#BFDBFE","400":"#60A5FA","600":"#2563EB","700":"#1D4ED8"},
    "uni": {"voll":"#2563EB","tech":"#EA580C","kunst":"#059669","med":"#DC2626","special":"#7C3AED"},
    "seq": {"2022":"#DBEAFE","2023":"#93C5FD","2024":"#2563EB"},
    "div": {"neg3":"#991B1B","neg2":"#DC2626","neg1":"#FCA5A5","mid":"#E5E7EB","pos1":"#86EFAC","pos2":"#10B981","pos3":"#047857"},
    "cat": {"personal":"#2563EB","studierende":"#EA580C","neuzulassungen":"#059669","studien":"#DC2626","abschluesse":"#7C3AED","mobilitaet":"#0891B2","infrastruktur":"#DB2777"},
    "focus": "#3B82F6",
    "border": "#E2E8F0"
  },
  "radius": {"card":"8px","button":"6px"},
  "space": {"xs":"4px","sm":"8px","md":"12px","lg":"16px","xl":"24px","xxl":"32px"},
  "font": {"family":"Inter, ui-sans-serif, system-ui","sizeBody":"14px","sizeSmall":"12px","sizeH1":"24px","sizeH2":"20px","sizeH3":"16px","sizeKPI":"32px"}
}
```

## Icons (Font Awesome 6 Free)

Integration via CDN:
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
```

Icon-Mapping:
- Universit�tstypen: fa-university, fa-microchip, fa-palette, fa-user-md, fa-graduation-cap
- Kategorien: fa-users, fa-user-graduate, fa-user-plus, fa-book, fa-certificate, fa-plane, fa-building
- Aktionen: fa-download (Export), fa-filter (Filter), fa-chart-bar (Aggregation)
- Navigation: fa-home (�bersicht), fa-chevron-right (Breadcrumb)

Verwendung:
```html
<i class="fa-solid fa-university"></i>
```

Gr��en: 14px (inline), 16px (Button), 20px (Header)
