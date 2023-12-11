import requests
from datetime import datetime

APP_ID = 'beb58d3e'
APP_KEY = '14e25e90f3c161ce4b5bbdd054304615'
API_URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_API_URL = 'https://api.sheety.co/c0f6856a82dab9a3b8def4c44041939b/workoutTracking/workouts'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}

exercises_duration = {
    "query": input("Tell me what exercise you did: ")
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