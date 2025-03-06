import requests
from pprint import pprint
from flight_data import FlightData

SHEET_ENDPOINT = "https://api.sheety.co/2d91672219ab6db58e6ff709770ec733/pythonFlights/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def printing(self):
        pprint(self.response)

    def sheet_updating(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(f"{SHEET_ENDPOINT}/{city['id']}", json=new_data)
        print(response.text)


