from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class SeleniumHelper:
    def __init__(self, headless=True, wait=2):
        self.wait = wait
        options = Options()
        if headless:
            options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def get_page(self, url):
        self.driver.get(url)
        time.sleep(self.wait)
        return self.driver.page_source

    def close(self):
        self.driver.quit()
