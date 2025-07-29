from base.SeleniumDriver import SeleniumDriver
from page.practice import PracticePage
import conftest
import pytest
import unittest
from utility.variables import Variables

@pytest.mark.usefixtures("OneTimeSetup")
class PracticePaPgeTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, OneTimeSetup):
        self.pp = PracticePage(self.driver)

    def test_practice_homepage(self):
        self.pp.is_practice_page_displayed()
        







#def test_navigate_practice_page(self):