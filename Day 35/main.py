import requests
from twilio.rest import Client


wf_endpoint = "http://api.weatherapi.com/v1/forecast.json"
api_key = ""
account_sid = ""
auth_token = ""


weather_params = {
    "key": api_key,
    "q": "51.176200,102.828290",
    "days": 1,
    "aqi": "no",
    "alerts": "no"
}

response = requests.get(wf_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
will_it_rain = weather_data["forecast"]["forecastday"][0]["day"]["daily_will_it_rain"]
if will_it_rain == 1:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Take an umbrella ☂️",
        from_="",
        to=""
    )
    print(message.status)
