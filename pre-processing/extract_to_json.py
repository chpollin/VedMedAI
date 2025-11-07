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


def read_name_based_file(file_path, category_name="Gesamt"):
    """Liest Excel-Dateien mit Universitätsnamen und Frauen/Männer/Gesamt Spalten"""
    try:
        df_raw = pd.read_excel(file_path, sheet_name="Tab", header=None)

        header_row = None
        for i in range(min(30, len(df_raw))):
            if pd.notna(df_raw.iloc[i, 0]) and "Universität" in str(df_raw.iloc[i, 0]):
                header_row = i
                break

        if header_row is None:
            return {}

        df = pd.read_excel(file_path, sheet_name="Tab", header=header_row)

        columns_clean = []
        for i, col in enumerate(df.columns):
            if i == 0:
                columns_clean.append("Universität")
            elif "Frauen" in str(col) or i == 1:
                columns_clean.append("Frauen")
            elif "Männer" in str(col) or "M�nner" in str(col) or i == 2:
                columns_clean.append("Männer")
            elif i == 3:
                columns_clean.append("Gesamt")
            else:
                columns_clean.append(str(col))

        df.columns = columns_clean

        name_to_code = {
            "Universität Wien": "UA",
            "Universität Graz": "UB",
            "Universität Innsbruck": "UC",
            "Universität Salzburg": "UD",
            "Universität Klagenfurt": "UE",
            "Universität Linz": "UF",
            "Technische Universität Wien": "UG",
            "Technische Universität Graz": "UH",
            "Montanuniversität Leoben": "UI",
            "Universität für Bodenkultur Wien": "UJ",
            "Universität für künstlerische und industrielle Gestaltung Linz": "UK",
            "Universität Mozarteum Salzburg": "UL",
            "Universität für Musik und darstellende Kunst Wien": "UM",
            "Universität für Musik und darstellende Kunst Graz": "UN",
            "Akademie der bildenden Künste Wien": "UO",
            "Universität für angewandte Kunst Wien": "UQ",
            "Universität für Weiterbildung Krems": "UR",
            "Medizinische Universität Wien": "US",
            "Medizinische Universität Graz": "UT",
            "Medizinische Universität Innsbruck": "UU",
            "Veterinärmedizinische Universität Wien": "UV",
            "Wirtschaftsuniversität Wien": "UW"
        }

        result = {}

        for idx, row in df.iterrows():
            uni_name = str(row.iloc[0]) if pd.notna(row.iloc[0]) else None

            if uni_name and uni_name in name_to_code:
                uni_code = name_to_code[uni_name]

                if uni_code not in result:
                    result[uni_code] = {}

                if category_name not in result[uni_code]:
                    result[uni_code][category_name] = {}

                for col_name in ["Frauen", "Männer", "Gesamt"]:
                    if col_name in df.columns:
                        val = row[col_name]
                        if pd.notna(val) and isinstance(val, (int, float)):
                            result[uni_code][category_name][col_name] = float(val)

        return result
    except Exception as e:
        print(f"Fehler bei {file_path.name}: {e}")
        import traceback
        traceback.print_exc()
        return {}


def extract_studierende():
    """Extrahiert Studierende-Daten"""
    data = {}

    studierende_zeitreihe = data_folder / "Ordentliche Studierende an Universitäten - Zeitreihe Wintersemester.xlsx"
    if studierende_zeitreihe.exists():
        zeitreihe_data = read_excel_file(studierende_zeitreihe)
        if zeitreihe_data:
            data["zeitreihe"] = zeitreihe_data

    studierende_gesamt = data_folder / "Ordentliche Studierende nach Universitäten.xlsx"
    if studierende_gesamt.exists():
        gesamt_data = read_name_based_file(studierende_gesamt, "Ordentliche Studierende")
        if gesamt_data:
            data["gesamt"] = gesamt_data

    studierende_altersklassen = data_folder / "Ordentliche Studierende an Universitäten nach Altersklassen.xlsx"
    if studierende_altersklassen.exists():
        altersklassen_data = read_excel_file(studierende_altersklassen)
        if altersklassen_data:
            data["altersklassen"] = altersklassen_data

    studierende_unireife = data_folder / "Ordentliche Studierende an Universitäten nach Form der allgemeinen Universitätsreife.xlsx"
    if studierende_unireife.exists():
        unireife_data = read_excel_file(studierende_unireife)
        if unireife_data:
            data["universitaetsreife"] = unireife_data

    studierende_herkunft = data_folder / "Inländische ordentliche Studierende nach regionaler Herkunft.xlsx"
    if studierende_herkunft.exists():
        herkunft_data = read_excel_file(studierende_herkunft)
        if herkunft_data:
            data["bundeslaender"] = herkunft_data

    categories_folder = output_folder / "categories"
    categories_folder.mkdir(exist_ok=True)

    with open(categories_folder / "studierende.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("categories/studierende.json erstellt")


def extract_summary():
    """Extrahiert Top-Level KPIs für schnellen Überblick (nur 2024-Werte)"""
    summary = {}

    personal_koepfe = data_folder / "1-A-1 Personal - Köpfe.xlsx"
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

    studierende = data_folder / "Ordentliche Studierende nach Universitäten.xlsx"
    if studierende.exists():
        studierende_data = read_name_based_file(studierende, "Ordentliche Studierende")
        for uni_code, categories in studierende_data.items():
            if uni_code not in summary:
                summary[uni_code] = {}
            if "Ordentliche Studierende" in categories:
                values = categories["Ordentliche Studierende"]
                if "Gesamt" in values:
                    summary[uni_code]["studierende"] = values["Gesamt"]

    neuzulassungen = data_folder / "Ordentliche Neuzugelassene nach Universitäten.xlsx"
    if neuzulassungen.exists():
        neuzulassungen_data = read_name_based_file(neuzulassungen, "Ordentliche Neuzugelassene")
        for uni_code, categories in neuzulassungen_data.items():
            if uni_code not in summary:
                summary[uni_code] = {}
            if "Ordentliche Neuzugelassene" in categories:
                values = categories["Ordentliche Neuzugelassene"]
                if "Gesamt" in values:
                    summary[uni_code]["neuzulassungen"] = values["Gesamt"]

    studien = data_folder / "Ordentliche Studien nach Universitäten.xlsx"
    if studien.exists():
        studien_data = read_name_based_file(studien, "Ordentliche Studien")
        for uni_code, categories in studien_data.items():
            if uni_code not in summary:
                summary[uni_code] = {}
            if "Ordentliche Studien" in categories:
                values = categories["Ordentliche Studien"]
                if "Gesamt" in values:
                    summary[uni_code]["studien"] = values["Gesamt"]

    abschluesse = data_folder / "Studienabschlüsse nach Universitäten.xlsx"
    if abschluesse.exists():
        abschluesse_data = read_name_based_file(abschluesse, "Ordentliche Studienabschlüsse")
        for uni_code, categories in abschluesse_data.items():
            if uni_code not in summary:
                summary[uni_code] = {}
            if "Ordentliche Studienabschlüsse" in categories:
                values = categories["Ordentliche Studienabschlüsse"]
                if "Gesamt" in values:
                    summary[uni_code]["abschluesse"] = values["Gesamt"]

    mobilitaet = data_folder / "Studierendenmobilität nach Universitäten - Outgoing.xlsx"
    if mobilitaet.exists():
        mobilitaet_data = read_name_based_file(mobilitaet, "Outgoing-Studierende")
        for uni_code, categories in mobilitaet_data.items():
            if uni_code not in summary:
                summary[uni_code] = {}
            if "Outgoing-Studierende" in categories:
                values = categories["Outgoing-Studierende"]
                if "Gesamt" in values:
                    summary[uni_code]["mobilitaet"] = values["Gesamt"]

    infrastruktur = data_folder / "Nutzfläche nach Universitäten.xlsx"
    if infrastruktur.exists():
        infrastruktur_data = read_excel_file(infrastruktur)
        for uni_code, categories in infrastruktur_data.items():
            if uni_code not in summary:
                summary[uni_code] = {}
            for kategorie, years in categories.items():
                if "Nutzfläche" in kategorie:
                    for year_label, value in years.items():
                        if "2024" in year_label:
                            summary[uni_code]["infrastruktur"] = value
                            break

    with open(output_folder / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print("summary.json erstellt")


def extract_neuzulassungen():
    """Extrahiert Neuzulassungen-Daten"""
    data = {}

    neuzulassungen_zeitreihe = data_folder / "Ordentliche Neuzugelassene an Universitäten - Zeitreihe.xlsx"
    if neuzulassungen_zeitreihe.exists():
        zeitreihe_data = read_excel_file(neuzulassungen_zeitreihe)
        if zeitreihe_data:
            data["zeitreihe"] = zeitreihe_data

    neuzulassungen_gesamt = data_folder / "Ordentliche Neuzugelassene nach Universitäten.xlsx"
    if neuzulassungen_gesamt.exists():
        gesamt_data = read_name_based_file(neuzulassungen_gesamt, "Ordentliche Neuzugelassene")
        if gesamt_data:
            data["gesamt"] = gesamt_data

    neuzulassungen_altersklassen = data_folder / "Ordentliche Neuzugelassene an Universitäten nach Altersklassen.xlsx"
    if neuzulassungen_altersklassen.exists():
        altersklassen_data = read_excel_file(neuzulassungen_altersklassen)
        if altersklassen_data:
            data["altersklassen"] = altersklassen_data

    neuzulassungen_unireife = data_folder / "Ordentliche Neuzugelassene an Universitäten nach Form der allgemeinen Universitätsreife.xlsx"
    if neuzulassungen_unireife.exists():
        unireife_data = read_excel_file(neuzulassungen_unireife)
        if unireife_data:
            data["universitaetsreife"] = unireife_data

    neuzulassungen_herkunft = data_folder / "Inländische ordentliche Neuzugelassene nach regionaler Herkunft.xlsx"
    if neuzulassungen_herkunft.exists():
        herkunft_data = read_excel_file(neuzulassungen_herkunft)
        if herkunft_data:
            data["bundeslaender"] = herkunft_data

    categories_folder = output_folder / "categories"
    categories_folder.mkdir(exist_ok=True)

    with open(categories_folder / "neuzulassungen.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("categories/neuzulassungen.json erstellt")


def extract_studien():
    """Extrahiert Studien-Daten"""
    data = {}

    studien_zeitreihe = data_folder / "Ordentliche Studien - Zeitreihe Wintersemester.xlsx"
    if studien_zeitreihe.exists():
        zeitreihe_data = read_excel_file(studien_zeitreihe)
        if zeitreihe_data:
            data["zeitreihe"] = zeitreihe_data

    studien_gesamt = data_folder / "Ordentliche Studien nach Universitäten.xlsx"
    if studien_gesamt.exists():
        gesamt_data = read_name_based_file(studien_gesamt, "Ordentliche Studien")
        if gesamt_data:
            data["gesamt"] = gesamt_data

    studien_national = data_folder / "Ordentliche Studien nach nationalen Gruppen von Studien.xlsx"
    if studien_national.exists():
        national_data = read_excel_file(studien_national)
        if national_data:
            data["studiengruppen_national"] = national_data

    studien_international = data_folder / "Ordentliche Studien nach internationalen Gruppen von Studien.xlsx"
    if studien_international.exists():
        international_data = read_excel_file(studien_international)
        if international_data:
            data["studiengruppen_international"] = international_data

    studien_art = data_folder / "Ordentliche Studien nach Studienart.xlsx"
    if studien_art.exists():
        art_data = read_excel_file(studien_art)
        if art_data:
            data["studienarten"] = art_data

    studien_unireife = data_folder / "Ordentliche Studien an Universitäten nach Form der allgemeinen Universitätsreife.xlsx"
    if studien_unireife.exists():
        unireife_data = read_excel_file(studien_unireife)
        if unireife_data:
            data["universitaetsreife"] = unireife_data

    categories_folder = output_folder / "categories"
    categories_folder.mkdir(exist_ok=True)

    with open(categories_folder / "studien.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("categories/studien.json erstellt")


def extract_abschluesse():
    """Extrahiert Abschlüsse-Daten"""
    data = {}

    abschluesse_zeitreihe = data_folder / "Studienabschlüsse an Universitäten - Zeitreihe Studienjahr.xlsx"
    if abschluesse_zeitreihe.exists():
        zeitreihe_data = read_excel_file(abschluesse_zeitreihe)
        if zeitreihe_data:
            data["zeitreihe"] = zeitreihe_data

    abschluesse_gesamt = data_folder / "Studienabschlüsse nach Universitäten.xlsx"
    if abschluesse_gesamt.exists():
        gesamt_data = read_name_based_file(abschluesse_gesamt, "Ordentliche Studienabschlüsse")
        if gesamt_data:
            data["gesamt"] = gesamt_data

    categories_folder = output_folder / "categories"
    categories_folder.mkdir(exist_ok=True)

    with open(categories_folder / "abschluesse.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("categories/abschluesse.json erstellt")


def extract_mobilitaet():
    """Extrahiert Mobilitäts-Daten"""
    data = {}

    mobilitaet_zeitreihe = data_folder / "Studierendenmobilität an Universitäten - Outgoing - Zeitreihe.xlsx"
    if mobilitaet_zeitreihe.exists():
        zeitreihe_data = read_excel_file(mobilitaet_zeitreihe)
        if zeitreihe_data:
            data["zeitreihe"] = zeitreihe_data

    mobilitaet_gesamt = data_folder / "Studierendenmobilität nach Universitäten - Outgoing.xlsx"
    if mobilitaet_gesamt.exists():
        gesamt_data = read_name_based_file(mobilitaet_gesamt, "Outgoing-Studierende")
        if gesamt_data:
            data["gesamt"] = gesamt_data

    mobilitaet_kontinente = data_folder / "Studierendenmobilität nach Kontinenten - Outgoing.xlsx"
    if mobilitaet_kontinente.exists():
        kontinente_data = read_excel_file(mobilitaet_kontinente)
        if kontinente_data:
            data["kontinente"] = kontinente_data

    categories_folder = output_folder / "categories"
    categories_folder.mkdir(exist_ok=True)

    with open(categories_folder / "mobilitaet.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("categories/mobilitaet.json erstellt")


def extract_infrastruktur():
    """Extrahiert Infrastruktur-Daten"""
    data = {}

    infrastruktur_nutzflaeche = data_folder / "Nutzfläche nach Universitäten.xlsx"
    if infrastruktur_nutzflaeche.exists():
        nutzflaeche_data = read_excel_file(infrastruktur_nutzflaeche)
        if nutzflaeche_data:
            data["nutzflaeche"] = nutzflaeche_data

    categories_folder = output_folder / "categories"
    categories_folder.mkdir(exist_ok=True)

    with open(categories_folder / "infrastruktur.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("categories/infrastruktur.json erstellt")


def main():
    print("Starte JSON-Extraktion...\n")

    extract_meta()
    extract_summary()
    extract_personal()
    extract_studierende()
    extract_neuzulassungen()
    extract_studien()
    extract_abschluesse()
    extract_mobilitaet()
    extract_infrastruktur()

    print("\nExtraktion abgeschlossen")
    print(f"Ausgabe: {output_folder}/")


if __name__ == "__main__":
    main()
