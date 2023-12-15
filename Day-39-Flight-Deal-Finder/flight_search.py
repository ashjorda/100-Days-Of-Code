import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def city_code(self, city):
        headers = {'accept': 'application/json', 'apikey': 'e32VH4eghtlNc4qOd3jubQAWIZQ5xdWs'}
        query = {"term": city, "location_types": "city"}
        api_url = 'https://api.tequila.kiwi.com/locations/query'
        response = requests.get(url=api_url, headers=headers, params=query)
        results = response.json()['locations']
        code = results[0]['code']
        return code

    def flight_price(self, origin_city, destination_city, departure_date, return_date):
        headers = {
            'accept': 'application/json',
            'apikey': 'e32VH4eghtlNc4qOd3jubQAWIZQ5xdWs',
        }
        query = {
            'fly_from': origin_city,
            'fly_to': destination_city,
            'date_from': departure_date.strftime('%d/%m/%Y'),
            'date_to': return_date.strftime('%d/%m/%Y'),
            'nights_in_dst_from': '7',
            'nights_in_dst_to': '28',
            'flight_type': "round",
            'one_for_cit': '1',
            'max_stopovers': '0',
            'curr': 'USD',
            'vehicle_type': 'aircraft',
            'locale': 'en',
        }
        flight_search_api_url = "https://api.tequila.kiwi.com/v2/search"
        flight_data = requests.get(url=flight_search_api_url, headers=headers, params=query)
        try:
            flight_info = flight_data.json()['data'][0]
            price = flight_info['price']
            city_from = flight_info['cityFrom']
            fly_from = flight_info['flyFrom']
            city_to = flight_info['cityTo']
            fly_to = flight_info['flyTo']
            local_departure = flight_info['local_departure']
            local_arrival = flight_info['local_arrival']

            notification_parameters = {'price': price,
                                       'city_from': city_from,
                                       'fly_from': fly_from,
                                       'city_to': city_to,
                                       'fly_to': fly_to,
                                       'local_departure': local_departure,
                                       'local_arrival': local_arrival
                                       }
            return notification_parameters

        except IndexError:
            pass
