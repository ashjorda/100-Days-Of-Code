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
sender_email = "user@user.com"
recipient_email = "user@user.com"
password = "sender email password"
now = dt.datetime.now()
day_of_month = now.day
current_month = now.month

# Birthday letter template file names from /letter_templates directory
templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# Open birthday recipients list
df = pd.read_csv("birthdays.csv")
# Stores the row index(s) in birthday_list where the current month/day matches a row within the birthdays.csv file
birthday_list = df.loc[(df['month'] == current_month) & (df['day'] == day_of_month)].index


for recipient in birthday_list:
    # Extracts the name, email from the returned indexes within birthday_list dataframe
    birthday_name = df.at[recipient, "name"]
    birthday_email = df.at[recipient, "email"]

    # Randomly chooses a letter_template from the template list, then reads the template into draft, and
    # replaces the [NAME] placeholder with the birthday_name variable.
    # Then store the template with the proper name in new_letter

    birthday_template = random.choice(templates)
    with open(f"letter_templates/{birthday_template}", "r") as draft_letter:
        draft = draft_letter.read()
        new_letter = draft.replace("[NAME]", birthday_name)

        # Sends the new_letter to the recipient email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(from_addr=sender_email,
                                to_addrs=recipient_email,
                                msg=f"Happy Birthday!\n\n{new_letter}"
                                )
