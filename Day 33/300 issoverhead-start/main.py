import smtplib

import requests
from datetime import datetime
import time


MY_LAT = "51.183841"
MY_LONG = "32.811196"


def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset

def under_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    return float(MY_LONG)-5 <= iss_longitude <= float(MY_LONG)+5 and float(MY_LAT) - 5 <= iss_latitude <= float(MY_LAT) + 5

def is_night():
    parameters = {
            "lat":MY_LAT,
            "lng": MY_LONG,
            "formatted":0

        }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    dt_sunrise=  datetime.strptime(data["results"]["sunrise"], '%Y-%m-%dT%H:%M:%S%z')
    dt_sunset=  datetime.strptime(data["results"]["sunset"], '%Y-%m-%dT%H:%M:%S%z')

    sunrise = datetime_from_utc_to_local(dt_sunrise).hour
    sunset = datetime_from_utc_to_local(dt_sunset).hour

    time_now = datetime.now()
    if time_now.hour >= sunset or time_now<=sunrise:
        return True


print("Started")




#If the ISS is close to my current position
while True:
    if under_me()  and is_night():
        email_from = "your email"
        password = "your password"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email_from, password=password)
            connection.sendmail(
                from_addr=email_from,
                to_addrs="email",
                msg=f"Subject:Look up\n\n Look up into the sky"
            )
    time.sleep(60)





