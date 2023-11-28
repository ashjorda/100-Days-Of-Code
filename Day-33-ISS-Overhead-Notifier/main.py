import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 32.931049  # Your latitude
MY_LONG = -96.458649  # Your longitude
SENDER_EMAIL = "dev.ashton18@gmail.com"
SENDER_PASSWORD = "bume huws tlsf iqat"
RECIPIENT_EMAIL = "jen_weeden@yahoo.com"


def up_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_dark():
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

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if up_above() and is_dark():
        # Sends the new_letter to the recipient email using gmail smtp. Can replace smtp with your email provider server
        # and secure port
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
            connection.sendmail(from_addr=SENDER_EMAIL,
                                to_addrs=RECIPIENT_EMAIL,
                                msg=f"Subject:ISS Alert!\n\nWake Up, the ISS is above!"
                                )
