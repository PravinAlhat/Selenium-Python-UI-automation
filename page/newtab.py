from base.SeleniumDriver import SeleniumDriver
import pytest, time
from utility.variables import Variables as V

class Tab(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_tab(self):
        self.click_element(locator=V.open_tab_btn_xpath, locatorType='xpath')

    def get_current_tabhandle(self):
        current_whandle = self.driver.current_window_handle
        return current_whandle
    
    def get_alltabhandles(self):
        all_handles = self.driver.window_handles
        return all_handles
    
    def swicth_to_tab(self, chandle, allhandles):
        for handle in allhandles:
            if handle != chandle:
                self.driver.switch_to.window(handle)
                break
        window_title = self.driver.title
        print(f"Switched to the desired handle {window_title}")
        time.sleep(2)
    
    def switch_to_parenttab(self, p_handle):
        self.driver.switch_to.window(p_handle)