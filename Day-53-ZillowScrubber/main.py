import requests
from bs4 import BeautifulSoup

listing_site = requests.get(url='https://appbrewery.github.io/Zillow-Clone/')

listing_site_parsed = BeautifulSoup(listing_site.text, features="html.parser")

property_address_links = [address['href'] for address in listing_site_parsed.find_all(name='a', href=True, class_="property-card-link")]

