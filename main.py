import requests
from datetime import datetime
import os

##################################################################################
# Sheet file address:   https://docs.google.com/spreadsheets/d/1q0cH00lZVB0K1tX2kwcjmZRKRZoFCmOPyFT99Yt5Elk/edit#gid=0
##################################################################################

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
BEARER_TOKEN = os.environ["BEARER_TOKEN"]
Exercise_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
new_row = "https://api.sheety.co/2b0dffeec12bb812649c7bc9ea70a311/=myWorkoutsNima/workouts"

note = input("How you exercise today? :")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": note,
    "gender": "male",
    "weight_kg": 95,
    "height_cm": 173,
    "age": 41,
}

today = datetime.now()
date_today = today.strftime("%d/%m/%Y")
hour_today = today.strftime("%H:%M:%S")


response = requests.post(url=Exercise_ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
data = response.json()


parameters_sheety = {
    "workout": {
        "date": date_today,
        "time": hour_today,
        "exercise": data["exercises"][0]["name"],
        "duration": data["exercises"][0]["duration_min"],
        "calories": data["exercises"][0]["nf_calories"],
    }
}
print(parameters_sheety)

headers_sheety = {
    "Authorization": BEARER_TOKEN
}

response1 = requests.post(url=new_row, json=parameters_sheety, headers=headers_sheety)
response1.raise_for_status()
data2 = response.json()
