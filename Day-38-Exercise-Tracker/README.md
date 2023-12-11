# Exercise Tracking App

This Python script allows you to track your exercises and update a Google Sheet using the Nutritionix API and Sheety API.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- [Python](https://www.python.org/) (version 3.6 or higher)
- [Requests](https://docs.python-requests.org/en/latest/) library

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/ashjorda/100-Days-Of-Code.git
    ```

2. Change into the project directory:

    ```bash
    cd Day-38-Exercise-Tracker
    ```

3. Install the required Python packages using pip:

    ```bash
    pip install requests
    ```

## Configuration

1. Obtain API keys:
   - Nutritionix API: [Nutritionix Developer Portal](https://developer.nutritionix.com/)
   - Sheety API: [Sheety](https://sheety.co/)

2. Replace the placeholder values in the code with your API keys:

    ```python
    APP_ID = 'your_nutritionix_app_id'
    APP_KEY = 'your_nutritionix_api_key'
    SHEETY_API_URL = 'your_sheety_api_url'
    SHEETY_BEARER = 'your_sheety_bearer_token'
    ```

## Usage

Run the script by executing the following command:

```bash
python main.py
```

Follow the on-screen prompts to input your exercises and durations. The script will then update the specified Google Sheet with the exercise details.

**Note**: Make sure to handle your API keys securely and do not share them publicly.

Feel free to customize the script according to your needs and enjoy tracking your exercises!