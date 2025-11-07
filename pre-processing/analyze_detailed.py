import os
import pandas as pd
from pathlib import Path
import json

data_folder = Path("data")
excel_files = sorted(data_folder.glob("*.xlsx"))

results = {}

print("Detaillierte Analyse aller Excel-Dateien...\n")

for file in excel_files:
    print(f"Analysiere: {file.name}")

    try:
        excel_file = pd.ExcelFile(file)

        file_info = {
            "filename": file.name,
            "sheets": [],
            "total_sheets": len(excel_file.sheet_names)
        }

        for sheet_name in excel_file.sheet_names:
            if sheet_name in ["XLCubedFormats", "Tabelle2"]:
                continue

            df = pd.read_excel(file, sheet_name=sheet_name)

            # Bereinige leere Spalten
            df_clean = df.dropna(axis=1, how='all')

            # Extrahiere Titel aus ersten Zeilen
            title_rows = []
            for i in range(min(5, len(df))):
                row_vals = df.iloc[i].dropna().astype(str).tolist()
                if row_vals:
                    title_rows.append(" ".join(row_vals))

            # Finde Daten-Header (erste Zeile mit mehreren nicht-leeren Werten)
            header_row = None
            data_start = 0
            for i in range(min(20, len(df))):
                non_null = df.iloc[i].notna().sum()
                if non_null >= 3:
                    header_row = i
                    data_start = i + 1
                    break

            # Extrahiere echte Spalten
            if header_row is not None:
                actual_columns = df.iloc[header_row].fillna("").astype(str).tolist()
            else:
                actual_columns = df.columns.tolist()

            sheet_info = {
                "name": sheet_name,
                "dimensions": f"{df.shape[0]} × {df.shape[1]}",
                "title": title_rows[0] if title_rows else "",
                "columns": [col for col in actual_columns if col and not col.startswith("Unnamed")],
                "data_rows": df.shape[0] - data_start if header_row else df.shape[0]
            }

            file_info["sheets"].append(sheet_info)

        results[file.name] = file_info

    except Exception as e:
        print(f"  Fehler: {e}")
        results[file.name] = {"error": str(e)}

# Speichere Ergebnisse
with open("data_structure.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\n✓ Analyse abgeschlossen. Ergebnisse in data_structure.json gespeichert.")
