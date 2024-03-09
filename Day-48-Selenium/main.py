from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")


element = driver.find_element(By.TAG_NAME, 'div')
e_class = element.find_element(By.CLASS_NAME, 'event-widget')
event_list = e_class.find_elements(By.TAG_NAME, 'li')

event_data = {}

key = 0
for event in event_list:
    event_data[key] = {'time': event.text.split('\n')[0], 'name': event.text.split('\n')[1]}
    key +=1

print(event_data)
# driver.close()
driver.quit()
