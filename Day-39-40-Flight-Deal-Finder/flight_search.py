import requests
from settings_vault import Settings


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        # Initialize FlightSearch with API credentials from Settings
        self.credentials = Settings()

    def city_code(self, city):
        """
        Get the IATA code for a given city using the Flight Search API.
        :param city: Name of the city.
        :return: IATA code for the city.
        """
        api_key = self.credentials.kiwi_api_key
        headers = {'accept': 'application/json', 'apikey': f'{api_key}'}
        query = {"term": city, "location_types": "city"}
        api_url = 'https://api.tequila.kiwi.com/locations/query'
        response = requests.get(url=api_url, headers=headers, params=query)

        try:
            results = response.json()['locations']
            code = results[0]['code']
            return code
        except KeyError:
            print(f"{response.json()} Please populate 'self.kiwi_api_key' in settings_vault.py file")

    def dest_city(self, origin_city, destination_city, departure_date, return_date):
        """
        Search for available flights between the specified origin and destination cities.
        :param origin_city: IATA code for the origin city.
        :param destination_city: IATA code for the destination city.
        :param departure_date: Departure date for the flight.
        :param return_date: Return date for the flight.
        :return: Notification parameters for affordable flights.
        """
        api_key = self.credentials.kiwi_api_key
        headers = {'accept': 'application/json', 'apikey': f'{api_key}'}
        query = {
            'fly_from': origin_city,
            'fly_to': destination_city,
            'date_from': departure_date.strftime('%d/%m/%Y'),
            'date_to': return_date.strftime('%d/%m/%Y'),
            'nights_in_dst_from': '7',
            'nights_in_dst_to': '28',
            'flight_type': "round",
            'one_for_city': '1',
            'max_stopovers': '0',
            'curr': 'USD',
            'vehicle_type': 'aircraft',
            'locale': 'en',
        }
        flight_search_api_url = "https://api.tequila.kiwi.com/v2/search"
        flight_data = requests.get(url=flight_search_api_url, headers=headers, params=query)

        try:
            flight_results = flight_data.json()['data'][0]
        except IndexError:
            try:
                # If no direct flights found, allow up to 2 stopovers
                query['max_stopovers'] = 2
                flight_search_api_url = "https://api.tequila.kiwi.com/v2/search"
                flight_data = requests.get(url=flight_search_api_url, headers=headers, params=query)
                flight_results = flight_data.json()['data'][0]
                notification_parameters = {'nights_in_dest': flight_results['nightsInDest'],
                                           'price': flight_results['fare']['adults'],
                                           'depart_city_from': flight_results['route'][0]['cityFrom'],
                                           'depart_fly_from': flight_results['route'][0]['flyFrom'],
                                           'depart_city_to': flight_results['route'][1]['cityTo'],
                                           'depart_fly_to': flight_results['route'][1]['flyTo'],
                                           'depart_local_departure': flight_results['route'][0]['local_departure'].split("T")[0],
                                           'depart_local_arrival': flight_results['route'][1]['local_departure'].split("T")[0],
                                           'layover_city': flight_results['route'][0]['cityTo'],
                                           'booking_link': flight_results['deep_link'],
                                           # Additional parameters for multi-stop flights
                                           }
                return notification_parameters
            except IndexError:
                pass
        else:
            notification_parameters = {'nights_in_dest': flight_results['nightsInDest'],
                                       'price': flight_results['fare']['adults'],
                                       'depart_city_from': flight_results['route'][0]['cityFrom'],
                                       'depart_fly_from': flight_results['route'][0]['flyFrom'],
                                       'depart_city_to': flight_results['route'][0]['cityTo'],
                                       'depart_fly_to': flight_results['route'][0]['flyTo'],
                                       'depart_local_departure': flight_results['route'][0]['local_departure'].split("T")[0],
                                       'depart_local_arrival': flight_results['route'][1]['local_departure'].split("T")[0],
                                       'booking_link': flight_results['deep_link'],
                                       }
            return notification_parameters
