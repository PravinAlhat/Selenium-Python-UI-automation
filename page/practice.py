from selenium import webdriver
from base.SeleniumDriver import SeleniumDriver
from utility.webdirverfactory import WebDriverFactory
from utility.variables import *

class PracticePage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_practice_page_displayed(self):
        practice_page_element = self.wait_for_element(locator=Variables.PRACTICE_PAGE, locatorType='xpath')
        assert practice_page_element != None
