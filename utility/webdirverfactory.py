from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def get_webdriver_instance(self):
        if self.browser == "chrome":
            driver = webdriver.Chrome()
            driver.get(self.url)
            driver.maximize_window()
            driver.implicitly_wait(10)
            return driver
        