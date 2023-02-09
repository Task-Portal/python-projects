import requests

from flight_data import FlightData


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint_prices = ""
        self.sheety_endpoint_users = ""
        self.data = {}

    def get_data(self):
        response = requests.get(self.sheety_endpoint_prices)
        response.raise_for_status()
        self.data = response.json()

        return response.json()

    def write_data(self, fd: FlightData):
        for i in self.get_data()['prices']:
            data = {
                "price": {
                    "iataCode": fd.get_code_by_city(i["city"]),

                }
            }

            response = requests.put(f"{self.sheety_endpoint_prices}/{i['id']}", json=data)
            response.raise_for_status()

    def get_price(self, town):
        for i in self.data["prices"]:
            if i["city"]==town:
                return i["lowestPrice"]
        return 0

    def get_location_code(self, town):
        for i in self.data["prices"]:
            if i["city"] == town:
                return i["iataCode"]

    def get_all_location_codes_with_prices(self):
        codes = []
        for i in self.data["prices"]:
           codes.append({"code":i["iataCode"], "price":i["lowestPrice"]})
        return codes

    def add_users(self, fname, lname,email):
        data = {
            "user": {
                "firstName": fname,
                "lastName": lname,
                "email":email
            }
        }

        response = requests.post(f"{self.sheety_endpoint_users}", json=data)
        response.raise_for_status()

    def read_emails(self):
        response = requests.get(self.sheety_endpoint_users)
        response.raise_for_status()
        emails = [i["email"] for i in response.json()["users"]]
        return emails


