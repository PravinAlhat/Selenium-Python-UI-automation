from selenium import webdriver
from base.SeleniumDriver import SeleniumDriver
from utility.webdirverfactory import WebDriverFactory
from utility.variables import *

class CheckBox(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_check_box(self, checkbox):
        checkbox_locator = Variables.check_box.replace('car', checkbox)
        self.element = self.wait_for_element(locator=checkbox_locator, locatorType='xpath')
        self.click_element(element=self.element)
