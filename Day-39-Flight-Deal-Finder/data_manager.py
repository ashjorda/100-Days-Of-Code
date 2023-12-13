import requests
from flight_search import FlightSearch


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def get_sheetly_data():
        api_url = 'https://api.sheety.co/c0f6856a82dab9a3b8def4c44041939b/flightDeals/prices'
        data = requests.get(url=api_url)
        return data.json()['prices']

    def check_iata(sheetdata):
        for _ in sheetdata:
            if len(_['iataCode']) == 0:
                body = {
                    "price": {
                        "iataCode": FlightSearch.get_iata(_['city']),
                    }
                }
                requests.put(url=f"https://api.sheety.co/c0f6856a82dab9a3b8def4c44041939b/flightDeals/prices/{_['id']}",
                             json=body)

    def get_iata():
        api_url = 'https://api.sheety.co/c0f6856a82dab9a3b8def4c44041939b/flightDeals/prices'
        data = requests.get(url=api_url)
        for iata in data.json()['prices']:
            print(FlightSearch.flight_price(iata['iataCode']))