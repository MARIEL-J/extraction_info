import os

def clean_text(input_file, output_file):
    """ Nettoie le texte extrait et le sauvegarde. """
    try:
        if not os.path.exists(input_file):
            print(f"❌ Fichier non trouvé : {input_file}")
            return

        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Suppression des espaces multiples et lignes vides
        cleaned_text = "\n".join(line.strip() for line in text.splitlines() if line.strip())

        # Création du dossier output_data/processed s'il n'existe pas
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Sauvegarde du texte structuré
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(cleaned_text)

        print(f"✅ Fichier structuré créé : {output_file}")

    except Exception as e:
        print(f"❌ Erreur lors du nettoyage du texte : {e}")

# Test manuel (exécuter ce fichier indépendamment)
if __name__ == "__main__":
    input_path = "output_data/2101.00001v1.txt"  # Remplace par le bon nom de fichier
    output_path = "output_data/processed/mon_fichier_structured.txt"
    clean_text(input_path, output_path)