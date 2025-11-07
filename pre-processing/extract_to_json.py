import os
import pandas as pd
from pathlib import Path
import json

data_folder = Path("data")
output_folder = Path("docs/data")
output_folder.mkdir(parents=True, exist_ok=True)

def extract_meta():
    """Extrahiert Metadaten: Universitäten-Codex, Dimensionen, Klassifikationen"""
    meta = {
        "universities": {
            "UA": "Universität Wien",
            "UB": "Universität Graz",
            "UC": "Universität Innsbruck",
            "UD": "Universität Salzburg",
            "UE": "Universität Klagenfurt",
            "UF": "Universität Linz",
            "UG": "Technische Universität Wien",
            "UH": "Technische Universität Graz",
            "UI": "Montanuniversität Leoben",
            "UJ": "Universität für Bodenkultur Wien",
            "UK": "Universität für künstlerische und industrielle Gestaltung Linz",
            "UL": "Universität Mozarteum Salzburg",
            "UM": "Universität für Musik und darstellende Kunst Wien",
            "UN": "Universität für Musik und darstellende Kunst Graz",
            "UO": "Akademie der bildenden Künste Wien",
            "UQ": "Universität für angewandte Kunst Wien",
            "UR": "Universität für Weiterbildung Krems",
            "US": "Medizinische Universität Wien",
            "UT": "Medizinische Universität Graz",
            "UU": "Medizinische Universität Innsbruck",
            "UV": "Veterinärmedizinische Universität Wien",
            "UW": "Wirtschaftsuniversität Wien"
        },
        "dimensions": {
            "altersklassen": ["18-21", "22-25", "26-30", "31-35", "36-40", "41-45", "46-50", "51+"],
            "universitaetsreife": [
                "AHS-Matura",
                "BHS-Matura",
                "Studienberechtigungsprüfung",
                "Berufsreifeprüfung",
                "Sonstige österreichische Zulassung",
                "EWR-Reifezeugnis",
                "Sonstige ausländische Zulassung"
            ],
            "studiengruppen_national": [
                "Geisteswissenschaften",
                "Naturwissenschaften",
                "Sozial- und Wirtschaftswissenschaften",
                "Rechtswissenschaften",
                "Medizin",
                "Technik",
                "Kunst"
            ],
            "studienarten": ["Bachelor", "Master", "Diplom", "Doktorat/PhD"],
            "bundeslaender": [
                "Wien", "Niederösterreich", "Burgenland", "Oberösterreich",
                "Salzburg", "Steiermark", "Kärnten", "Tirol", "Vorarlberg"
            ],
            "kontinente": ["Europa", "Nordamerika", "Südamerika", "Asien", "Afrika", "Ozeanien"]
        },
        "years": [2022, 2023, 2024],
        "stichtage": {
            "personal": "31.12.",
            "studierende_ws": "15.11.",
            "studierende_ss": "15.05."
        },
        "klassifikationen": {
            "UHSBV": "Universitäts-Haushalts- und Stellenplanverordnung",
            "WBV": "Wissensbilanz-Verordnung",
            "ISCED": "International Standard Classification of Education (UNESCO 2013)",
            "ISCED_F_99": "ISCED Fields of Education and Training 2013 (99 Felder)",
            "UG": "Universitätsgesetz"
        }
    }

    with open(output_folder / "meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print("meta.json erstellt")


def find_header_and_data_start(df):
    """Findet Header-Zeile und Datenstart"""
    for i in range(min(25, len(df))):
        non_null = df.iloc[i].notna().sum()
        if non_null >= 3:
            row_text = ' '.join([str(x) for x in df.iloc[i] if pd.notna(x)])
            if any(year in row_text for year in ['2024', '2023', '2022', 'WS', 'Universität']):
                return i, i + 1
    return 0, 1


def extract_university_code(value):
    """Extrahiert Universitätscode"""
    if pd.notna(value):
        val_str = str(value).strip()
        if len(val_str) == 2 and val_str.startswith("U") and val_str[1].isalpha():
            return val_str
    return None


def read_excel_file(file_path):
    """Liest Excel-Datei und gibt Daten strukturiert zurück"""
    try:
        df_raw = pd.read_excel(file_path, sheet_name="Tab", header=None)

        header_row = None
        for i in range(min(25, len(df_raw))):
            if pd.notna(df_raw.iloc[i, 0]) and "Universität" in str(df_raw.iloc[i, 0]):
                if pd.notna(df_raw.iloc[i, 1]) and "Codex" in str(df_raw.iloc[i, 1]):
                    header_row = i
                    break

        if header_row is None:
            return {}

        df = pd.read_excel(file_path, sheet_name="Tab", header=header_row)

        result = {}
        current_uni = None

        for idx, row in df.iterrows():
            uni_code = extract_university_code(row.iloc[1] if len(row) > 1 else None)

            if uni_code:
                current_uni = uni_code
                if current_uni not in result:
                    result[current_uni] = {}

            if current_uni and len(row) >= 4:
                kategorie = str(row.iloc[3]) if pd.notna(row.iloc[3]) else None

                if kategorie and kategorie != 'nan':
                    kategorie_clean = kategorie.strip()

                    for col_idx in range(4, len(row)):
                        val = row.iloc[col_idx]
                        if pd.notna(val) and isinstance(val, (int, float)):
                            col_name = str(df.columns[col_idx])
                            if kategorie_clean not in result[current_uni]:
                                result[current_uni][kategorie_clean] = {}
                            result[current_uni][kategorie_clean][col_name] = float(val)

        return result
    except Exception as e:
        print(f"Fehler bei {file_path.name}: {e}")
        import traceback
        traceback.print_exc()
        return {}


def extract_personal():
    """Extrahiert Personal-Daten"""
    personal_files = [
        "1-A-1 Personal - Köpfe.xlsx",
        "1-A-1 Personal - VZÄ.xlsx"
    ]

    data = {}

    for filename in personal_files:
        file_path = data_folder / filename
        if file_path.exists():
            key = "koepfe" if "Köpfe" in filename else "vzae"
            data[key] = read_excel_file(file_path)

    categories_folder = output_folder / "categories"
    categories_folder.mkdir(exist_ok=True)

    with open(categories_folder / "personal.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("categories/personal.json erstellt")


def extract_studierende():
    """Extrahiert Studierende-Daten"""
    studierende_files = [
        "Ordentliche Studierende nach Universitäten.xlsx"
    ]

    data = {}

    for filename in studierende_files:
        file_path = data_folder / filename
        if file_path.exists():
            data["ordentliche"] = read_excel_file(file_path)

    categories_folder = output_folder / "categories"
    categories_folder.mkdir(exist_ok=True)

    with open(categories_folder / "studierende.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("categories/studierende.json erstellt")


def extract_summary():
    """Extrahiert Top-Level KPIs für schnellen Überblick"""
    summary = {}

    personal_koepfe = data_folder / "1-A-1 Personal - Köpfe.xlsx"
    studierende = data_folder / "Ordentliche Studierende nach Universitäten.xlsx"

    if personal_koepfe.exists():
        personal_data = read_excel_file(personal_koepfe)
        for uni_code, categories in personal_data.items():
            if uni_code not in summary:
                summary[uni_code] = {}

            if "Wissenschaftliches und künstlerisches Personal" in categories:
                years = categories["Wissenschaftliches und künstlerisches Personal"]
                for year_label, value in years.items():
                    if "2024" in year_label:
                        summary[uni_code]["personal_koepfe"] = value
                        break

    if studierende.exists():
        studierende_data = read_excel_file(studierende)
        for uni_code, categories in studierende_data.items():
            if uni_code not in summary:
                summary[uni_code] = {}

            if categories:
                first_category = list(categories.values())[0]
                if isinstance(first_category, dict):
                    for year_label, value in first_category.items():
                        if "2024" in year_label:
                            summary[uni_code]["studierende"] = value
                            break

    with open(output_folder / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print("summary.json erstellt")


def main():
    print("Starte JSON-Extraktion...\n")

    extract_meta()
    extract_summary()
    extract_personal()
    extract_studierende()

    print("\nExtraktion abgeschlossen")
    print(f"Ausgabe: {output_folder}/")


if __name__ == "__main__":
    main()
