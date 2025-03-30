import os
import json
import pandas as pd

def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding="utf-8")

if __name__ == "__main__":
    input_folder = "output_data/processed"
    output_folder = "output_data/final"
    os.makedirs(output_folder, exist_ok=True)

    structured_data = []

    for file in os.listdir(input_folder):
        if file.endswith("_structured.txt"):
            with open(os.path.join(input_folder, file), "r", encoding="utf-8") as f:
                content = f.read()
                structured_data.append({"document": file, "content": content})

    save_to_json(structured_data, os.path.join(output_folder, "structured_data.json"))
    save_to_csv(structured_data, os.path.join(output_folder, "structured_data.csv"))

    print("Données exportées en JSON et CSV.")