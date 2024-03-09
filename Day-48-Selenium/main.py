from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")


element = driver.find_element(By.TAG_NAME, 'div')
e_class = element.find_element(By.CLASS_NAME, 'event-widget')
events = e_class.find_elements(By.TAG_NAME, 'li')

for date in events:
    print(date.text)

# driver.close()
driver.quit()
