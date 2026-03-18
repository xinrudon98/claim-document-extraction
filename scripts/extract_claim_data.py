import os
import re
import pandas as pd

# =========================
# CONFIG
# =========================
INPUT_FOLDER = "data/"
OUTPUT_FILE = "output/claims_data.xlsx"

# =========================
# HELPERS
# =========================
def read_file(file_path):
    try:
        with open(file_path, "r", errors="ignore") as f:
            return f.read()
    except:
        return ""

def extract_field(pattern, text):
    match = re.search(pattern, text)
    return match.group(1).strip() if match else None

# =========================
# EXTRACTION LOGIC
# =========================
def extract_claim_info(text):
    return {
        "ClaimNumber": extract_field(r"Claim Number[:\s]+(\S+)", text),
        "PolicyNumber": extract_field(r"Policy Number[:\s]+(\S+)", text),
        "InsuredName": extract_field(r"Insured[:\s]+(.+)", text),
        "LossDate": extract_field(r"Loss Date[:\s]+(.+)", text),
        "Adjuster": extract_field(r"Adjuster[:\s]+(.+)", text)
    }

# =========================
# MAIN PIPELINE
# =========================
def process_documents(input_folder):
    records = []

    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)

        if not os.path.isfile(file_path):
            continue

        text = read_file(file_path)

        if not text:
            continue

        data = extract_claim_info(text)
        data["FileName"] = file_name

        records.append(data)

    return pd.DataFrame(records)

def main():
    print("Starting extraction...")

    df = process_documents(INPUT_FOLDER)

    if df.empty:
        print("No data extracted.")
        return

    os.makedirs("output", exist_ok=True)

    df.to_excel(OUTPUT_FILE, index=False)

    print(f"Extraction completed. Output saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
