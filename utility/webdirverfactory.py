from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import  Options as co
from selenium.webdriver.firefox.options import Options as fo


class WebDriverFactory():

    def __init__(self, browser, url, headless):
        self.browser = browser
        self.url = url
        self.headless = headless

    # def get_webdriver_instance(self):
    #     if self.browser == "chrome":
    #         chrome_options = co()
    #         driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    #     if self.browser == "firefox":
    #         driver = webdriver.Firefox()
    #     driver.get(self.url)
    #     driver.maximize_window()
    #     driver.implicitly_wait(10)
    #     return driver

    def get_webdriver_instance(self):
        if self.browser == "chrome":
            chrome_options = co()
            if self.headless in ['Y', 'y', 'YES', 'yes']:
                chrome_options.add_argument('--headless')
                driver = webdriver.Chrome(options=chrome_options)
            else:
                driver = webdriver.Chrome(options=chrome_options)
        if self.browser == 'firefox':
            firefox_options = fo()
            if self.headless in ['Y', 'y', 'YES', 'yes']:
                #firefox_options.headless = True
                firefox_options.add_argument('--headless')
                driver = webdriver.Firefox(options=firefox_options)
            else:
                firefox_options.headless = False
                driver = webdriver.Firefox(options=firefox_options)

        driver.get(self.url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver
        