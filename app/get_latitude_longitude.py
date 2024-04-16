# Importing the requests library
import requests

# Function to get the latitude and longitude of an address
def get_latitude_longitude(address):
    api_url = f"https://api-adresse.data.gouv.fr/search/?q={address}&type=street"
    response = requests.get(api_url)
    api_data = response.json()
    location = api_data['features'][0]['geometry']['coordinates']
    if location:
        return location
    else:
        return None