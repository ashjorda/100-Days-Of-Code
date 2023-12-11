import requests
from datetime import datetime

APP_ID = 'nutritionix.com api id'
APP_KEY = '<nutritionix.com api key>'
API_URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_API_URL = '<sheety api for your specified sheet to update>'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}

exercises_duration = {
    "query": input("Tell me what exercise(s) you did: ")
}

send_exercise = requests.post(url=API_URL, headers=headers, json=exercises_duration)

# Update Google Docs Spreadsheet with exercise activity
today = datetime.now()
time = today.time()

for _ in send_exercise.json()['exercises']:
    exercise = _['name']
    duration = _['duration_min']
    calories = _['nf_calories']

exercise_data = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": f"{time.hour}:{time.minute}",
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories
    }
}

update_sheet = requests.post(url=SHEETY_API_URL, json=exercise_data)