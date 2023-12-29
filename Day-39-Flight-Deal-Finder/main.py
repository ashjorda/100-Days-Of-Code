# Import necessary modules
from datetime import datetime, timedelta
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from settings_vault import Settings

# Create instances of DataManager, FlightSearch, and NotificationManager
flight_data = DataManager()
flight_search = FlightSearch()
notification_service = NotificationManager()
settings = Settings()

# Import flight data from Sheetly
destination_list = flight_data.import_data()

# Check if the imported data contains city codes for each destination, populate them if missing
flight_data.city_code_exist(destination_list)

# Set the origin city code and define time parameters for flight search
ORIGIN_CITY_IATA = settings.airport_code
tomorrow = datetime.now() + timedelta(days=1)
six_months_future = tomorrow + timedelta(days=180)

# Loop through each destination in the list and check flight prices
for city in destination_list['prices']:
    destination_code = city['iataCode']
    my_price = city['maxPrice']

    # Perform flight search for the specified origin and destination cities and time frame
    available_flights = flight_search.dest_city(
        origin_city=ORIGIN_CITY_IATA,
        destination_city=destination_code,
        departure_date=tomorrow,
        return_date=six_months_future,
    )

    # Check if there are available flights within the specified budget
    if available_flights:
        if available_flights['price'] <= my_price:
            # Send email notification for the affordable flight
            notification_service.send_email(available_flights)