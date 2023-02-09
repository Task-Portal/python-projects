import requests


class FlightData:
    #This class is responsible for structuring the flight data.


    def __init__(self):
        self.api_key_tequila = {
            "apikey":""
        }
        self.location_endpoint_tequila = "https://api.tequila.kiwi.com/locations/query"

    def get_code_by_city(self, city):
        params = {
            "term":city,
            "location_types":"city"
        }

        response = requests.get(self.location_endpoint_tequila, headers=self.api_key_tequila,params=params)
        response.raise_for_status()
        return response.json()["locations"][0]['code']