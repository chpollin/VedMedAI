# Pre-Processing

Dieser Ordner enthält alle Scripts zur Vorbereitung und Aufbereitung der Rohdaten.

## Scripts

### analyze.py
Zentrales Analyse-Script mit 3 Modi für Excel-Dateien im data/ Ordner.

### extract_to_json.py
Konvertiert Excel-Dateien zu JSON für Dashboard (docs/data/).

Modi:

overview - Übersichtsanalyse
- Zählt alle Excel-Dateien
- Liest erste 3 Dateien im Detail
- Kategorisiert Dateien nach Namen
- Zeigt Sheet-Struktur und Dimensionen
- Ausgabe: Konsole

structure - Strukturanalyse
- Analysiert alle Excel-Dateien
- Extrahiert Sheet-Namen und Dimensionen
- Identifiziert Titel aus ersten Zeilen
- Findet Header-Zeilen und Spaltennamen
- Schätzt Anzahl Datenzeilen
- Ausgabe: data_structure.json

deep - Tiefenanalyse
- Vollständige Analyse aller 59 Excel-Dateien
- Extrahiert Metadaten aus Header-Zeilen
- Identifiziert Datenstart und Header-Position
- Liest Sample-Daten (erste 5 Zeilen)
- Extrahiert kategorische Werte (Universitäten, Kategorien)
- Analysiert Datenstruktur und Spaltentypen
- Ausgabe: data_deep_analysis.json

all - Alle Modi nacheinander

## Ergebnisse

### data_structure.json
Strukturierte Übersicht aller Excel-Dateien mit:
- Dateiname
- Anzahl Sheets
- Dimensionen
- Titel
- Spaltennamen
- Anzahl Datenzeilen

### data_deep_analysis.json
Vollständige Analyse mit:
- Komplette Metadaten
- Title-Lines (erste 10 Zeilen)
- Header-Row Position
- Data-Start-Row
- Spaltennamen
- Sample-Daten (erste 5 Zeilen)
- Unique Values für kategorische Spalten
- Universitätslisten
- Verwendungskategorien

## Parsing-Funktionen

extract_to_json.py verwendet 4 Parsing-Strategien:

read_excel_file:
- Standard-Format: "Universität (Codex)" in Spalte 1
- Header-Detection: Sucht "Universität" + "Codex" in ersten 30 Zeilen
- Daten ab Spalte 4
- Verwendet für: Personal, Zeitreihen

read_name_based_file:
- Universitätsname statt Code
- name_to_code Mapping (22 Universitäten)
- Verwendet für: Studierende, Neuzulassungen, Studien, Abschlüsse, Mobilität (gesamt)

read_wissensbilanz_file:
- Neue Wissensbilanz-Dateien: "Universität" in Spalte 0, "Codex" in Spalte 1
- Daten ab Spalte 3
- Aggregiert unter "Gesamt" Kategorie
- Verwendet für: Berufungen, Frauenquote, Gender Pay Gap, etc.

read_wissensbilanz_multiheader_file:
- Multi-Header-Struktur: Zeile -1 (Studienjahr), Zeile 0 (Spalten)
- Kombiniert zu "Studienjahr 2023/24 - EU"
- Entfernt Pandas-Suffixe (.1, .2)
- Verwendet für: Incoming-Studierende, Outgoing-Studierende

read_infrastruktur_file:
- Spezial-Format: Jahr-Spalten (2006-2023)
- Universitätsname in Spalte 0
- Nur für: Nutzfläche nach Universitäten

## Verwendung

Im Projektroot ausführen:

```bash
python pre-processing/analyze.py overview
python pre-processing/analyze.py structure
python pre-processing/analyze.py deep
python pre-processing/analyze.py all
python pre-processing/extract_to_json.py
```

## Ausgabe JSON-Dateien

extract_to_json.py generiert:

docs/data/meta.json
- Universitäten-Codex (22 Universitäten UA-UW)
- Dimensionen (Altersklassen, Universitätsreife, Studiengruppen, Bundesländer, Kontinente, Studienarten)
- Klassifikationen (UHSBV, WBV, ISCED, ISCED-F 99, UG)
- Jahre (2022-2024), Stichtage

docs/data/summary.json
- 7 Top-Level KPIs pro Universität (nur 2024-Werte)
- personal_koepfe, studierende, neuzulassungen, studien, abschluesse, mobilitaet, infrastruktur
- Initial Load für schnellen Dashboard-Überblick (4 KB mit meta.json)

docs/data/categories/

Basis-Kategorien (7 Dateien):
- personal.json (185 KB: Köpfe + VZÄ nach UHSBV-Kategorien, Zeitreihen 2022-2024)
- studierende.json (3,2 KB: Ordentliche Studierende gesamt, Frauen/Männer)
- neuzulassungen.json (3,3 KB: Ordentliche Neuzugelassene gesamt, Frauen/Männer)
- studien.json (3,5 KB: Ordentliche Studien gesamt, Frauen/Männer)
- abschluesse.json (3,7 KB: Ordentliche Studienabschlüsse gesamt, Frauen/Männer)
- mobilitaet.json (2,9 KB: Outgoing-Studierende gesamt, Frauen/Männer)
- infrastruktur.json (69 Zeilen: Nutzfläche m² 2006-2023, 22 Universitäten)

Neue Wissensbilanz-Kennzahlen (12 Dateien):
- berufungen.json (6,0 KB: Berufungen an die Universität, Frauen/Männer/Gesamt, 2022-2024)
- frauenquote-kollegialorgane.json (14 KB: Frauenquote in Kollegialorganen, 2024)
- gender-pay-gap.json (16 KB: Gender pay gap, 2022-2024)
- professorinnen-aequivalente.json (3,7 KB: ProfessorInnen und Äquivalente, 2022-2024)
- eingerichtete-studien.json (2,3 KB: Eingerichtete Studien, 2022-2024)
- besondere-zulassungsbedingungen.json (6,0 KB: Besondere Zulassungsbedingungen, 2022-2024)
- belegte-ordentliche-studien.json (4,6 KB: Belegte ordentliche Studien, 2022-2024)
- outgoing-studierende.json (5,6 KB: Ordentliche Studierende outgoing, 2022-2023)
- incoming-studierende.json (5,7 KB: Ordentliche Studierende incoming, 2022-2023)
- doktoratsstudierende.json (6,0 KB: Doktoratsstudierende mit BV, 2022-2024)
- ausserordentliche-abschluesse.json (2 B: Außerordentliche Studienabschlüsse, leer)
- ordentliche-abschluesse.json (3,2 KB: Ordentliche Studienabschlüsse, 2022-2024)

## Abhängigkeiten

- pandas
- openpyxl (für Excel-Support)

```bash
pip install pandas openpyxl
```
