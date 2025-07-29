from base.SeleniumDriver import SeleniumDriver
from page.login import LoginPage
import pytest
import unittest
from utility.variables import Variables

@pytest.mark.usefixtures("OneTimeSetup")
class HomePageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, OneTimeSetup):
        self.hp = LoginPage(self.driver)

    def test_home_page(self):
        self.hp.login_successsful()

    def test_pratice_menu(self):
        self.hp.practice_page()
        self.hp.element_practice_submenu()
        



