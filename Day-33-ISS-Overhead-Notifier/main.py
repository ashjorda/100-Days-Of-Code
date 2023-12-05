import requests
import smtplib
from datetime import datetime
import time

# Set the Latitude/Longitude coordinates for your location, and the sender email, sender email password, and recipient
# email of the ISS overheard notification
MY_LAT = 46.412830  # Your latitude
MY_LONG = -1.409850  # Your longitude
SENDER_EMAIL = "<sender email account>"  # user@gmail.com
SENDER_PASSWORD = "<sender email account password>"
RECIPIENT_EMAIL = "<recipient email>"  # recieved@gmail.com


# Function gets the long/lat of the ISS via API, and also raises an exception if the api call is not successful.
# The API response is stored in data. Then parsed for the exact values needed. Then we compare if our long/lat is within
# 5 degrees of the current ISS long/lat.Then return True if the statement checks out.
def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


# Function checks if it is nighttime at your long/lat location via API. It uses the API to get the sunset, and sunrise
# time of your location. And check the current time to see if the current time is after sunset, and before sunrise.
# If the condition is True, the function returns True.
def dark_outside():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_time = datetime.now().hour

    if current_time >= sunset or current_time <= sunrise:
        return True


print("Currently watching the Sky's!")

# While loop runs the code every 60 seconds, until stopped by user input or an exception is hit.
while True:
    time.sleep(60)
    # If ISS is close, and it's nighttime. Send an email notifying ISS is close.
    if iss_overhead() and dark_outside():
        # Sends an email to the recipient email using the set smtp. Stating that the ISS is within 5+ or 5- degrees of
        # MY_LAT, MY_LONG above.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
            connection.sendmail(from_addr=SENDER_EMAIL,
                                to_addrs=RECIPIENT_EMAIL,
                                msg=f"Subject:ISS Alert!\n\nWake Up, the ISS is above!"
                                )
