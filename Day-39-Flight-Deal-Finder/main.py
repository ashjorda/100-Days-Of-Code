# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

import flight_search
from datetime import datetime, timedelta
from data_manager import DataManager

flight_data = DataManager()

# Import Flight Data from Sheetly. Check if Data contains city codes for each destination, if not populate them
#destination_list = flight_data.import_data()
destination_list = {'prices': [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]}
flight_data.city_code_exist(destination_list)


# Check flights
ORIGIN_CITY_IATA = "DFW"
tomorrow = datetime.now() + timedelta(days=1)
six_months_future = tomorrow + timedelta(days=180)

for city in destination_list['prices']:
    dest_city = city['iataCode']
    flight_search.flight_price(ORIGIN_CITY_IATA, dest_city, tomorrow, six_months_future)
