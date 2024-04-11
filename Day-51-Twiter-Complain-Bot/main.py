from selenium import webdriver
from selenium.webdriver.common.by import By
import time


PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "ashton.jordan@gmail.com"
TWITTER_PASSWORD = "YOUR PASSWORD"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:

    def __init__(self):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.speedtest.net/")

    def get_internet_speed(self):
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()

        time.sleep(30)
        self.down = float(self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text)
        self.up = float(self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text)

        print(f"down: {self.down} up: {self.up}")
        self.driver.close()
        self.driver.quit()

    def tweet_at_provider(self):
        if self.down < 150 and self.up < PROMISED_UP:
            message = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
            driver = webdriver.Chrome(options=chrome_options)
            driver.get("https://twitter.com/")

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
