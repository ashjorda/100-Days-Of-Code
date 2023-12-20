import requests
from settings_vault import Settings


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.credentials = Settings()

    def city_code(self, city):
        api_key = self.credentials.kiwi_api_key
        headers = {'accept': 'application/json', 'apikey': f'{api_key}'}
        query = {"term": city, "location_types": "city"}
        api_url = 'https://api.tequila.kiwi.com/locations/query'
        response = requests.get(url=api_url, headers=headers, params=query)
        results = response.json()['locations']
        code = results[0]['code']
        return code

    def dest_city(self, origin_city, destination_city, departure_date, return_date):
        api_key = self.credentials.kiwi_api_key
        headers = {f'accept': 'application/json', 'apikey': f'{api_key}'}
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
        flight_results = flight_data.json()['data']
        try:
            # Flight Info specific to price, and total nights
            flight_info = flight_results[0]
            price = flight_info['fare']['adults']
            nights_in_dest = flight_info['nightsInDest']

            # Flight departure information
            flight_route_info = flight_results[0]['route'][0]
            depart_city_from = flight_route_info['cityFrom']
            depart_fly_from = flight_route_info['flyFrom']
            depart_city_to = flight_route_info['cityTo']
            depart_fly_to = flight_route_info['flyTo']
            depart_local_departure = flight_route_info['local_departure']
            depart_local_arrival = flight_route_info['local_arrival']

            # Flight return information
            flight_route_info = flight_results[0]['route'][1]
            return_city_from = flight_route_info['cityFrom']
            return_fly_from = flight_route_info['flyFrom']
            return_city_to = flight_route_info['cityTo']
            return_fly_to = flight_route_info['flyTo']
            return_local_departure = flight_route_info['local_departure']
            return_local_arrival = flight_route_info['local_arrival']

            notification_parameters = {'nights_in_dest': nights_in_dest,
                                       'price': price,
                                       'depart_city_from': depart_city_from,
                                       'depart_fly_from': depart_fly_from,
                                       'depart_city_to': depart_city_to,
                                       'depart_fly_to': depart_fly_to,
                                       'depart_local_departure': depart_local_departure,
                                       'depart_local_arrival': depart_local_arrival,
                                       'return_city_from': return_city_from,
                                       'return_fly_from': return_fly_from,
                                       'return_city_to': return_city_to,
                                       'return_fly_to': return_fly_to,
                                       'return_local_departure': return_local_departure,
                                       'return_local_arrival': return_local_arrival,
                                       }
            return notification_parameters

        except IndexError:
            pass
