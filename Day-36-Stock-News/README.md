# Stock Monitoring and News Alert System

## Overview

This Python script monitors stock performance and sends email alerts based on the percentage change in the stock price. Additionally, it includes news articles related to a specified company retrieved from the News API.

## Prerequisites

Make sure you have the following installed:

- Python (version 3.x)
- Required Python packages: `requests` and `smtplib`. You can install them using the following command:

```bash
pip install requests smtplib
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/ashjorda/100-Days-Of-Code.git
```

2. Navigate to the project directory:

```bash
cd Day-36-Stock-News
```

3. Edit the script and set the required configuration variables:

- `STOCK`: Stock symbol to monitor (e.g., "TSLA").
- `COMPANY_NAME`: Company name for news retrieval (e.g., "Tesla Inc").
- `STOCK_API`: Alphavantage API key for stock data retrieval.
- `NEWS_API`: News API key for news data retrieval.
- `SENDER_EMAIL`: Email address for the sender (SMTP login).
- `SENDER_PASSWORD`: Password for the sender's email account (SMTP password).
- `RECIPIENT_EMAIL`: Email address for receiving alerts.

4. Run the script:

```bash
python main.py
```

The script will fetch stock data from Alphavantage and news articles from the News API. If the percentage change in stock price is greater than 5% (increase or decrease), it will send three email alerts, each containing a different news article related to the specified company.

Feel free to customize the script further based on your requirements.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ashjorda/100-Days-Of-Code/blob/master/LICENSE) file for details.
