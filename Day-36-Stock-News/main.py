import requests
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla&nbsp;Inc"
STOCK_API = "BQA7993Z4CEX0IQ0"
NEWS_API = "0f642f75fb3449f3a90b478328ec8f9b"
SENDER_EMAIL = 'dev.ashton18@gmail.com'  # user@gmail.com
SENDER_PASSWORD = 'bume huws tlsf iqat'
RECIPIENT_EMAIL = 'jen_weeden@yahoo.com'  # recieved@gmail.com
header = None


# Funtion grabs current news articles for the Company name, then sends 3 emails containing the Stock Information and the
# first three news articles from the newsapi endpoint.
def send_email(email_subject):
    # Get request to the newsapi for the company name
    news = requests.get(
        f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&pagesize=4&apiKey={NEWS_API}')
    news_data = news.json()
    # sens 3 emails, each with a different news article, with the same {header} for each
    for _ in range(0, 3):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
            connection.sendmail(from_addr=SENDER_EMAIL,
                                to_addrs=RECIPIENT_EMAIL,
                                msg=f"Subject:{header} Headline: {news_data['articles'][_]['title']}\n\nBrief: {news_data['articles'][_]['description']}".encode(
                                    'utf8')
                                )


# Sets Alphavantage Stock Data API Endpoint URL
r = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API}')
# Store the 'Time Series (Daily)' key values in the variable: data
data = r.json()['Time Series (Daily)']

# Perform list comprehension to create a new list that contains each day's stock information only
close_information = [value for (key, value) in data.items()]
# Store the stock close information for yesterday, and the day before yesterday
yesterday_close = close_information[0]['4. close']
day_before_yesterday_close = close_information[1]['4. close']

# Calculate the percentage change between to the two close values
percent_change = round((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close * 100)

# Create a header for the email subject line to include the Stock Symbol, direction of change, and change percentage if
# the percentage change was greater than positive 5% or negative 5%. Then send 3 emails, with header and news article
if percent_change > 5:
    header = f"{STOCK}:🔺 {percent_change}%"
    send_email(header)
elif percent_change < -5:
    header = f"{STOCK}:🔻 {percent_change}%"
    send_email(header)
