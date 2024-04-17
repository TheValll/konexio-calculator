# Importing the requests library
import requests
import os

def get_distance(entreprise_adresse, student_adresse, mode):
    api_url = f"https://maps.googleapis.com/maps/api/directions/json?&destination={entreprise_adresse}&mode={mode}&origin={student_adresse}&key={os.getenv('ACCES_API_KEY')}"
    response = requests.get(api_url)
    api_data = response.json()
    if api_data: 
        return api_data
    else:
        return None