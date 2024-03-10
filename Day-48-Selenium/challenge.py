from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Signup for the LAB report
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Enter First Name on the form
fname = driver.find_element(By.NAME, value="fName")
fname.send_keys("John")

# Enter Last Name in the form
lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("Dough")

# Enter email address in the form
email = driver.find_element(By.NAME, value="email")
email.send_keys("jdough@gmail.com")

# Click the submit button
submit_button = driver.find_element(By.CSS_SELECTOR, value='.btn')
submit_button.click()
