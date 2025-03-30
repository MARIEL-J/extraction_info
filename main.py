import os
import json
import csv
from extract_text import extract_text_from_pdf
from process_text import clean_text

def convert_to_json(txt_file_path):
    """Convertir un fichier texte en JSON."""
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Créer une structure JSON plus appropriée
    data = {"content": [line.strip() for line in lines]}
    
    # Définir le chemin pour le fichier JSON dans 'output_data/final'
    json_file_path = os.path.join('output_data', 'final', os.path.basename(txt_file_path).replace('.txt', '.json'))
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    print(f"Fichier JSON sauvegardé dans {json_file_path}")

def convert_to_csv(txt_file_path):
    """Convertir un fichier texte en CSV."""
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Définir le chemin pour le fichier CSV dans 'output_data/final'
    csv_file_path = os.path.join('output_data', 'final', os.path.basename(txt_file_path).replace('.txt', '.csv'))
    
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        # Chaque ligne du fichier texte devient une ligne dans le CSV
        for line in lines:
            writer.writerow([line.strip()])  # Ajoute une cellule par ligne du texte
    
    print(f"Fichier CSV sauvegardé dans {csv_file_path}")

def main():
    # Chemin du dossier contenant les fichiers PDF
    input_folder = "input_docs"
    
    # Liste des fichiers PDF dans le dossier input_docs
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]
    
    if not pdf_files:
        print("Aucun fichier PDF trouvé dans le dossier input_docs.")
        return
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        print(f"Traitement du fichier : {pdf_file}")
        
        # Extraction du texte du fichier PDF
        texte_extrait = extract_text_from_pdf(pdf_path)
        
        # Sauvegarde du texte extrait dans un fichier temporaire
        fichier_temp = os.path.join('output_data', pdf_file.replace('.pdf', '_temp.txt'))
        with open(fichier_temp, 'w', encoding='utf-8') as file:
            file.write(texte_extrait)
        
        # Définir le nom du fichier texte de sortie
        fichier_texte = pdf_file.replace('.pdf', '.txt')
        output_file = os.path.join('output_data', 'processed', fichier_texte)
        
        # Nettoyage et structuration du texte
        clean_text(fichier_temp, output_file)
        
        # Optionnel : supprimer le fichier temporaire après traitement
        os.remove(fichier_temp)

        print(f"Texte extrait et nettoyé sauvegardé dans {output_file}")
        
        # Récupérer le fichier .txt nettoyé à partir du dossier 'output_data/processed'
        txt_file_path = os.path.join('output_data', 'processed', fichier_texte)
        
        if os.path.exists(txt_file_path):
            print(f"Conversion du fichier {txt_file_path} en JSON et CSV...")
            # Convertir en JSON et CSV
            convert_to_json(txt_file_path)
            convert_to_csv(txt_file_path)
        else:
            print(f"Le fichier {txt_file_path} n'existe pas.")
    
if __name__ == "__main__":
    main()