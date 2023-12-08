import requests
from twilio.rest import Client

# OpenWeatherMap API Key
api_key = "<twilio api key"
account_sid = "<twilio account sid>"
auth_token = "<twilio auth token>"

# API Parameters to set location, appid, result count
weather_params = {
    "lat": 30.332184,  # Latitude of your location
    "lon": -81.655647,  # Longitude of your location
    "appid": api_key,  # API Key from OpenWeather API
    "cnt": 4,  # How many results to return. Currently, 4 results for weather at an every 3-hour interval
}

# Get request to the API Endpoint, with the Parameters appended to the get request
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
# Raises any exceptions to the console that result from the get request above
response.raise_for_status()
# Stores returned api results in weather_data variable
weather_data = response.json()

# stores the weather condition id's from the weather_data into a list
condition_id = [code["weather"][0]["id"] for code in weather_data["list"]]

# Checks to see if any of the condition ID's are less than 700, Which indicates a form of Rain.
# Send SMS "Bring Umbrella"
if any(weather_code in condition_id for weather_code in range(0, 699)):
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Bring an umbrella ☔️.",
            from_="free twilio number",
            to="<recipient phone number>"
    )
    print(message.status)
