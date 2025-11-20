from page.swicthwindow import SwitchHandle
import pytest, unittest

@pytest.mark.usefixtures("OneTimeSetup")
class TestSwitchWindow(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, OneTimeSetup):
        self.sw = SwitchHandle(self.driver)

    def test_switch_to_window(self):
        parent_handle = self.sw.get_current_handle()
        self.sw.click_openwindow()
        all_handles = self.sw.get_allhandles()
        self.sw.swicth_to_handle(chandle=parent_handle, allhandles=all_handles)
        self.driver.close()
        self.sw.switch_to_parenthandle(p_handle=parent_handle)
