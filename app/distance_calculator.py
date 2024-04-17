# Import get_latitude_longitude and get_route functions from the corresponding files.
from get_distance import get_distance

# Class DistanceCalculator to calculate the distance between the company and the student.
class DistanceCalculator:
    # Initialize the class with the company address and the student address.
    def __init__(self, entreprise_adresse, student_adresse):
        self.entreprise_adresse = entreprise_adresse
        self.student_adresse = student_adresse

    # Function to calculate the distance between the company and the student by public transport.
    def route_transport(self):
        if self.entreprise_adresse and self.student_adresse:
            route = get_distance(self.entreprise_adresse, self.student_adresse, "transit")
            distance = route["routes"][0]["legs"][0]["distance"]["text"]
            duration = route["routes"][0]["legs"][0]["duration"]["text"]
            return distance, duration

    # Function to calculate the distance between the company and the student by car.
    def route_voiture(self):
        if self.entreprise_adresse and self.student_adresse:
            route = get_distance(self.entreprise_adresse, self.student_adresse, "driving")
            distance = route["routes"][0]["legs"][0]["distance"]["text"]
            duration = route["routes"][0]["legs"][0]["duration"]["text"]
            return distance, duration
        else:
            return None
        
    # Function to calculate the distance between the company and the student by bike.
    def route_velo(self):
        if self.entreprise_adresse and self.student_adresse:
            route = get_distance(self.entreprise_adresse, self.student_adresse, "bicycling")
            distance = route["routes"][0]["legs"][0]["distance"]["text"]
            duration = route["routes"][0]["legs"][0]["duration"]["text"]
            return distance, duration
        else:
            return None
