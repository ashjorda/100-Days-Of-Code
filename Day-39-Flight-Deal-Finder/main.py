# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from flight_search import FlightSearch
from datetime import datetime, timedelta
from data_manager import DataManager

flight_data = DataManager()
flight_search = FlightSearch()

# Import Flight Data from Sheetly
destination_list = flight_data.import_data()

# Check if Data contains city codes for each destination, if not populate them
flight_data.city_code_exist(destination_list)


# Check prices of flights from ORIGIN_CITY_IATA to city's listed in destination_list
ORIGIN_CITY_IATA = "DFW"
tomorrow = datetime.now() + timedelta(days=1)
six_months_future = tomorrow + timedelta(days=180)
notification_parameters = []

for city in destination_list['prices']:
    destination_city = city['iataCode']
    flight_search.flight_price(origin_city=ORIGIN_CITY_IATA,
                               destination_city=destination_city,
                               departure_date=tomorrow,
                               return_date=six_months_future,
                               notification_message=notification_parameters)

print(notification_parameters)