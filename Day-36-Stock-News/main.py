import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey=BQA7993Z4CEX0IQ0'

r = requests.get(url)
data = r.json()

# data_keys = [x for x in data["Time Series (Daily)"]]
v1 = 500  # current_close = float(data["Time Series (Daily)"][data_keys[0]]["4. close"])
v2 = 235  # previous_close = float(data["Time Series (Daily)"][data_keys[1]]["4. close"])

percent_change = (v2 - v1) / v1 * 100

if percent_change < -5:
    direction = "🔻"
elif percent_change > 5:
    direction = "🔺"

# # STEP 2: Use https://newsapi.org Instead of printing ("Get News"), actually get the first 3 news pieces for the
# COMPANY_NAME. news = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&q=Apple&pagesize=4&apiKey
# =0f642f75fb3449f3a90b478328ec8f9b')
news = requests.get(
    f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&pagesize=4&apiKey=0f642f75fb3449f3a90b478328ec8f9b')

news_data = news.json()

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
print(f"{STOCK}: {direction}{percent_change} \nThe Good, The Bad, The Ugly Goes Here")

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
