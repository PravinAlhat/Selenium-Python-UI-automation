import pytest
from selenium import webdriver
from utility import webdirverfactory as wd
import time

@pytest.yield_fixture(scope="class")
def OneTimeSetup(request, browser, url):
    print(browser)
    print(url)
    wdf = wd.WebDriverFactory(browser, url)
    driver = wdf.get_webdriver_instance()
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    time.sleep(2)
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")




