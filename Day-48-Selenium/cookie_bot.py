from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

seconds = 0
cps = driver.find_element(By.CSS_SELECTOR, value='#cps')

start_time = time.time()
elapsed_time = 0

while True:
    if seconds != 4: 
        click_cookie = driver.find_element(By.CSS_SELECTOR, value='#cookie')
        click_cookie.click()
        seconds +=1
    elif seconds == 4:
        money = driver.find_element(By.CSS_SELECTOR, value='#money')
        store = driver.find_elements(By.CSS_SELECTOR, "#store div b")
        cookies = int(money.text)
        afford = {}
        for items in store:
            if len(items.text) > 0:
                if cookies >= int(items.text.split('- ')[1].replace(',', '')):
                    afford[f"buy{items.text.split('-')[0]}"] =  int(items.text.split('- ')[1].replace(',', ''))
        if not bool(afford) != True:
            buy_expensive_item = max(zip(afford.values(), afford.keys()))[1]
            buy_button = driver.find_element(By.CSS_SELECTOR, value=f'#{buy_expensive_item}')
            buy_button.click()
        seconds = 0
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > 5 * 60:
        print(f"Cookies/Second: {cps.text}")
        break

driver.quit()