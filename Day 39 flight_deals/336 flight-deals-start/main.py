# This file will need to use the DataManager,FlightSearch,
# FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager

from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

fs = FlightSearch()
dt = DataManager()
fd = FlightData()

if len(dt.get_data()["prices"][0]["iataCode"]) == '':
    dt.write_data(fd)



codes = dt.get_all_location_codes_with_prices()
arr = []
for c in codes:
    res = fs.search_flights(c["code"], c["price"])
    for i in res:
        arr.append(i)

if len(arr)>0:
   nm = NotificationManager()

   letter = ""

   for i in arr:
       letter+=f"<div>{i['cityTo']}, Price: {i['price']}&#8364;, <a href='{i['link']}'>tickets</a>\n\n</div> "


   nm.send_email(letter, dt.read_emails())

# first_name= input("Please enter your first name: ")
# last_name= input("Please enter your last name: ")
# email= input("Please enter your email: ")
# dt.add_users(first_name,last_name,email)

# dt.read_emails()
