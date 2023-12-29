# Flight Deals Notifier

Flight Deals Notifier is a Python program that helps users find affordable flight deals by searching for flights from a specified origin city to a list of destinations. The program checks flight prices using the Kiwi Flight Search API and sends email notifications when a flight with a price within the specified budget is found.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Import flight destinations from a Google Sheet using the Sheetly API.
- Check and populate city codes for each destination if missing in the Google Sheet.
- Search for flight deals from a specified origin city to multiple destinations.
- Send email notifications with detailed flight information for affordable deals.
- **Optional:** Use the user interface on Replit to enter your email and receive flight deal notifications.

## Prerequisites
Before running the program, ensure you have the following prerequisites:

- Python 3.x
- Required Python packages (install using `pip install requests smtplib`)
- **Tequila Kiwi API Key:** Sign up for a free account and obtain your API key from [Tequila Kiwi Travel](https://tequila.kiwi.com/) to access the flight search API.
- Make a copy of the Google Sheet at [this link](https://docs.google.com/spreadsheets/d/1WPZ0_el4qXyjfwq1iZ0W3oEzK0RT5UbyyedOGXrmPJo/edit?usp=sharing).
- Sign up for [Sheety](https://sheety.io/), and connect your Google Sheet to Sheetly so that you can obtain your Google Sheet API URL. **Note**: In Sheety, the following permissions need to be set for each sheet: **prices:** (GET, PUT) **users:** (GET, POST) 



## Installation
1. Clone the repository to your local machine.
2. Navigate to "Day-39-Flight-Deal-Finder" directory.

## Configuration
1.  Fork the Replit at [this link](https://replit.com/@AshtonJordan2/Day-40-Flight-Club#main.py) and add your Sheety API URL for the "users" tab. Alternatively, you can manually add emails to the "users" tab in the main.py in the Replit on Line 10 "api_url".
2. Open the `settings_vault.py` file and provide your Kiwi API key, SMTP login details, and other configuration settings.

## Usage
1. Run the `main.py` script to initiate the flight search and notification process.
2. Check your email for notifications about affordable flight deals.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
