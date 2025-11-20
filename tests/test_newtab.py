from page.newtab import Tab
import pytest, unittest
from utility.variables import Variables as V

@pytest.mark.usefixtures("OneTimeSetup")
class TestTab(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, OneTimeSetup):
        self.nt = Tab(self.driver)

    def test_open_new_tab(self):
        cthandle = self.nt.get_current_tabhandle()
        self.nt.open_tab()
        allthandles = self.nt.get_alltabhandles()
        self.nt.swicth_to_tab(chandle=cthandle, allhandles=allthandles)
        self.driver.close()
        self.nt.switch_to_parenttab(cthandle)