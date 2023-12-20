from datetime import datetime, timedelta
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

flight_data = DataManager()
flight_search = FlightSearch()
notification_service = NotificationManager()

# Import Flight Data from Sheetly
destination_list = flight_data.import_data()


# Check if Data contains city codes for each destination, if not populate them
flight_data.city_code_exist(destination_list)

# # Check prices of flights from ORIGIN_CITY_IATA to city's listed in destination_list
ORIGIN_CITY_IATA = "DFW"
tomorrow = datetime.now() + timedelta(days=1)
six_months_future = tomorrow + timedelta(days=180)

for city in destination_list['prices']:
    destination_code = city['iataCode']
    my_price = city['maxPrice']

    available_flights = flight_search.dest_city(origin_city=ORIGIN_CITY_IATA,
                                                destination_city=destination_code,
                                                departure_date=tomorrow,
                                                return_date=six_months_future,
                                                )
    if available_flights:
        if available_flights['price'] <= my_price:
            notification_service.send_email(available_flights)
