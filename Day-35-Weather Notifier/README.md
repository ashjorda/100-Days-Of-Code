# Weather Alert Notifier

## Overview

This Python script utilizes the OpenWeatherMap API and Twilio to provide weather alerts based on current weather conditions. If rain is detected in the forecast, the script sends an SMS alert advising the user to bring an umbrella.

## Prerequisites

Make sure you have the following installed:

- Python (version 3.x)
- Required Python packages: `requests` and `twilio`. You can install them using the following command:

```bash
pip install requests twilio
```

## Configuration

Before running the script, you need to set up the following variables in the script:

- `api_key`: OpenWeatherMap API key for weather data retrieval.
- `account_sid`: Twilio account SID.
- `auth_token`: Twilio authentication token.
- `weather_params`: API parameters including latitude, longitude, API key, and result count.
- `from_`: Twilio phone number (free Twilio number) sending the SMS.
- `to`: Recipient's phone number for receiving alerts.

## Usage

1. Clone the repository:

```bash
git download main.py to your project directory
```

2. Navigate to the project directory:

```bash
cd project directory
```

3. Edit the script and set the required configuration variables.

4. Run the script:

```bash
python main.py
```

The script will fetch weather data from the OpenWeatherMap API based on the specified location parameters. If rain is detected in the forecast (any condition ID less than 700), it will send an SMS alert using Twilio.

Feel free to customize the script further based on your requirements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.