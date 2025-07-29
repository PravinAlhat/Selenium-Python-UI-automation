from selenium import webdriver
from base.SeleniumDriver import SeleniumDriver
from utility.webdirverfactory import WebDriverFactory
from utility.variables import *

class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login_successsful(self):
        element = self.get_element(locator=Variables.home_menu, locatorType='xpath')
        is_element_present = self.is_element_present(element=element)
        assert is_element_present == True

    def practice_page(self):
        self.element = self.wait_for_element(locator=Variables.practice_menu, locatorType='xpath')
        # element_presence = self.is_element_present(self.element)
        # assert element_presence == True

    def element_practice_submenu(self):
        self.click_element(element=self.element)
        element_practice_menu = self.wait_for_element(locator=Variables.elementpractice_submenu, locatorType='xpath')
        assert element_practice_menu != None
