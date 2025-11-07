import os
import pandas as pd
from pathlib import Path
import json
import argparse

data_folder = Path("data")

def overview_analysis():
    """Übersichtsanalyse aller Excel-Dateien"""
    excel_files = list(data_folder.glob("*.xlsx"))

    print(f"Gefundene Excel-Dateien: {len(excel_files)}\n")
    print("="*80)

    for i, file in enumerate(excel_files[:3]):
        print(f"\n{i+1}. Datei: {file.name}")
        print("-"*80)

        try:
            excel_file = pd.ExcelFile(file)
            print(f"   Anzahl Sheets: {len(excel_file.sheet_names)}")
            print(f"   Sheet-Namen: {', '.join(excel_file.sheet_names)}")

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
        for f in sorted(files)[:5]:
            print(f"  - {f}")
        if len(files) > 5:
            print(f"  ... und {len(files)-5} weitere")


def structure_analysis():
    """Strukturanalyse mit Extraktion von Metadaten"""
    excel_files = sorted(data_folder.glob("*.xlsx"))
    results = {}

    print("Strukturanalyse aller Excel-Dateien...\n")

    for file in excel_files:
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
                df_clean = df.dropna(axis=1, how='all')

                title_rows = []
                for i in range(min(5, len(df))):
                    row_vals = df.iloc[i].dropna().astype(str).tolist()
                    if row_vals:
                        title_rows.append(" ".join(row_vals))

                header_row = None
                data_start = 0
                for i in range(min(20, len(df))):
                    non_null = df.iloc[i].notna().sum()
                    if non_null >= 3:
                        header_row = i
                        data_start = i + 1
                        break

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
            results[file.name] = {"error": str(e)}

    output_file = "pre-processing/data_structure.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"Strukturanalyse abgeschlossen. Ergebnisse in {output_file}")


def deep_analysis():
    """Tiefenanalyse mit vollständiger Datenextraktion"""
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

                for i in range(min(10, len(df))):
                    row_text = " ".join([str(x) for x in df.iloc[i] if pd.notna(x) and str(x).strip()])
                    if row_text:
                        metadata["title_lines"].append(row_text)

                for i in range(min(25, len(df))):
                    non_null_count = df.iloc[i].notna().sum()
                    if non_null_count >= 3:
                        metadata["header_row"] = i
                        metadata["data_start_row"] = i + 1
                        headers = df.iloc[i].fillna("").astype(str).tolist()
                        metadata["columns"] = [h.strip() for h in headers if h.strip() and not h.startswith("Unnamed")]
                        break

                if metadata["header_row"] > 0:
                    try:
                        df_data = pd.read_excel(file, sheet_name=sheet_name, header=metadata["header_row"])

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

                        for col in df_data.columns:
                            if df_data[col].dtype == 'object':
                                unique_vals = df_data[col].dropna().unique()
                                if 1 < len(unique_vals) <= 50:
                                    col_name = str(col)
                                    if len(col_name) < 100:
                                        metadata["unique_values"][col_name] = sorted([str(v) for v in unique_vals])[:20]

                        metadata["actual_data_rows"] = len(df_data)

                    except Exception as e:
                        metadata["data_load_error"] = str(e)

                file_info["sheets"].append(metadata)

            results[file.name] = file_info

        except Exception as e:
            print(f"  FEHLER: {e}")
            results[file.name] = {"error": str(e)}

    output_file = "pre-processing/data_deep_analysis.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\nAnalyse abgeschlossen. Ergebnisse in {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Analyse Excel-Dateien im data/ Ordner')
    parser.add_argument('mode', choices=['overview', 'structure', 'deep', 'all'],
                       help='Analysemodus: overview (Übersicht), structure (Struktur), deep (Tiefenanalyse), all (alles)')

    args = parser.parse_args()

    if args.mode == 'overview':
        overview_analysis()
    elif args.mode == 'structure':
        structure_analysis()
    elif args.mode == 'deep':
        deep_analysis()
    elif args.mode == 'all':
        print("\n=== ÜBERSICHTSANALYSE ===\n")
        overview_analysis()
        print("\n\n=== STRUKTURANALYSE ===\n")
        structure_analysis()
        print("\n\n=== TIEFENANALYSE ===\n")
        deep_analysis()


if __name__ == "__main__":
    main()
