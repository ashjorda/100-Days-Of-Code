from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")

# Wait 5 seconds before entering the login credentials
time.sleep(5)

# Click login button on main page
login_in = driver.find_element(By.LINK_TEXT, value="Log in")
login_in.click()

# Wait 5 seconds before entering the login credentials
time.sleep(5)

# Switch frame by id
login_google = driver.find_element(By.XPATH, '//*[@id="gsi_802342_709961"]')
login_google.click()