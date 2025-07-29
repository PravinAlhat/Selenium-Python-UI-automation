from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utility.logger import custom_logger as cl
import logging


class SeleniumDriver():
    log = cl(loglevel=logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locatorType):
        #locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        if locatorType == 'name':
            return By.NAME
        if locatorType == 'xpath':
            return By.XPATH
        if locatorType == 'class':
            return By.CLASS_NAME
        if locatorType == 'css':
            return By.CSS_SELECTOR
        if locatorType == 'tag':
            return By.TAG_NAME
        if locatorType == 'link':
            return By.LINK_TEXT
        if locatorType == 'partial text':
            return By.PARTIAL_LINK_TEXT
    
    def get_element(self, locator, locatorType):
        try:
            locatorType = locatorType.lower()
            by_type = self.get_by_type(locatorType)
            print(by_type)
            element = self.driver.find_element(by_type, locator) 
            #element = self.driver.find_element(By.XPATH, locator)
            if element is not None:
                self.log.info(f"Element with {locator} and {locatorType} is found")
                return element
        except:
            self.log.error(f"Element with {locator} and {locatorType} is not found")
            raise ElementNotVisibleException
    
    def click_element(self, locator=None, locatorType='id', element=None):
        try:
            if locator:
                element = self.get_element(locator, locatorType)
            element.click()
            self.log.info(f"Element: {element} is clicked.")
        except:
            self.log.error(f"Element with {locator} and {locatorType} is NOT clicked.")
            raise NoSuchElementException

    def send_keys(self, data, locator, locatorType='id', element=None):
        try:
            if element:
                element.send_keys(data)
                self.log.info(f"Keys are sent for an element with {locator} and {locatorType}")
            else:
                element = self.get_element(locator, locatorType)
                element.send_keys(data)
                self.log.info(f"Keys are sent for an element with {locator} and {locatorType}")
        except:
            self.log.error(f"Keys are not sent for an element with {locator} and {locatorType}")

    def is_element_present(self, locator=None, locatorType=None, element=None):
        try:
            if element is not None:
                element_check = element.is_displayed()
                return element_check
            else:
                element = self.get_element(locator, locatorType)
                element_check = element.is_displayed()
                return element_check
        except:
            raise ElementNotVisibleException
        
    def wait_for_element(self, locator, locatorType):
        try:
            by_type = self.get_by_type(locatorType)
            wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=1, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException, ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.log.info(f"Element is found with {locator} and {locatorType}")
        except:
            self.log.error(f"Element is not found with {locator} and {locatorType}")
            raise TimeoutError
        return element
        

    

