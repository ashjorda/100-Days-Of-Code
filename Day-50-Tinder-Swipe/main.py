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



# # # Enter Username
# username = driver.find_element(By.ID, value="username")
# username.send_keys("dev.linkedin6@gmail.com")

# # Enter Password
# password = driver.find_element(By.ID, value="password")
# password.send_keys("BE.mature.2018")

# time.sleep(3) # Wait 3 seconds before clicking the sign in button

# # Click the sign in button
# click_sign_in = driver.find_element(By.CLASS_NAME, value="btn__primary--large ")
# click_sign_in.click()

# time.sleep(3) # Wait 3 seconds before clicking the sign in button
# # Click the save button
# click_save = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
# click_save.click()

#Complete