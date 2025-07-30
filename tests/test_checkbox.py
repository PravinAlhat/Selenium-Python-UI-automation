from base.SeleniumDriver import SeleniumDriver
from page.checkbox import CheckBox
import pytest
import unittest
from utility.variables import Variables

@pytest.mark.usefixtures("OneTimeSetup")
class PracticePaPgeTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, OneTimeSetup):
        self.cb = CheckBox(self.driver)

    def test_checkbox(self):
        self.cb.select_check_box('bmw')
        self.cb.select_check_box('benz')
        self.cb.select_check_box('honda')
        







#def test_navigate_practice_page(self):