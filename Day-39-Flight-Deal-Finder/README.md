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
Before running the program, ensure you have the following prerequisites installed:
- Python 3.x
- Required Python packages (install using `pip install requests smtplib`)

## Installation
1. Clone the repository to your local machine.
2. Navigate to the project directory.

## Configuration
1. Make a copy of the Google Sheet at [this link](https://docs.google.com/spreadsheets/d/1WPZ0_el4qXyjfwq1iZ0W3oEzK0RT5UbyyedOGXrmPJo/edit?usp=sharing).
2. Connect the copied Google Sheet to Sheetly for the API.
3. **Optional:** Fork the Replit at [this link](https://replit.com/@AshtonJordan2/Day-40-Flight-Club#main.py) and add your Sheetly API URL for the "users" tab. Alternatively, you can manually add emails to the "users" tab in the Google Sheet.
5. Open the `settings_vault.py` file and provide your Kiwi API key, SMTP login details, and other configuration settings.

## Usage
1. Run the `main.py` script to initiate the flight search and notification process.
2. Check your email for notifications about affordable flight deals.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
