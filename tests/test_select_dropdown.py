from selenium import webdriver
import pytest, unittest
from parameterized import parameterized
from page.dropdown_select import DropDown
from utilities.excel_ops import exl_to_dict

@pytest.mark.usefixtures("OneTimeSetup")
class TestDropDown(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, OneTimeSetup):
        self.dd = DropDown(self.driver)

    # @parameterized.expand(["benz", "honda", "bmw"])
    # def test_selec_car_from_dropdown(self, car):
    #     self.dd.select_car(value=car)

    def test_select_car_by_name_Benz(self):
        cars = exl_to_dict()
        for car in cars:
            if car['Car Name']=='Benz':
                self.dd.select_car(text=car['Car Name'])
            break
