# Importing the required libraries
import json
import pandas as pd

# Function to convert a CSV file to JSON
def convert_csv_to_json(uploaded_file):
    data = pd.read_excel(uploaded_file)
    json_data = data.to_json(orient='records')
    try:
        json_obj = json.loads(json_data)
        return json_obj
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier : {e}")