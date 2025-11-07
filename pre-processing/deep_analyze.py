import pandas as pd
from pathlib import Path
import json

data_folder = Path("data")
excel_files = sorted(data_folder.glob("*.xlsx"))

results = {}

print("Tiefenanalyse aller Excel-Dateien...")
print(f"Anzahl Dateien: {len(excel_files)}\n")

for idx, file in enumerate(excel_files, 1):
    print(f"[{idx}/{len(excel_files)}] {file.name}")

    try:
        excel_file = pd.ExcelFile(file)

        file_info = {
            "filename": file.name,
            "sheets_count": len(excel_file.sheet_names),
            "sheets": []
        }

        for sheet_name in excel_file.sheet_names:
            if sheet_name in ["XLCubedFormats", "Tabelle2"]:
                continue

            df = pd.read_excel(file, sheet_name=sheet_name, header=None)

            # Extrahiere Metadaten aus den ersten Zeilen
            metadata = {
                "sheet_name": sheet_name,
                "total_rows": df.shape[0],
                "total_cols": df.shape[1],
                "title_lines": [],
                "data_start_row": 0,
                "header_row": 0,
                "columns": [],
                "sample_data": [],
                "unique_values": {}
            }

            # Erste 10 Zeilen für Titel/Metadaten
            for i in range(min(10, len(df))):
                row_text = " ".join([str(x) for x in df.iloc[i] if pd.notna(x) and str(x).strip()])
                if row_text:
                    metadata["title_lines"].append(row_text)

            # Finde Header-Zeile (erste Zeile mit mehreren gefüllten Zellen)
            for i in range(min(25, len(df))):
                non_null_count = df.iloc[i].notna().sum()
                if non_null_count >= 3:
                    metadata["header_row"] = i
                    metadata["data_start_row"] = i + 1
                    # Extrahiere Spaltennamen
                    headers = df.iloc[i].fillna("").astype(str).tolist()
                    metadata["columns"] = [h.strip() for h in headers if h.strip() and not h.startswith("Unnamed")]
                    break

            # Lade Daten neu mit korrektem Header
            if metadata["header_row"] > 0:
                try:
                    df_data = pd.read_excel(file, sheet_name=sheet_name, header=metadata["header_row"])

                    # Sample der ersten Datenzeilen
                    sample_rows = min(5, len(df_data))
                    if sample_rows > 0:
                        for i in range(sample_rows):
                            row_dict = {}
                            for col in df_data.columns:
                                val = df_data.iloc[i][col]
                                if pd.notna(val):
                                    row_dict[str(col)] = str(val)
                            if row_dict:
                                metadata["sample_data"].append(row_dict)

                    # Analysiere kategorische Spalten
                    for col in df_data.columns:
                        if df_data[col].dtype == 'object':
                            unique_vals = df_data[col].dropna().unique()
                            if 1 < len(unique_vals) <= 50:
                                col_name = str(col)
                                if len(col_name) < 100:  # Nur sinnvolle Spaltennamen
                                    metadata["unique_values"][col_name] = sorted([str(v) for v in unique_vals])[:20]

                    metadata["actual_data_rows"] = len(df_data)

                except Exception as e:
                    metadata["data_load_error"] = str(e)

            file_info["sheets"].append(metadata)

        results[file.name] = file_info

    except Exception as e:
        print(f"  FEHLER: {e}")
        results[file.name] = {"error": str(e)}

# Speichere detaillierte Ergebnisse
output_file = "data_deep_analysis.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nAnalyse abgeschlossen. Ergebnisse in {output_file}")
