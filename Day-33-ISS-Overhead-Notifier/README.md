# International Space Station Notifier Program

![ISS_Image](https://github.com/ashjorda/100-Days-Of-Code/assets/40682488/fb13e8ce-01b8-4e52-af26-64708a7cf761)

**Description**

The International Space Staation Notifer Program is a simple script, that can notify you via email when the ISS is
close to your specified location using longitude/latitude coordinates of your sepcified location. 

**Dependencies**

* requests <br>
* smtplib (included in Python) <br>
* datetime (included in Python) <br>
* time (included in Python) <br>

**Usage**

1. Copy the contents of main.py, save to a python file locally
2. Install 'requests' python module
3. Modify the MY_LAT, and MY_LONG constants with the latitude/longitude coordinates of your speficiced location. Can use https://www.latlong.net/ to gather your cooridantes
4. Modify the SENDER_EMAIL, SENDER_PASSWORD, and RECIPIENT_EMAIL constants to their respetive values. Sender Email, and Sender Password combination is the credentails you want
to use from your email provider to send the email noitifcation. And the recipient email is the account that you want to recieve the notifacation when the ISS is over head.
5. Update the smtp address of your email provider on line 60, currenlty set for gmail smtp address.
6. Run the python script from CLI or a hosted server. The script will execute every 60 seconds until canceled or an exception is raised
