# WORKING JOURNAL

## 2025-11-07 Session 1

### Aufgabe
Datenanalyse aller Excel-Dateien im data/ Ordner
Dokumentation erstellen
Projekt strukturieren

### Durchgeführt
Analyse von 59 Excel-Dateien (österreichische Universitäten, Wissensbilanz)
Kategorisierung nach Inhalt: Personal, Studierende, Neuzulassungen, Studien, Abschlüsse, Mobilität, Infrastruktur
Tiefenanalyse mit Extraktion von Metadaten, Spaltenstrukturen, Sample-Daten

### Erstellt
pre-processing/analyze_data.py - Übersichtsanalyse
pre-processing/analyze_detailed.py - Strukturanalyse
pre-processing/deep_analyze.py - Tiefenanalyse mit vollständigen Metadaten
pre-processing/README.md - Dokumentation der Analyse-Scripts
pre-processing/data_structure.json - Strukturierte Übersicht
pre-processing/data_deep_analysis.json - Vollständige Analyse (374 Datenzeilen pro Hauptdatei)

docs/knowledge/DATA.md - Vollständige Datendokumentation aller 59 Dateien
docs/knowledge/CLAUDE.md - Arbeitsregeln für Claude
docs/WORKING.journal.md - Dieses Journal

### Erkenntnisse

Datenstruktur:
20 österreichische Universitäten erfasst (UA bis UU)
Zeitraum 2022-2024 (Wintersemester)
Stichtag Personal: 31.12.
Stichtag Studierende: 15.11. (WS)

Excel-Format:
3 Sheets pro Datei (Tab, Tabelle2, XLCubedFormats)
15-25 Zeilen Header mit Metadaten
Hierarchische Strukturen durch Einrückungen
Wissensbilanz-Kennzahlen (1.A.1, 1.A.2, etc.)

Datenqualität:
Duplikate erkannt (Dateien mit (1), (2) Suffix)
Konsistente Struktur über alle Dateien
Vollständige Zeitreihen ab ca. 2010

Kategorien:
Personal: 13 Dateien (Köpfe, VZÄ, Stammpersonal, Funktionen, Berufungen, Gender)
Studierende: 7 Dateien (Zeitreihen, Altersklassen, Herkunft, Universitätsreife)
Neuzulassungen: 6 Dateien (analog zu Studierenden)
Studien: 16 Dateien (Programme, ISCED-Klassifikation, Studienarten)
Abschlüsse: 2 Dateien (Zeitreihen, nach Universitäten)
Mobilität: 3 Dateien (Outgoing, Zeitreihen, Kontinente)
Infrastruktur: 2 Dateien (Nutzfläche, Lehrlinge)

Verwendungskategorien Personal:
Wissenschaftliches und künstlerisches Personal
- Professorinnen und Professoren
- Äquivalente (Dozentinnen, Assoziierte Prof., Assistenzprof.)
- Wissenschaftliche Mitarbeiterinnen
Allgemeines Personal

Klassifikationen:
UHSBV - Universitäts-Haushalts- und Stellenplanverordnung
WBV - Wissensbilanz-Verordnung
ISCED - International Standard Classification of Education (UNESCO 2013)
ISCED-F 99 - 99 detaillierte Studienfelder
UG - Universitätsgesetz

Beispielwerte Universität Wien WS 2024:
Wissenschaftliches Personal: 7640 Köpfe / 4282.5 VZÄ
Professorinnen: 573 Köpfe / 560.2 VZÄ

### Nächste Schritte
Bei Bedarf: Datenbereinigung (Encoding, Duplikate)
Bei Bedarf: Datenintegration (gemeinsame Dimensionen)
Bei Bedarf: Analysen (Zeitreihen, Vergleiche, Trends)

### Notizen
data_analysis_report.md gelöscht (ersetzt durch DATA.md)
Alle Python-Scripts in pre-processing/ verschoben
CLAUDE.md Regeln: Keine Emojis, kein Bold, kompakte Dokumentation
