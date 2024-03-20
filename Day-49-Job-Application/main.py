from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

# Sigin into Linkedin
sign_in = driver.find_element(By.CLASS_NAME, value="btn-secondary-emphasis")
sign_in.click()

# Wait 5 seconds before entering the login credentials
time.sleep(3)

# # Enter Username
username = driver.find_element(By.ID, value="username")
username.send_keys("dev.linkedin6@gmail.com")

# Enter Password
password = driver.find_element(By.ID, value="password")
password.send_keys("BE.mature.2018")

click_sign_in = driver.find_element(By.CLASS_NAME, value="btn__primary--large ")
click_sign_in.click()