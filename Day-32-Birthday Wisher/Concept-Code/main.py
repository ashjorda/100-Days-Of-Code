import random
import smtplib
import datetime as dt
from random import choice

# Define sender, receiver, sender email password
sender_email = "user@user.com"
recipient_email = "user@user.com"
password = "<sender email passsword>"

# Initialize Datetime Object, and store current day integer in day_of_week variable
now = dt.datetime.now()
day_of_week = now.weekday()

# Determine if the current day is Monday, if so send motivational quote to recipient email
if day_of_week == 0:
    # Open quotes.txt, and store all quotes in a list.
    with open("quotes.txt", "r") as quotes:
        q_list = quotes.readlines()
        random_quote = random.choice(q_list)

    # Send email with the qoute of the day to the "to_addrs" email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=recipient_email,
                            msg=f"Subject:Monday Motivation\n\n{random_quote}"
                            )