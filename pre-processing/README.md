# Pre-Processing

Dieser Ordner enthält alle Scripts zur Vorbereitung und Aufbereitung der Rohdaten.

## Scripts

### analyze_data.py
Erste Übersichtsanalyse aller Excel-Dateien im data/ Ordner.

Funktion:
- Zählt alle Excel-Dateien
- Liest erste 3 Dateien im Detail
- Kategorisiert Dateien nach Namen
- Zeigt Sheet-Struktur und Dimensionen

Ausgabe: Konsole, visuelle Übersicht

### analyze_detailed.py
Mittlere Analysetiefe mit Strukturextraktion.

Funktion:
- Analysiert alle Excel-Dateien
- Extrahiert Sheet-Namen und Dimensionen
- Identifiziert Titel aus ersten Zeilen
- Findet Header-Zeilen und Spaltennamen
- Schätzt Anzahl Datenzeilen

Ausgabe: data_structure.json

### deep_analyze.py
Tiefenanalyse mit vollständiger Datenextraktion.

Funktion:
- Vollständige Analyse aller 59 Excel-Dateien
- Extrahiert Metadaten aus Header-Zeilen
- Identifiziert Datenstart und Header-Position
- Liest Sample-Daten (erste 5 Zeilen)
- Extrahiert kategorische Werte (Universitäten, Kategorien)
- Analysiert Datenstruktur und Spaltentypen

Ausgabe: data_deep_analysis.json

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

Alle Scripts im Projektroot ausführen:

```bash
python pre-processing/analyze_data.py
python pre-processing/analyze_detailed.py
python pre-processing/deep_analyze.py
```

## Abhängigkeiten

- pandas
- openpyxl (für Excel-Support)

```bash
pip install pandas openpyxl
```
