# Import the DistanceCalculator class and the convert_csv_to_json function.
from distance_calculator import DistanceCalculator
from convert_csv_to_json import convert_csv_to_json

def set_data(uploaded_files, entreprise_adresses):
    
    # Convert the uploaded file to JSON.
        data = convert_csv_to_json(uploaded_files)

        # Create empty lists to store the data.
        result = {}
        nom = []
        prenom = []
        distances_voiture_list = []
        temps_voiture_list = []
        distances_pieton_list = []
        temps_pieton_list = []
        temps_velo_list = []

        # Loop through the data to get the distance between the company and its students.
        for people in data:
            if not all(people.get(key) for key in ['Adresse', 'Code postal', 'Ville']):
                continue
            
            # Create a instance of the DistanceCalculator class.
            distance_calculator = DistanceCalculator(entreprise_adresses, f"{people['Adresse']}, {people['Code postal']}, {people['Ville']}")

            # Get the latitude and longitude of the student address.
            distance_voiture_value = distance_calculator.distance_voiture()
            distance_pieton_value = distance_calculator.distance_pieton()
            temps_voiture_value = distance_calculator.temps_voiture()
            temps_pieton_value = distance_calculator.temps_pieton()
            temps_velo_value = distance_calculator.temps_velo()

            # Append the data to the lists.
            nom.append(people['Nom'])
            prenom.append(people['Prénom'])
            distances_voiture_list.append(distance_voiture_value)
            distances_pieton_list.append(distance_pieton_value)
            temps_voiture_list.append(temps_voiture_value)
            temps_pieton_list.append(temps_pieton_value)
            temps_velo_list.append(temps_velo_value)

        # Return the data.
        result['nom'] = nom
        result['prenom'] = prenom
        result['distances_voiture_list'] = distances_voiture_list
        result['temps_voiture_list'] = temps_voiture_list
        result['distances_pieton_list'] = distances_pieton_list
        result['temps_pieton_list'] = temps_pieton_list
        result['temps_velo_list'] = temps_velo_list
        return result