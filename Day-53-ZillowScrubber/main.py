import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


listing_site = requests.get(url='https://appbrewery.github.io/Zillow-Clone/')

listing_site_parsed = BeautifulSoup(listing_site.text, features="html.parser")

property_listing = [listing_link['href'] for listing_link in listing_site_parsed.find_all(name='a', href=True, class_="property-card-link")]

property_prices = []
for price in listing_site_parsed.find_all(name='span', class_="PropertyCardWrapper__StyledPriceLine"):
    price_slash = price.get_text().split('/')
    price_plus = price_slash[0].split('+')
    property_prices.append(price_plus[0])

property_address = [address.get_text(strip=True) for address in listing_site_parsed.find_all(name='address')]

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLScqwyl9a4WW8jBrjc0-Qu5Z77cOjMtkcsyvoBOr2IY76yfoFg/viewform?usp=sf_link")

# Enter Property Address
form_address = driver.find_element(By.CLASS_NAME, value="Xb9hP")
form_address.send_keys(property_address[0])

# time.sleep(3) # Wait 3 seconds before clicking the sign in button

# Click the sign in button
# click_sign_in = driver.find_element(By.CLASS_NAME, value="btn__primary--large ")
# click_sign_in.click()
