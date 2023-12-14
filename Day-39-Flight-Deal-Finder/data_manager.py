import requests
from flight_search import FlightSearch


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def import_data(self):
        api_url = 'https://api.sheety.co/c0f6856a82dab9a3b8def4c44041939b/flightDeals/prices'
        data = requests.get(url=api_url)
        return data.json()

    def city_code_exist(self, data):
        for _ in data['prices']:
            if len(_['iataCode']) == 0:
                body = {
                    "price": {
                        "iataCode": FlightSearch.city_code(_['city']),
                    }
                }
                requests.put(url=f"https://api.sheety.co/c0f6856a82dab9a3b8def4c44041939b/flightDeals/prices/{_['id']}",
                             json=body)

