from base.SeleniumDriver import SeleniumDriver
from page.radiobutton import RadioButton
import pytest
import unittest
from utility.variables import Variables

@pytest.mark.usefixtures("OneTimeSetup")
class PracticePaPgeTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, OneTimeSetup):
        self.rb = RadioButton(self.driver)

    def test_selectradiobutton(self):
        self.rb.select_radio_button('bmw')
        self.rb.select_radio_button('benz')
        self.rb.select_radio_button('honda')
        







#def test_navigate_practice_page(self):