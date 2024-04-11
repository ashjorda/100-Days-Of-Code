from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:

    def __init__(self):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.speedtest.net/")

    def get_internet_speed(self):
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()

        time.sleep(60)
        self.down = float(self.driver.find_element_by_css_selector(".download-speed").text)
        self.up = float(self.driver.find_element_by_css_selector(".upload-speed").text)

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN and self.up < PROMISED_UP:
            message = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
            driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
            driver.get("https://twitter.com/")