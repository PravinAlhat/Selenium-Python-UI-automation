from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebDriverFactory():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def get_webdriver_instance(self):
        if self.browser == "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(self.url)
            driver.maximize_window()
            driver.implicitly_wait(10)
            return driver
        