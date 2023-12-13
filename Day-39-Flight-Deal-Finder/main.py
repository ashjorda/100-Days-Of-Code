# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
#
from data_manager import DataManager
from flight_search import FlightSearch

flight_search = FlightSearch
data_manager = DataManager

# # data_manager.check_iata(data_manager.get_sheetly_data())


DataManager.get_iata()
