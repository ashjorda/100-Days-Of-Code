import requests
from datetime import datetime

APP_ID = 'nutrionix appid'
APP_KEY = '<nutrionix api key>'
API_URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_API_URL = 'https://api.sheety.co/c0f6856a82dab9a3b8def4c44041939b/workoutTracking/workouts'


APP_ID = '<nutritionix.com api id>'
APP_KEY = '<nutritionix.com api key>'
API_URL = 'https://trackapi.nutritionix.com/v2/natural/exercise' # API for Exercise transcription
SHEETY_API_URL = '<sheety api for your specified sheet to update>'
SHEETY_BEARER = '<bearrer token from sheety for sheet protection>' # Authentication is optional on Sheety, can remove if not wanted

# Required headers for the nutritionix api
headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}

# Captures user input on what exercises they completed
exercises_duration = {
    "query": input("Tell me what exercise(s) you did: ")
}

# Sends the exercise_duration query to the nutritionix api url for transcription
send_exercise = requests.post(url=API_URL, headers=headers, json=exercises_duration)

# Formats the date, and time to accompany your exercise record that will be written to the Google sheet
today = datetime.now()
time = today.time()

# Cycles through the json response from nutrionix api, and the for loop catches if you did multiple exercises. And stores the infromation in their respective variables.
for _ in send_exercise.json()['exercises']:
    exercise = _['name']
    duration = _['duration_min']
    calories = _['nf_calories']

# Header information for the Sheety API, if SHEETY_BEARER is removed above, this header section is not needed
header = {
    "Authorization": SHEETY_BEARER
}

# Formats the Nutritionix JSON response into JSON to be posted to the SHEETY API (Exercise Google Sheet). The key's in the workout dictionary are the values that should corresponde to your google sheet column headers
exercise_data = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": f"{time.hour}:{time.minute}",
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories
    }
}

# Post exercise_data to the Google Sheet via the SHEETY API
update_sheet = requests.post(url=SHEETY_API_URL, headers=header, json=exercise_data)
