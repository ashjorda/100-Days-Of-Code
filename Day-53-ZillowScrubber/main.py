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

for rental in range(len(property_address)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScqwyl9a4WW8jBrjc0-Qu5Z77cOjMtkcsyvoBOr2IY76yfoFg/viewform?usp=sf_link")
    time.sleep(2)

    # Enter Property Address
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(property_address[rental])

    # Enter Property Price
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(property_prices[rental])

    # Enter Property Link
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(property_listing[rental])

    time.sleep(1) # Wait 2 seconds before clicking the sign in button

    # Click the sign in button
    click_sign_in = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    click_sign_in.click()
