# Exercise Tracker

This Python script tracks exercise activities using the Nutritionix API and updates a Google Docs Spreadsheet with exercise details.

## Prerequisites

Before running the script, ensure you have the following:

- Python (version 3.x) installed on your machine.
- Required Python packages: `requests`. You can install it using the following command:

```bash
pip install requests
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/exercise-tracker.git
```

2. Navigate to the project directory:

```bash
cd exercise-tracker
```

3. Edit the script and set the required configuration variables:

   - `APP_ID`: Your Nutritionix API ID.
   - `APP_KEY`: Your Nutritionix API key.
   - `API_URL`: Nutritionix API endpoint for exercise tracking.
   - `SHEETY_API_URL`: Sheety API endpoint for updating the Google Docs Spreadsheet.

4. Run the script:

```bash
python exercise_tracker.py
```

The script will prompt you to input the exercise(s) you did. It will then send this information to the Nutritionix API to retrieve details such as duration and calories burned. Finally, it updates a Google Docs Spreadsheet with the exercise details.

Feel free to customize the script based on your specific needs or integrate it into a larger project.

## Acknowledgments

- The script uses the Nutritionix API for exercise tracking.
- Google Docs Spreadsheet is updated using the Sheety API.

Happy exercising!