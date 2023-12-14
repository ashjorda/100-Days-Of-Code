import requests
from flight_search import FlightSearch


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def import_data(self):
        api_url = 'https://api.sheety.co/c0f6856a82dab9a3b8def4c44041939b/flightDeals/prices'
        data = requests.get(url=api_url)
        return data.json()

    def city_code_exist(self, data):
        flight = FlightSearch()
        for _ in data['prices']:
            if len(_['iataCode']) == 0:
                city_code = flight.city_code(_['city'])
                _['iataCode'] = city_code
                body = {
                    "price": {
                        "iataCode": city_code,
                    }
                }
                requests.put(url=f"https://api.sheety.co/c0f6856a82dab9a3b8def4c44041939b/flightDeals/prices/{_['id']}",
                             json=body)

