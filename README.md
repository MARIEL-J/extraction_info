# extraction_info
Ce projet vise à développer des méthodes pour extraire automatiquement des informations de documents non structurés (PDF) et les convertir en formats structurés (CSV). Il se concentre sur l'amélioration de l'OCR, l'analyse syntaxique et sémantique, ainsi que la structuration des données pour des applications futures.

# Extraction Info

## Overview
This project automates the extraction, cleaning, and structuring of text from PDF documents. It identifies and processes PDF files from the `input_docs` directory and generates structured text output in `output_data/processed/`.

## Features
- **Automatic PDF detection:** Processes any PDF found in `input_docs`.
- **Text extraction:** Uses `pdfplumber` and `pytesseract` for OCR.
- **Text cleaning & structuring:** Removes noise and formats the output.
- **Logging & error handling:** Ensures smooth execution with debug logs.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) (for OCR processing)

### Dependencies
Install required Python packages:
```sh
pip install -r requirements.txt
```

## Usage
Run the script to process all PDFs in input_docs:

```sh
Copier
python main.py
```
## Expected Output

```graphql
Processing file: 2101.00001v1.pdf
✅ Extracted text saved: output_data/2101.00001v1.txt
✅ Cleaned & structured text saved: output_data/processed/structured_text.txt
```

## Folder Structure

```graphql
extraction_info/
│── input_docs/            # Folder containing PDF files to process
│── output_data/           # Folder for extracted text files
│   ├── processed/         # Structured output text files
│── src/
│   ├── extract_text.py    # Handles text extraction from PDFs
│   ├── process_text.py    # Cleans and structures extracted text
│   ├── main.py            # Main execution script
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
```

## License

This project is licensed under the MIT License. See LICENSE for details.

## Contribution

Feel free to fork and submit pull requests. For major changes, please open an issue first.

## Issues

If you encounter any issues, create a GitHub issue, or contact the repository owner.
