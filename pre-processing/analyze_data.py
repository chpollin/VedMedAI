import os
import pandas as pd
from pathlib import Path

# Ordner mit den Daten
data_folder = Path("data")

# Liste aller Excel-Dateien
excel_files = list(data_folder.glob("*.xlsx"))

print(f"Gefundene Excel-Dateien: {len(excel_files)}\n")
print("="*80)

# Kleine Analyse: Erste 3 Dateien im Detail
for i, file in enumerate(excel_files[:3]):
    print(f"\n{i+1}. Datei: {file.name}")
    print("-"*80)

    try:
        # Excel-Datei laden
        excel_file = pd.ExcelFile(file)

        print(f"   Anzahl Sheets: {len(excel_file.sheet_names)}")
        print(f"   Sheet-Namen: {', '.join(excel_file.sheet_names)}")

        # Erstes Sheet laden
        df = pd.read_excel(file, sheet_name=0)
        print(f"\n   Dimensionen (Zeilen x Spalten): {df.shape}")
        print(f"   Spalten: {list(df.columns)}")
        print(f"\n   Erste 3 Zeilen:")
        print(df.head(3).to_string())

    except Exception as e:
        print(f"   Fehler beim Lesen: {e}")

print("\n" + "="*80)
print("\nDatei-Kategorien (basierend auf Namen):")
print("-"*80)

# Kategorisierung nach Dateinamen
categories = {}
for file in excel_files:
    name = file.name
    if "Personal" in name or "Funktion" in name or "Berufung" in name:
        category = "Personal & Mitarbeiter"
    elif "Neuzugelassen" in name:
        category = "Neuzulassungen"
    elif "Studierende" in name:
        category = "Studierende"
    elif "Studien" in name:
        category = "Studien & Programme"
    elif "Abschluss" in name or "Abschlüsse" in name:
        category = "Studienabschlüsse"
    elif "Mobilität" in name:
        category = "Mobilität"
    elif "Nutzfläche" in name or "Lehrlinge" in name:
        category = "Infrastruktur & Ressourcen"
    elif "Altersverteilung" in name:
        category = "Demographie"
    elif "Gender" in name or "Frauen" in name:
        category = "Gender & Diversität"
    else:
        category = "Sonstige"

    if category not in categories:
        categories[category] = []
    categories[category].append(name)

for category, files in sorted(categories.items()):
    print(f"\n{category} ({len(files)} Dateien):")
    for f in sorted(files)[:5]:  # Nur erste 5 pro Kategorie anzeigen
        print(f"  - {f}")
    if len(files) > 5:
        print(f"  ... und {len(files)-5} weitere")
