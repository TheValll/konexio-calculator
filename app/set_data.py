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
        distances_transport_list = []
        temps_transport_list = []
        distances_voiture_list = []
        temps_voiture_list = []
        distances_velo_list = []
        temps_velo_list = []

        # Loop through the data to get the distance between the company and its students.
        for people in data:
            if not all(people.get(key) for key in ['Adresse', 'Code postal', 'Ville']):
                continue
            
            student_adresse = f"{people['Adresse']}, {people['Code postal']} {people['Ville']}"
            # Create a instance of the DistanceCalculator class.
            distance_calculator = DistanceCalculator(entreprise_adresses, student_adresse)

            # Get the latitude and longitude of the student address.]
            distance_transport = distance_calculator.route_transport()[0]
            distance_voiture_value = distance_calculator.route_voiture()[0]
            distance_velo_value = distance_calculator.route_velo()[0]
            temps_transport_value = distance_calculator.route_transport()[1]
            temps_voiture_value = distance_calculator.route_voiture()[1]
            temps_velo_value = distance_calculator.route_velo()[1]

            # Append the data to the lists.
            nom.append(people['Nom'])
            prenom.append(people['Prénom'])
            distances_transport_list.append(distance_transport)
            distances_voiture_list.append(distance_voiture_value)
            distances_velo_list.append(distance_velo_value)
            temps_transport_list.append(temps_transport_value)
            temps_voiture_list.append(temps_voiture_value)
            temps_velo_list.append(temps_velo_value)

        # Return the data.
        result['nom'] = nom
        result['prenom'] = prenom
        result['distances_transport_list'] = distances_transport_list
        result['temps_transport_list'] = temps_transport_list
        result['distances_voiture_list'] = distances_voiture_list
        result['temps_voiture_list'] = temps_voiture_list
        result['distances_velo_list'] = distances_velo_list
        result['temps_velo_list'] = temps_velo_list
        return result