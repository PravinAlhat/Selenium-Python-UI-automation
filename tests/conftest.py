import pytest
from selenium import webdriver
from utility import webdirverfactory as wd
import time

@pytest.fixture(scope="class")
def OneTimeSetup(request, browser, url, headless):
    wdf = wd.WebDriverFactory(browser, url, headless)
    driver = wdf.get_webdriver_instance()
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    time.sleep(2)
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")
    parser.addoption("--headless")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope="session")
def headless(request):
    return request.config.getoption("--headless")



