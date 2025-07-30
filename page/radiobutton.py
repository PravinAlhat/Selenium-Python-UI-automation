from selenium import webdriver
from base.SeleniumDriver import SeleniumDriver
from utility.webdirverfactory import WebDriverFactory
from utility.variables import *

class RadioButton(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_radio_button(self, radiobutton):
        radio_button_locator = Variables.radio_button.replace('car', radiobutton)
        self.element = self.wait_for_element(locator=radio_button_locator, locatorType='xpath')
        self.click_element(element=self.element)
        # element_presence = self.is_element_present(self.element)
        # assert element_presence == True

    # def element_practice_submenu(self):
    #     self.click_element(element=self.element)
    #     element_practice_menu = self.wait_for_element(locator=Variables.elementpractice_submenu, locatorType='xpath')
    #     assert element_practice_menu != None
