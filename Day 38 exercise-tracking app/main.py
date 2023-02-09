import datetime

import requests

NUTRITION_API_KEY = ""

APP_ID = ""

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = 'https://api.sheety.co/7e43a8f4be440758a7f89b10d9393c1b/workoutTracking/workouts'
headers_nutrition = {
    "x-app-id": APP_ID,
    "x-app-key": NUTRITION_API_KEY,

}

# "query": "ran 3K and cycled for 20 minutes.",

params_nutrition = {
    "query": input("What you have done today?")


}

response = requests.post(url=nutrition_endpoint, headers=headers_nutrition, json=params_nutrition)
response.raise_for_status()
# print(response.json())

# exercise = response.json()["'exercises'"]
date = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().time().strftime("%H:%M:%S")

arr = [{"name": i["name"].title(), "duration": i["duration_min"], "calories": i["nf_calories"]} for i in
       response.json()["exercises"]]

for i in arr:
    params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": i["name"],
            "duration": i["duration"],
            "calories":i["calories"]
        }
    }
    res = requests.post(sheety_endpoint, json=params)
    res.raise_for_status()
    print(res)

print(arr)
