import requests
from datetime import datetime, timedelta
from flight_data import FlightData


def flight_price(origin_city, destination_city, departure_date, return_date):
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
    price_data = requests.get(url=flight_search_api_url, headers=headers, params=query)
    try:
        city = price_data.json()['data'][0]['cityTo']
        price = price_data.json()['data'][0]['price']
        print(f"{city}: {price}")
    except IndexError:
        pass


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def city_code(city):
        headers = {'accept': 'application/json', 'apikey': 'e32VH4eghtlNc4qOd3jubQAWIZQ5xdWs'}
        query = {"term": city, "location_types": "city"}
        api_url = 'https://api.tequila.kiwi.com/locations/query'
        response = requests.get(url=api_url, headers=headers, params=query)
        results = response.json()['locations']
        code = results[0]['code']
        return code
