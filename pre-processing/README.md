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

## Verwendung

Im Projektroot ausführen:

```bash
python pre-processing/analyze.py overview
python pre-processing/analyze.py structure
python pre-processing/analyze.py deep
python pre-processing/analyze.py all
```

## Ausgabe JSON-Dateien

extract_to_json.py generiert:

docs/data/meta.json
- Universitäten-Codex (UA-UU)
- Dimensionen (Altersklassen, Universitätsreife, Studiengruppen, etc.)
- Klassifikationen (UHSBV, WBV, ISCED, UG)
- Jahre, Stichtage

docs/data/summary.json
- Top-Level KPIs pro Universität
- Schneller Überblick für Dashboard

docs/data/categories/
- personal.json (Köpfe, VZÄ nach Verwendungskategorien)
- studierende.json (Ordentliche Studierende)
- weitere Kategorien folgen

## Abhängigkeiten

- pandas
- openpyxl (für Excel-Support)

```bash
pip install pandas openpyxl
```
