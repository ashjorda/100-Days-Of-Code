##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import pandas as pd
import random

# Program Variables
SENDER_EMAIL = "user@user.com"
SENDER_PASSWORD = "<sender email password here>"
RECIPIENT_EMAIL = "user@user.com"

now = dt.datetime.now()
day_of_month = now.day
current_month = now.month

# Open birthday recipients list
df = pd.read_csv("birthdays.csv")
# Stores the row index(s) in birthday_list if the current month/day matches a row within the birthdays.csv file
birthday_list = df.loc[(df['month'] == current_month) & (df['day'] == day_of_month)].index


for recipient in birthday_list:
    # Extracts the name, email from the returned indexes within birthday_list dataframe
    birthday_name = df.at[recipient, "name"]
    birthday_email = df.at[recipient, "email"]

    # Randomly chooses a letter_template from the templates folder, then reads the template into "letter", and
    # replaces the [NAME] placeholder with the birthday_name variable.
    # Then stores the replaced letter with back inside "letter"

    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as birthday_letter:
        letter = birthday_letter.read()
        letter = letter.replace("[NAME]", birthday_name)

        # Sends the new_letter to the recipient email using gmail smtp. Can replace smtp with your email provider server
        # and secure port
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
            connection.sendmail(from_addr=SENDER_EMAIL,
                                to_addrs=RECIPIENT_EMAIL,
                                msg=f"Subject:Happy Birthday!\n\n{letter}"
                                )
