# DATA - Datendokumentation

**Quelle:** Österreichische Universitäten Wissensbilanz
**Format:** Excel XLSX
**Dateien:** 74 (59 ursprünglich + 15 neue Wissensbilanz-Kennzahlen)
**Zeitraum:** 2022-2024 (teilweise 2006-2023)
**Stichtag Personal:** 31.12.
**Stichtag Studierende:** 15.11. (WS) / 15.05. (SS)

**Update:** Session 9 - 15 zusätzliche Dateien (1-A-2 bis 1-A-5, 2-A-1 bis 2-A-9, 2-B-1, 3-A-1 bis 3-A-3)

## UNIVERSITÄTEN-CODEX

| Code | Universität |
|------|-------------|
| UA | Universität Wien |
| UB | Universität Graz |
| UC | Universität Innsbruck |
| UD | Universität Salzburg |
| UE | Universität Klagenfurt |
| UF | Universität Linz |
| UG | Technische Universität Wien |
| UH | Technische Universität Graz |
| UI | Montanuniversität Leoben |
| UJ | Universität für Bodenkultur Wien |
| UK | Universität für künstlerische und industrielle Gestaltung Linz |
| UL | Universität Mozarteum Salzburg |
| UM | Universität für Musik und darstellende Kunst Wien |
| UN | Universität für Musik und darstellende Kunst Graz |
| UO | Akademie der bildenden Künste Wien |
| UQ | Universität für angewandte Kunst Wien |
| UR | Universität für Weiterbildung Krems |
| US | Medizinische Universität Wien |
| UT | Medizinische Universität Graz |
| UU | Medizinische Universität Innsbruck |
| UV | Veterinärmedizinische Universität Wien |
| UW | Wirtschaftsuniversität Wien |

## STANDARDDIMENSIONEN

### Altersklassen
18-21, 22-25, 26-30, 31-35, 36-40, 41-45, 46-50, 51+

### Universitätsreife-Kategorien
- AHS-Matura
- BHS-Matura
- Studienberechtigungsprüfung
- Berufsreifeprüfung
- Sonstige österreichische Zulassung
- EWR-Reifezeugnis
- Sonstige ausländische Zulassung

### Studiengruppen National
- Geisteswissenschaften
- Naturwissenschaften
- Sozial- und Wirtschaftswissenschaften
- Rechtswissenschaften
- Medizin
- Technik
- Kunst

### Studienarten
- Bachelor
- Master
- Diplom
- Doktorat/PhD

### Bundesländer
Wien, Niederösterreich, Burgenland, Oberösterreich, Salzburg, Steiermark, Kärnten, Tirol, Vorarlberg

### Kontinente (Mobilität)
Europa, Nordamerika, Südamerika, Asien, Afrika, Ozeanien

## TECHNISCHE STRUKTUR

### Excel-Standard
- **Sheets:** 2-3 pro Datei (Tab, Tabelle2, XLCubedFormats)
- **Header-Bereich:** Zeilen 1-25 (variabel)
  - Zeile 1-2: Wissensbilanz-Kennzahl
  - Zeile 3-4: Titel
  - Zeile 5-10: Definitionen, Quellen, Anmerkungen
  - Zeile 11-15: Datenprüfung, Aufbereitung
  - Letzte Header-Zeile: Spaltennamen
- **Encoding:** UTF-8
- **Dezimaltrennzeichen:** Punkt
- **Tausendertrennzeichen:** Keines
- **Hierarchie:** Einrückungen durch Leerzeichen

### Datenverantwortung
- **Datenquelle:** Datenmeldungen der Universitäten (UHSBV/WBV)
- **Datenprüfung:** bmfwf, Abt. I/2 oder I/6
- **Datenaufbereitung:** bmfwf, Abt. I/10

---

## 1. PERSONAL (15 Dateien)

### 1.A.1 Personal - Köpfe
**Datei:** `1-A-1 Personal - Köpfe.xlsx`  
**Kennzahl:** Wissensbilanz 1.A.1  
**Struktur:** 374 Datenzeilen + 20 Header | 7 Spalten  
**Zeitreihe:** WS 2024, 2023, 2022  
**Definition:** Anzahl Mitarbeiter als physische Personen (Kopfzahl)  
**Erfassung:** Alle Verwendungen gemäß Z 3.6 der Anlage 9 UHSBV  
**Ausschluss:** Karenzierte und ausgeschiedene Personen  
**Besonderheit:** Personen mit mehreren Beschäftigungsverhältnissen nur einmal gezählt

**Verwendungskategorien (hierarchisch):**
- Wissenschaftliches und künstlerisches Personal
  - Professorinnen und Professoren
  - Äquivalente zu Professorinnen und Professoren
    - Dozentinnen und Dozenten
    - Assoziierte Professorinnen und Professoren (KV)
    - Assistenzprofessorinnen und Assistenzprofessoren (KV) (UG-Karrierepfad)
  - wissenschaftliche und künstlerische Mitarbeiterinnen und Mitarbeiter
    - darunter Universitätsassistentinnen und -assistenten (KV) auf Laufbahnstelle gemäß § 13b Abs. 3 UG
    - darunter über F & E-Projekte drittfinanzierte Mitarbeiterinnen und Mitarbeiter
    - darunter Ärztinnen und Ärzte in Facharztausbildung
    - darunter Ärzt/inn/e/n mit ausschließlichen Aufgaben in öffentlichen Krankenanstalten
    - darunter Krankenpflege im Rahmen einer öff. Krankenanstalt und Tierpflege in med. Einrichtungen
- Allgemeines Personal
  - darunter über F&E-Projekte drittfinanziertes allgemeines Personal

**Beispielwerte Universität Wien WS 2024:**
- Wissenschaftliches Personal gesamt: 7640 Köpfe
- Professorinnen und Professoren: 573
- Äquivalente zu Professorinnen: 263
- Dozentinnen und Dozenten: 114

### 1.A.1 Personal - VZÄ
**Datei:** `1-A-1 Personal - VZÄ.xlsx`  
**Kennzahl:** Wissensbilanz 1.A.1  
**Struktur:** 374 Datenzeilen + 19 Header | 7 Spalten  
**Zeitreihe:** WS 2024, 2023, 2022  
**Definition:** Personal als Vollzeitäquivalente (FTE)  
**Erfassung:** Mit Beschäftigungsausmaß gewichtete Personen-Einheiten  
**Ausschluss:** Ausgeschiedene Personen  
**Kategorien:** Identisch zu Köpfe-Datei

**Beispielwerte Universität Wien WS 2024:**
- Wissenschaftliches Personal gesamt: 4282.5 VZÄ
- Professorinnen und Professoren: 560.2 VZÄ

### 1.A.2 Berufungen
**Datei:** `1-A-2 Berufungen an die Universität.xlsx`  
**Kennzahl:** Wissensbilanz 1.A.2  
**Struktur:** 26 Datenzeilen + 17 Header | 15 Spalten  
**Zeitreihe:** 2024, 2023, 2022 (Studienjahre)  
**Definition:** Anzahl Berufungen an die Universität  
**Spaltenstruktur:** Jahr, Studienjahr, Measures (3 Spaltenblöcke für 3 Jahre, jeweils Frauen/Männer/Gesamt)

### 1.A.3 Frauenquote Kollegialorgane
**Datei:** `1-A-3 Frauenquote in Kollegialorganen.xlsx`  
**Kennzahl:** Wissensbilanz 1.A.3  
**Struktur:** 25 Datenzeilen + 17 Header | 24 Spalten  
**Zeitreihe:** 2024, 2023, 2022  
**Definition:** Frauenquote in universitären Entscheidungsgremien  
**Spalten pro Jahr:** 7 (Köpfe Frauen, Köpfe Männer, Köpfe Gesamt, Frauen %, Männer %, Organe mit erfüllter Quote, Interpretation)  
**Organe:** Universitätsrat, Rektorat, Senat, Fakultätskollegien  
**Hinweis:** Auswahl Gesamt beim Feld Monitoringkategorie führt zu nicht verwertbaren Ergebnissen  
**Anmerkung:** Aufgrund Änderungen in Erhebungsmethoden sind Werte im zeitlichen Verlauf nicht immer direkt vergleichbar

**Beispielwerte Universität Wien 2024:**
- Köpfe Frauen: 2, Köpfe Männer: 3, Köpfe Gesamt: 5
- Frauen %: 40%, Organe mit erfüllter Quote: 1

### 1.A.4 Gender Pay Gap
**Datei:** `1-A-4 Gender pay gap.xlsx`  
**Kennzahl:** Wissensbilanz 1.A.4  
**Struktur:** 27 Datenzeilen + 16 Header | 21 Spalten  
**Zeitreihe:** 2024, 2023, 2022  
**Definition:** Lohnunterschied zwischen Geschlechtern  
**Spalten pro Jahr:** 6 (Gehaltsvergleiche nach Kategorien)

### 1.A.5 Frauen in Berufungsverfahren
**Datei:** `1-A-5 Repräsentanz von Frauen in Berufungsverfahren.xlsx`  
**Kennzahl:** Wissensbilanz 1.A.5  
**Struktur:** 50 Datenzeilen + 17 Header | 13 Spalten  
**Zeitreihe:** 2024, 2023, 2022  
**Definition:** Frauenanteil in allen Phasen von Berufungsverfahren  
**Erfasst:** BewerberInnen, Shortlist, Berufungen nach Geschlecht

### Personal an Universitäten - Kopfzahl
**Datei:** `Personal an Universitäten - Kopfzahl.xlsx`  
**Struktur:** Variable  
**Spalten:** 7+  
**Definition:** Erweiterte Personalstatistik nach Verwendungskategorien  
**Funktion:** Detaillierte Aufschlüsselung aller Personalkategorien

### Personal an Universitäten - VZÄ
**Datei:** `Personal an Universitäten - VZÄ.xlsx`  
**Definition:** Wie Kopfzahl, jedoch in Vollzeitäquivalenten

### Stammpersonal - Kopfzahl
**Datei:** `Stammpersonal an Universitäten - Kopfzahl.xlsx`  
**Definition:** Nur Stammpersonal (unbefristete Stellen)  
**Ausschluss:** Befristete, projektgebundene Stellen

### Stammpersonal - VZÄ
**Datei:** `Stammpersonal an Universitäten - VZÄ.xlsx`  
**Definition:** Stammpersonal in Vollzeitäquivalenten

### Personal nach Verwendung
**Datei:** `Personal nach Verwendung.xlsx`  
**Definition:** Detaillierte Aufschlüsselung nach Verwendungsarten  
**Kategorien:** Lehre, Forschung, Verwaltung, Technik

### Funktionen an Universitäten
**Dateien:** `Funktionen an Universitäten.xlsx`, `(1).xlsx`  
**Definition:** Besetzung akademischer und administrativer Funktionsstellen  
**Erfasst:** Professuren, Lektorate, Institutsvorstände, Dekane

### Altersverteilung Personal
**Dateien:** `Altersverteilung nach Verwendung.xlsx`, `(1).xlsx`  
**Definition:** Altersstruktur des Personals nach Verwendungskategorien  
**Altersklassen:** Variable Klasseneinteilung

### Altersverteilung ProfessorInnen
**Datei:** `Altersverteilung von ProfessorInnen nach Universitäten.xlsx`  
**Definition:** Altersverteilung nur des Professorats  
**Aufschlüsselung:** Pro Universität und Altersklasse

### Lehrlinge
**Datei:** `Lehrlinge nach Universitäten.xlsx`  
**Definition:** Auszubildende in Verwaltung und Technik  
**Bereiche:** Verwaltung, Technik, Bibliothek

---

## 2. STUDIERENDE (8 Dateien)

### Ordentliche Studierende - Zeitreihe
**Datei:** `Ordentliche Studierende an Universitäten - Zeitreihe Wintersemester.xlsx`  
**Definition:** Historische Entwicklung ordentlicher Studierendenzahlen  
**Zeitreihe:** Ab ca. 2010 bis WS 2024  
**Aufschlüsselung:** Geschlecht, Universität

### Ordentliche Studierende - Universitäten
**Datei:** `Ordentliche Studierende nach Universitäten.xlsx`  
**Definition:** Aktuelle Studierendenzahlen pro Universität  
**Aufschlüsselung:** Geschlecht, Staatsangehörigkeit (inländisch/ausländisch)

### Ordentliche Studierende - Altersklassen
**Datei:** `Ordentliche Studierende an Universitäten nach Altersklassen.xlsx`  
**Definition:** Altersverteilung der Studierenden  
**Altersklassen:** 18-21, 22-25, 26-30, 31-35, 36-40, 41-45, 46-50, 51+

### Ordentliche Studierende - Universitätsreife
**Dateien:** `Ordentliche Studierende an Universitäten nach Form der allgemeinen Universitätsreife.xlsx`, `(1).xlsx`  
**Definition:** Art der Hochschulzugangsberechtigung  
**Kategorien:** AHS-Matura, BHS-Matura, Studienberechtigungsprüfung, Berufsreifeprüfung, Sonstige österreichische Zulassung, EWR-Reifezeugnis, Sonstige ausländische Zulassung

### Inländische Studierende - regionale Herkunft
**Datei:** `Inländische ordentliche Studierende nach regionaler Herkunft.xlsx`  
**Definition:** Herkunftsbundesland österreichischer Studierender  
**Bundesländer:** Wien, Niederösterreich, Burgenland, Oberösterreich, Salzburg, Steiermark, Kärnten, Tirol, Vorarlberg

### Studierende gesamt - Zeitreihe
**Datei:** `Studierende an Universitäten - Zeitreihe Wintersemester.xlsx`  
**Definition:** Alle Studierenden inkl. außerordentlicher  
**Kategorien:** Ordentlich, außerordentlich, Lehrgang

### Senioren-Studierende
**Datei:** `Senioren-Studierende an Universitäten - Zeitreihe Wintersemester.xlsx`  
**Definition:** Studierende 55+  
**Zeitreihe:** Historische Entwicklung Seniorenstudium

---

## 3. NEUZULASSUNGEN (8 Dateien)

### Ordentliche Neuzugelassene - Zeitreihe
**Datei:** `Ordentliche Neuzugelassene an Universitäten - Zeitreihe.xlsx`  
**Definition:** Erstmalig zugelassene ordentliche Studierende  
**Zeitreihe:** Ab ca. 2010 bis aktuell  
**Aufschlüsselung:** Geschlecht, Staatsangehörigkeit

### Ordentliche Neuzugelassene - Universitäten
**Datei:** `Ordentliche Neuzugelassene nach Universitäten.xlsx`  
**Definition:** Neuzulassungen pro Universität  
**Aufschlüsselung:** Geschlecht, Studienart

### Ordentliche Neuzugelassene - Altersklassen
**Dateien:** `Ordentliche Neuzugelassene an Universitäten nach Altersklassen.xlsx`, `(1).xlsx`  
**Definition:** Alter bei Erstzulassung  
**Altersklassen:** 18-21, 22-25, 26-30, 31-35, 36-40, 41-45, 46-50, 51+

### Ordentliche Neuzugelassene - Universitätsreife
**Datei:** `Ordentliche Neuzugelassene an Universitäten nach Form der allgemeinen Universitätsreife.xlsx`  
**Definition:** Zugangsweg der Neuzugelassenen  
**Kategorien:** AHS-Matura, BHS-Matura, Studienberechtigungsprüfung, Berufsreifeprüfung, Sonstige österreichische Zulassung, EWR-Reifezeugnis, Sonstige ausländische Zulassung

### Inländische Neuzugelassene - regionale Herkunft
**Datei:** `Inländische ordentliche Neuzugelassene nach regionaler Herkunft.xlsx`  
**Definition:** Herkunftsbundesland bei Erstzulassung  
**Bundesländer:** Wien, Niederösterreich, Burgenland, Oberösterreich, Salzburg, Steiermark, Kärnten, Tirol, Vorarlberg

### Neuzugelassene gesamt - Zeitreihe
**Dateien:** `Neuzugelassene an Universitäten - Zeitreihe.xlsx`, `(1).xlsx`, `(2).xlsx`  
**Definition:** Alle Neuzulassungen inkl. außerordentlicher  
**Kategorien:** Ordentlich, außerordentlich

---

## 4. STUDIEN (14 Dateien)

### Ordentliche Studien - Zeitreihe
**Datei:** `Ordentliche Studien - Zeitreihe Wintersemester.xlsx`  
**Definition:** Anzahl belegter Studien (nicht Studierende)  
**Hinweis:** Ein/e Studierende/r kann mehrere Studien belegen  
**Zeitreihe:** Ab ca. 2010 bis WS 2024

### Ordentliche Studien - Universitäten
**Datei:** `Ordentliche Studien nach Universitäten.xlsx`  
**Definition:** Anzahl Studienbelegungen pro Universität  
**Aufschlüsselung:** Studienart, Geschlecht

### Ordentliche Studien - nationale Gruppen
**Datei:** `Ordentliche Studien nach nationalen Gruppen von Studien.xlsx`  
**Definition:** Österreichische Klassifikation von Studienrichtungen  
**Gruppen:** Geisteswissenschaften, Naturwissenschaften, Sozial- und Wirtschaftswissenschaften, Rechtswissenschaften, Medizin, Technik, Kunst

### Ordentliche Studien - internationale Gruppen
**Datei:** `Ordentliche Studien nach internationalen Gruppen von Studien.xlsx`  
**Definition:** ISCED-Klassifikation (International Standard Classification of Education)  
**Standard:** UNESCO ISCED 2013

### Ordentliche Studien - Studienart
**Dateien:** `Ordentliche Studien nach Studienart.xlsx`, `(1).xlsx`  
**Definition:** Aufschlüsselung nach Abschlussart  
**Arten:** Bachelor, Master, Diplom, Doktorat/PhD

### Ordentliche Studien - Universitätsreife
**Datei:** `Ordentliche Studien an Universitäten nach Form der allgemeinen Universitätsreife.xlsx`  
**Definition:** Studien nach Art der Hochschulzugangsberechtigung

### Studien im ersten Semester - Zeitreihe
**Datei:** `Ordentliche Studien im ersten Semester - Zeitreihe Studienjahr.xlsx`  
**Definition:** Neu begonnene Studien pro Studienjahr  
**Hinweis:** Inkludiert Mehrfachstudien (eine Person kann mehrere Studien beginnen)

### Studien im ersten Semester - Universitäten
**Datei:** `Ordentliche Studien im ersten Semester nach Universitäten.xlsx`  
**Definition:** Neu begonnene Studien pro Universität

### Studien im ersten Semester - nationale Gruppen
**Datei:** `Ordentliche Studien im ersten Semester nach nationalen Gruppen von Studien.xlsx`  
**Definition:** Neu begonnene Studien nach österreichischer Klassifikation

### Studien im ersten Semester - internationale Gruppen
**Datei:** `Ordentliche Studien im ersten Semester nach internationalen Gruppen von Studien.xlsx`  
**Definition:** Neu begonnene Studien nach ISCED

### Studien im ersten Semester - ISCED-F 99
**Datei:** `Ordentliche Studien im ersten Semester nach internationalen Gruppen von Studien (ISCED-F 99).xlsx`  
**Definition:** Detaillierte ISCED Fields of Education and Training 2013  
**Klassifikation:** 99 detaillierte Studienfelder

### Studien im ersten Semester - Studienart
**Datei:** `Ordentliche Studien im ersten Semester nach Studienart.xlsx`  
**Definition:** Neu begonnene Studien nach Abschlussart

### Studien im ersten Semester - Universitätsreife
**Datei:** `Ordentliche Studien im ersten Semester an Universitäten nach Form der allgemeinen Universitätsreife.xlsx`  
**Definition:** Neu begonnene Studien nach Zugangsweg

### Studien im ersten Semester - Studium-Ebene
**Datei:** `Ordentliche Studien im ersten Semester auf Studium-Ebene.xlsx`  
**Definition:** Detaillierte Liste aller konkreten Studienprogramme  
**Inhalt:** Einzelne Studien mit offiziellen Namen

### Liste belegter Studien - Zeitreihe
**Datei:** `Liste aller von ordentlichen Studierenden belegten Studien im ersten Semester - Zeitreihe Studienjahr.xlsx`  
**Definition:** Vollständige Liste aller im 1. Semester belegten Studien  
**Zeitreihe:** Mit historischer Entwicklung

### Liste belegter Studien - Universitäten
**Datei:** `Liste aller von ordentlichen Studierenden belegten Studien im ersten Semester - Universitäten.xlsx`  
**Definition:** Belegte Studien aufgeschlüsselt nach Universitäten

---

## 5. STUDIENABSCHLÜSSE (2 Dateien)

### Studienabschlüsse - Zeitreihe
**Dateien:** `Studienabschlüsse an Universitäten - Zeitreihe Studienjahr.xlsx`, `(1).xlsx`  
**Definition:** Anzahl abgeschlossener Studien pro Studienjahr  
**Zeitreihe:** Ab ca. 2010  
**Aufschlüsselung:** Studienart, Geschlecht

### Studienabschlüsse - Universitäten
**Dateien:** `Studienabschlüsse nach Universitäten.xlsx`, `(1).xlsx`  
**Definition:** Abschlüsse pro Universität  
**Aufschlüsselung:** Studienart (Bachelor, Master, Diplom, Doktorat)

---

## 6. MOBILITÄT (3 Dateien)

### Studierendenmobilität - Zeitreihe
**Datei:** `Studierendenmobilität an Universitäten - Outgoing - Zeitreihe.xlsx`  
**Definition:** Historische Entwicklung Auslandsmobilität  
**Erfasst:** Österreichische Studierende im Ausland  
**Programme:** Erasmus+, Freemover, Austauschprogramme

### Studierendenmobilität - Universitäten
**Datei:** `Studierendenmobilität nach Universitäten - Outgoing.xlsx`  
**Definition:** Outgoing-Mobilität pro Heimatuniversität  
**Aufschlüsselung:** Zielland, Programm

### Studierendenmobilität - Kontinente
**Datei:** `Studierendenmobilität nach Kontinenten - Outgoing.xlsx`  
**Definition:** Zielregionen der Mobilität  
**Kontinente:** Europa, Nordamerika, Südamerika, Asien, Afrika, Ozeanien

---

## 7. INFRASTRUKTUR (1 Datei)

### Nutzfläche
**Datei:** `Nutzfläche nach Universitäten.xlsx`  
**Definition:** Verfügbare Gebäudeflächen in m²  
**Kategorien:** Hörsäle, Seminarräume, Labore, Bibliotheken, Verwaltung, Sonstige

---

## KLASSIFIKATIONSSYSTEME

### UHSBV
**Name:** Universitäts-Haushalts- und Stellenplanverordnung  
**Verwendung:** Personalklassifikation  
**Referenz:** Z 3.6 der Anlage 9 für Verwendungskategorien

### WBV
**Name:** Wissensbilanz-Verordnung  
**Verwendung:** Definition aller Kennzahlen  
**Struktur:** Kennzahlen 1.A.1 bis 1.A.5 und weitere

### ISCED
**Name:** International Standard Classification of Education  
**Herausgeber:** UNESCO  
**Version:** ISCED 2013  
**Verwendung:** Internationale Vergleichbarkeit von Studienrichtungen

### ISCED-F 99
**Name:** ISCED Fields of Education and Training 2013  
**Felder:** 99 detaillierte Studienrichtungen  
**Verwendung:** Granulare fachliche Klassifikation

### UG
**Name:** Universitätsgesetz  
**Relevanz:** Rechtsgrundlage für Personalkategorien  
**Beispiel:** § 13b Abs. 3 UG für Laufbahnstellen

---

## QUALITÄTSHINWEISE

### Zeitliche Vergleichbarkeit
- **Gender-Daten:** Eingeschränkt aufgrund Methodenänderungen
- **Vollständigkeit:** Zeitreihen meist ab 2010 verfügbar
- **Konsistenz:** Alle Dateien folgen Wissensbilanz-Standard

### Zähllogik
- **Köpfe:** Physische Personen, Mehrfachbeschäftigte nur einmal
- **VZÄ:** Mit Beschäftigungsausmaß gewichtet
- **Studierende vs. Studien:** Studierende mit mehreren Studien bei Studienzählung mehrfach erfasst

### Dateihinweise
- **Duplikate:** Dateien mit (1), (2) sind Varianten oder Updates
- **Interpretation:** Manche Dateien enthalten eigene Interpretation-Spalten
- **XLCubedFormats:** Sheet kann ignoriert werden (nur Formatierung)

### Stichtage
- **Strikt eingehalten:** Keine nachträglichen Korrekturen
- **Personal:** Immer 31.12. des jeweiligen Jahres
- **Studierende:** WS 15.11., SS 15.05.

## NEUE WISSENSBILANZ-KENNZAHLEN (SESSION 9)

### Kategorie 1-A: Personal und Gleichstellung

#### 1-A-2 Berufungen an die Universität
- Datei: 1-A-2 Berufungen an die Universität.xlsx
- Header-Row: 21
- Zeitreihen: Jahr 2024, 2023, 2022 / Studienjahr 2024/25, 2023/24, 2022/23
- Dimensionen: Frauen, Männer, Gesamt
- Struktur: Standard (read_excel_file)
- Filter-Dimensionen: Wissenschaftszweig, Herkunftsuni, Berufungsart

#### 1-A-3 Frauenquote in Kollegialorganen
- Datei: 1-A-3 Frauenquote in Kollegialorganen.xlsx
- Header-Row: 20
- Zeitreihen: Jahr 2024 / Studienjahr 2024/25
- Dimensionen: Köpfe Frauen, Köpfe Männer, Köpfe Gesamt, Frauen %, Männer %, Organe mit erfüllter Quote
- Struktur: Standard (read_excel_file)

#### 1-A-4 Gender pay gap
- Datei: 1-A-4 Gender pay gap.xlsx
- Header-Row: 20
- Zeitreihen: Jahr 2024, 2023, 2022 / Studienjahr 2024/25, 2023/24, 2022/23
- Dimensionen: Frauen, Männer, Gesamt, Gender pay gap (%)
- Struktur: Standard (read_excel_file)

#### 1-A-5 Repräsentanz von Frauen in Berufungsverfahren
- Datei: 1-A-5 Repräsentanz von Frauen in Berufungsverfahren.xlsx
- Header-Row: 19 (erste Tabelle), 33 (zweite Tabelle)
- Zeitreihen: Studienjahr 2024/25, 2023/24, 2022/23
- Dimensionen: Anzahl, Durchschnittlicher Frauenanteil %, Frauen, Männer, Gesamt
- Struktur: Spezial (read_name_based_file) - Universität als Filter
- Besonderheit: Mehrere Tabellen pro Sheet (Berufungskommission, 3er-Vorschlag, etc.)

### Kategorie 2-A: Studien und Studierende

#### 2-A-1 ProfessorInnen und Äquivalente
- Datei: 2-A-1 ProfessorInnen und Äquivalente.xlsx
- Header-Row: 23
- Zeitreihen: Jahr 2024, 2023, 2022 / Studienjahr 2023/24, 2023/24, 2022/23
- Dimensionen: ProfessorInnen und Äquivalente (Einzelwert)
- Struktur: Standard (read_excel_file)
- Anmerkung: Entfällt für Universität für Weiterbildung Krems

#### 2-A-2 Eingerichtete Studien
- Datei: 2-A-2 Eingerichtete Studien.xlsx
- Header-Row: 19
- Zeitreihen: Studienjahr 2024/25, 2023/24, 2022/23
- Dimensionen: Gesamt (Einzelwert)
- Struktur: Standard (read_excel_file)

#### 2-A-3 Studienabschlussquote
- Datei: 2-A-3 Studienabschlussquote.xlsx
- Header-Row: 18
- Zeitreihen: Implizit in Spalten
- Dimensionen: Quoten (Dezimalwerte 0-1)
- Struktur: Komplex (zusätzliche Logik erforderlich)
- Besonderheit: Daten ab Zeile 18, keine expliziten Jahre-Header
- Anmerkung: Entfällt für Universität für Weiterbildung Krems

#### 2-A-4 Besondere Zulassungsbedingungen
- Datei: 2-A-4 Besondere Zulassungsbedingungen.xlsx
- Header-Row: 25
- Zeitreihen: Jahr 2024, 2023, 2022 / Studienjahr 2024/25, 2023/24, 2022/23
- Dimensionen: Frauen, Männer, Gesamt
- Struktur: Standard (read_excel_file)
- Filter: Zugangsgeregelte Studien, DQ-Status
- Anmerkung: Entfällt für Universität für Weiterbildung Krems

#### 2-A-5 Anzahl Studierenden
- Datei: 2-A-5 Anzahl Studierenden.xlsx
- Header-Row: 18
- Zeitreihen: Implizit in Spalten (Semester-Spalten)
- Dimensionen: Ordentliche Studierende, Neuzugelassene, etc.
- Struktur: Komplex (Subkategorie in Zeile 9)
- Besonderheit: Mehrere Measures

#### 2-A-6 Anzahl Prüfungsaktive
- Datei: 2-A-6 Anzahl Prüfungsaktive.xlsx
- Header-Row: 18
- Zeitreihen: Implizit in Spalten
- Dimensionen: Dezimalwerte (gewichtete Studierendenzahlen)
- Struktur: Komplex (Subkategorie in Zeile 9: Studienart)

#### 2-A-7 Anzahl belegte ordentliche Studien
- Datei: 2-A-7 Anzahl belegte ordentliche Studien.xlsx
- Header-Row: 20
- Zeitreihen: Wintersemester 2024, 2023, 2022 (mit Stichtag)
- Dimensionen: Ordentliche Studien (Einzelwert)
- Struktur: Standard (read_excel_file)
- Subkategorie: ISCED2013 1.Ebene

#### 2-A-7 Anzahl belegte Universitätslehrgänge
- Datei: 2-A-7 Anzahl belegte Universitätslehrgänge.xlsx
- Header-Row: 17
- Zeitreihen: Wintersemester 2024, 2023, 2022 (in Zeilen statt Spalten)
- Dimensionen: Staatengruppe (Gesamt, Österreich, EU, Drittstaaten) als Subzeilen
- Struktur: Spezial (read_name_based_file)
- Besonderheit: Nur Universität für Weiterbildung Krems, Zeitreihe in Zeilen

#### 2-A-8 Ordentliche Studierende (outgoing)
- Datei: 2-A-8 Ordentliche Studierende (outgoing).xlsx
- Header-Row: 21
- Zeitreihen: Studienjahr 2023/24, 2022/23
- Dimensionen: EU, Drittstaaten, Gesamt
- Struktur: Standard (read_excel_file)
- Anmerkung: Entfällt für Universität für Weiterbildung Krems

#### 2-A-9 Ordentliche Studierende (incoming)
- Datei: 2-A-9 Ordentliche Studierende (incoming).xlsx
- Header-Row: 21
- Zeitreihen: Studienjahr 2023/24, 2022/23
- Dimensionen: EU, Drittstaaten, Gesamt
- Struktur: Standard (read_excel_file)
- Anmerkung: Entfällt für Universität für Weiterbildung Krems

### Kategorie 2-B: Doktoratsstudierende

#### 2-B-1 Doktoratsstudierende mit BV zur Universität
- Datei: 2-B-1 Doktoratsstudierende mit BV zur Universität.xlsx
- Header-Row: 20
- Zeitreihen: Jahr 2024, 2023, 2022 / Studienjahr 2024/25, 2023/24, 2022/23
- Dimensionen: Frauen, Männer, Gesamt
- Struktur: Standard (read_excel_file)

### Kategorie 3-A: Studienabschlüsse

#### 3-A-1 Außerordentliche Studienabschlüsse
- Datei: 3-A-1 Außerordentliche Studienabschlüsse.xlsx
- Noch nicht analysiert (separate Session geplant)

#### 3-A-1 Ordentliche Studienabschlüsse
- Datei: 3-A-1 Ordentliche Studienabschlüsse.xlsx
- Noch nicht analysiert (separate Session geplant)

#### 3-A-2 Studienabschlüsse in der Toleranzstudiendauer
- Datei: 3-A-2 Studienabschlüsse in der Toleranzstudiendauer.xlsx
- Noch nicht analysiert (separate Session geplant)

#### 3-A-3 Studienabschlüsse mit studienbezogenem Auslandsaufenthalt
- Datei: 3-A-3 Studienabschlüsse mit studienbezogenem Auslandsaufenthalt.xlsx
- Noch nicht analysiert (separate Session geplant)

## GEMEINSAME MUSTER NEUER DATEIEN

### Excel-Struktur
- Sheet-Name: "Tab" (Daten), "XLCubedFormats" (Formatierung)
- Zeilen 1-8: Titel (Wissensbilanz, Kennzahl, Beschreibung, Quelle, Datenprüfung, Anmerkung)
- Interpretation-Spalten: Nach jedem Zeitraum (ignorierbar)

### Header-Row-Position
- Variable Position: Zeile 17-25
- Identifikation: Zeile mit "Universität (Codex)" in Spalte 1

### Zeitreihen-Formate
- Jahr: 2024, 2023, 2022 (4-stellig)
- Studienjahr: 2024/25, 2023/24, 2022/23 (Format: YYYY/YY)
- Semester: "Wintersemester 2024 (Stichtag: DD.MM.YYYY)"

### Dimensionen
- Geschlecht: Frauen, Männer, Gesamt
- Herkunft: Österreich, EU, Drittstaaten, Gesamt
- Studienart: Bachelor, Diplom, Master, Doktorat

### Parsing-Strategien

Standard (read_excel_file) - 12 Dateien:
- 1-A-2 Berufungen an die Universität
- 1-A-3 Frauenquote in Kollegialorganen
- 1-A-4 Gender pay gap
- 2-A-1 ProfessorInnen und Äquivalente
- 2-A-2 Eingerichtete Studien
- 2-A-4 Besondere Zulassungsbedingungen
- 2-A-7 Anzahl belegte ordentliche Studien
- 2-A-8 Ordentliche Studierende (outgoing)
- 2-A-9 Ordentliche Studierende (incoming)
- 2-B-1 Doktoratsstudierende mit BV zur Universität
- 3-A-1 Außerordentliche Studienabschlüsse
- 3-A-1 Ordentliche Studienabschlüsse

Spezial (read_name_based_file) - 2 Dateien:
- 1-A-5 Repräsentanz von Frauen in Berufungsverfahren (mehrere Tabellen pro Sheet)
- 2-A-7 Anzahl belegte Universitätslehrgänge (nur UR, Zeitreihe in Zeilen)

Komplex (neue Logik erforderlich) - 3 Dateien:
- 2-A-3 Studienabschlussquote (keine expliziten Jahre-Header)
- 2-A-5 Anzahl Studierenden (mehrere Measures)
- 2-A-6 Anzahl Prüfungsaktive (Subkategorien in Zeile 9)

Nicht analysiert - 2 Dateien:
- 3-A-2 Studienabschlüsse in der Toleranzstudiendauer
- 3-A-3 Studienabschlüsse mit studienbezogenem Auslandsaufenthalt

### Implementierungsstrategie

Phase 1: Standard-Dateien (read_excel_file)
- Bestehende Parsing-Funktion kann verwendet werden
- Header-Detection: "Universität (Codex)" in Spalte 1, Zeile 17-25
- Zeitreihen-Extraktion: extractYearValues() kompatibel
- Geschätzte Entwicklungszeit: 2-3h

Phase 2: Spezial-Dateien (read_name_based_file)
- Universitätsname statt Code als Identifier
- 1-A-5: Mehrere Tabellen pro Sheet (Berufungskommission, 3er-Vorschlag)
- 2-A-7 Lehrgänge: Nur UR, Zeitreihe in Zeilen statt Spalten
- Geschätzte Entwicklungszeit: 3-4h

Phase 3: Komplexe Dateien
- Individuelle Parsing-Logik erforderlich
- 2-A-3: Quoten-Berechnung ohne explizite Jahre-Header
- 2-A-5: Mehrere Measures (Studierende, Neuzulassungen) in einer Datei
- 2-A-6: Studienart-Subkategorien in Zeile 9
- Geschätzte Entwicklungszeit: 4-6h