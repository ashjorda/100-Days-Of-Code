from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Signup for the LAB report
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# # Enter First Name on the form
# fname = driver.find_element(By.NAME, value="fName")
# fname.send_keys("John")

# # Enter Last Name in the form
# lname = driver.find_element(By.NAME, value="lName")
# lname.send_keys("Dough")

# # Enter email address in the form
# email = driver.find_element(By.NAME, value="email")
# email.send_keys("jdough@gmail.com")

# Click the submit 
while True:
    click_cookie = driver.find_element(By.CSS_SELECTOR, value='#cookie')
    click_cookie.click()
