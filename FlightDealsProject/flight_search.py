import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "kZTWp6PN6a94k9BQDGWUbTPtM-ZwJVUo"


class FlightSearch:
    def get_destination_code(self, city):
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        parameters = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=parameters, headers=headers)
        data = response.json()['locations']
        code = data[0]["code"]
        return code
