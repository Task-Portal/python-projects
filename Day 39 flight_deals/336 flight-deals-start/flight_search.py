import datetime
from pprint import pprint

import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.tequila_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.from_location_code = "WAW"
        self.from_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
        self.to_date = (datetime.datetime.now() + datetime.timedelta(days=(6 * 30))).strftime("%d/%m/%Y")
        self.api_key = ""



    def search_flights(self, town, price):
        params={
            "fly_from":self.from_location_code,
            "fly_to":town,
            "dateFrom" : self.from_date,
            "dateTo":self.to_date
            # "dateTo":"11/02/2023"

        }
        headers = {
            "apikey":self.api_key
        }
        response= requests.get(self.tequila_endpoint,params=params, headers=headers)
        response.raise_for_status()
        # filter by price

        trip = []


        for i in response.json()['data']:
            if float(i["price"])<=float(price):

                item={
                    "cityTo":i["cityTo"],
                    "price":i["price"],
                    "link":i['deep_link']
                }
                trip.append(item)

        # return arr of dictionaries
        # print(response.json())
        return trip




