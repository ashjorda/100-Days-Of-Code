import requests
from bs4 import BeautifulSoup

listing_site = requests.get(url='https://appbrewery.github.io/Zillow-Clone/')

listing_site_parsed = BeautifulSoup(listing_site.text, features="html.parser")

property_address_links = [address['href'] for address in listing_site_parsed.find_all(name='a', href=True, class_="property-card-link")]

property_prices = []
for price in listing_site_parsed.find_all(name='span', class_="PropertyCardWrapper__StyledPriceLine"):
    price_slash = price.get_text().split('/')
    price_plus = price_slash[0].split('+')
    property_prices.append(price_plus[0])

print(property_prices)
form = "https://docs.google.com/forms/d/e/1FAIpQLScqwyl9a4WW8jBrjc0-Qu5Z77cOjMtkcsyvoBOr2IY76yfoFg/viewform?usp=sf_link"