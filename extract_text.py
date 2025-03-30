import os
import pdfplumber
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# Chemin vers Tesseract (modifiez si nécessaire)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(pdf_path):
    text = ""
    
    # Essayer d'extraire du texte directement
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    # Si l'extraction est vide, utiliser l'OCR
    if not text.strip():
        images = convert_from_path(pdf_path)
        for img in images:
            text += pytesseract.image_to_string(img, lang="fra") + "\n"
    
    return text.strip()

if __name__ == "__main__":
    input_folder = "input_docs"
    output_folder = "output_data"
    
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, file)
            extracted_text = extract_text_from_pdf(pdf_path)
            
            text_file = os.path.join(output_folder, file.replace(".pdf", ".txt"))
            with open(text_file, "w", encoding="utf-8") as f:
                f.write(extracted_text)

            print(f"Extraction terminée pour {file}, texte enregistré dans {text_file}")