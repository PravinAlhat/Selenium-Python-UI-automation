from selenium import webdriver
import pytest
from base.SeleniumDriver import SeleniumDriver
from utility.variables import Variables as V

class DropDown(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_car(self, value=None, index=None, text=None):
        self.click_element(locator=V.select_dropdown, locatorType='xpath')
        self.select_from_dropdown(locator=V.select_dropdown, locatorType='xpath', value=value, index=index, text=text)