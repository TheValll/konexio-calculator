# Importing the requests library
import requests

# Function to get the distance between two coordinates
def get_route(latitude1, longitude1, latitude2, longitude2, mode='car'):
    api_url = f"https://wxs.ign.fr/calcul/geoportail/itineraire/rest/1.0.0/route?resource=bdtopo-pgr&profile={mode}&optimization=fastest&start={longitude1},{latitude1}&end={longitude2},{latitude2}"
    response = requests.get(api_url)
    api_data = response.json()
    return api_data