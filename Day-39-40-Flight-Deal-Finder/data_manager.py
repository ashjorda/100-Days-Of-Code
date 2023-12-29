import requests
from flight_search import FlightSearch
from settings_vault import Settings


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        # Initialize DataManager with settings and FlightSearch instances
        self.settings = Settings()
        self.flight = FlightSearch()

    def import_data(self):
        """
        Import flight data from the Google Sheet.
        :return: JSON data containing flight information.
        """
        api_url = self.settings.flight_destinations
        data = requests.get(url=api_url)
        return data.json()

    def import_members(self):
        """
        Import user data from the Google Sheet.
        :return: JSON data containing user information.
        """
        api_url = self.settings.email_list
        data = requests.get(url=api_url)
        return data.json()

    def city_code_exist(self, data):
        """
        Check if city codes exist in the provided data. If not, fetch and update city codes.
        :param data: JSON data containing flight information.
        """

        for _ in data['prices']:
            if len(_['iataCode']) == 0:
                # If city code is missing, fetch and update it
                city_code = self.flight.city_code(_['city'])
                _['iataCode'] = city_code
                body = {
                    "price": {
                        "iataCode": city_code,
                    }
                }
                # Update the Google Sheet with the newly obtained city code
                requests.put(
                    url=self.settings.flight_destinations + _['id'],
                    json=body)
