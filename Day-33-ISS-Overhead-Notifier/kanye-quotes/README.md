# Kanye Quote Generator


**Description**

The International Space Station Notifier Program is a simple script, that can notify you via email when the ISS is
close to your longitude/latitude coordinates of your specified location. 

**Dependencies**

* requests <br>
* smtplib (included in Python) <br>
* datetime (included in Python) <br>
* time (included in Python) <br>

**Usage**

1. Copy the contents of main.py, save it to a python file locally
2. Install 'requests' python module
3. Modify the MY_LAT, and MY_LONG constants with the latitude/longitude coordinates of your specified location. Can use https://www.latlong.net/ to gather your coordinates
4. Modify the SENDER_EMAIL, SENDER_PASSWORD, and RECIPIENT_EMAIL constants to their respective values. Sender Email, Sender Password, as these are the credentials you want
to use from your email provider to send the email notification. And the recipient email is the account that you want to receive the notification when the ISS is over head.
5. Update the smtp address of your email provider on line 60, currently set for gmail smtp address.
6. Run the python script from CLI or a hosted server. The script will execute every 60 seconds until canceled or an exception is raised
