import requests
from datetime import datetime, timedelta


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_iata(city):
        headers = {
            'accept': 'application/json',
            'apikey': 'e32VH4eghtlNc4qOd3jubQAWIZQ5xdWs',
        }
        api_url = (f'https://api.tequila.kiwi.com/locations/query?term={city}&locale=en-US&location_types=city&limit'
                   f'=10&active_only=true')
        response = requests.get(url=api_url, headers=headers)
        return response.json()['locations'][0]['code']

    def flight_price(iata_code):
        current_date = datetime.now()
        tomorrow = current_date + timedelta(days=1)
        six_months_future = tomorrow + timedelta(days=180)
        from_city = 'DFW'
        headers = {
            'accept': 'application/json',
            'apikey': 'e32VH4eghtlNc4qOd3jubQAWIZQ5xdWs',
        }
        flight_search_api_url = f"https://api.tequila.kiwi.com/v2/search?fly_from={from_city}&fly_to={iata_code}&date_from={tomorrow.strftime('%d/%m/%Y')}&date_to={six_months_future.strftime('%d/%m/%Y')}&nights_in_dst_from=7&nights_in_dst_to=28&ret_from_diff_city=false&ret_to_diff_city=false&one_for_city=1&one_per_date=0&adults=1&children=0&infants=0&adult_hold_bag=2&adult_hand_bag=1&only_working_days=false&only_weekends=false&partner_market=us&curr=USD&locale=en&price_from=1000&price_to=7000&max_stopovers=0&vehicle_type=aircraft&sort=price&limit=500"
        price_data = requests.get(url=flight_search_api_url, headers=headers)
        try:
            city = price_data.json()['data'][0]['cityTo']
            price = price_data.json()['data'][0]['price']
            return f"{city}: {price}"
        except IndexError:
            pass
