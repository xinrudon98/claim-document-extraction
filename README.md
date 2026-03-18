# Claim Document Extraction Pipeline

An automated pipeline that extracts structured claim data from unstructured documents (e.g., scanned files, text reports) using Python and rule-based parsing.

---

## Overview

This project processes unstructured claim-related documents stored in a folder and extracts key information such as claim number, policy number, insured details, and loss data.

The extracted data is transformed into a structured dataset and exported to Excel for downstream analysis and reporting.

---

## Architecture

Documents (Unstructured Files)  
↓  
Python Extraction Script  
↓  
Regex / Rule-Based Parsing  
↓  
Structured DataFrame  
↓  
Excel Output  

---

## Application Demo

### Sample Input (Unstructured Document)

Example of raw claim document:
Claim Number: CLM123456
Policy Number: POL78910
Insured: John Doe
Loss Date: 2024-05-01
Adjuster: Jane Smith

---

### Extracted Output (Structured Data)

| ClaimNumber | PolicyNumber | InsuredName | LossDate | Adjuster |
|------------|-------------|------------|----------|----------|
| CLM123456  | POL78910    | John Doe   | 2024-05-01 | Jane Smith |

---

## Workflow

1. Load raw documents from folder  
2. Read file content  
3. Apply regex-based extraction rules  
4. Structure extracted data into a DataFrame  
5. Export results to Excel  

---

## Key Features

### Folder-Based Document Processing
- Iterates through a directory of claim documents
- Handles messy and inconsistent file structures

### Text Extraction & Parsing
- Uses regex-based pattern matching
- Extracts key claim-related fields:
  - claim number
  - policy number
  - insured name
  - loss date
  - adjuster

### Data Transformation
- Converts unstructured text into structured tabular format
- Handles missing or inconsistent values

### Output Generation
- Exports clean dataset to Excel
- Ready for reporting, analytics, or database ingestion

---

## Repository Structure

claim-document-extraction/
├── scripts/
│   └── extract_claim_data.py
├── notebooks/
│   └── onward_claimdocs_extractor.ipynb
├── data/
│   └── sample.txt          # sample input (simulated document)
├── output/
│   └── .gitkeep           # output folder for generated Excel
├── README.md

---

## Tech Stack

- Python
- Pandas
- Regex (re)
- File system processing (os)

---

## Setup

1. Place raw documents in the `data/` folder  
   (Note: actual scanned documents are not included in this repo for privacy reasons)

2. Run the extraction script:
   python scripts/extract_claim_data.py


3. Output will be generated at:
   output/claims_data.xlsx
   
---

## Business Impact

- Reduced manual document review effort
- Automated extraction from unstructured data
- Improved data consistency and accuracy
- Enabled downstream analytics and reporting

---

## Future Improvements

- Add PDF parsing (PyPDF / OCR)
- Improve extraction accuracy with NLP models
- Handle multiple formats (PDF, DOCX, images)
- Integrate with database pipelines

