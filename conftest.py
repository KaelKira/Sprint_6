import pytest
from selenium import webdriver
from constants import Constants


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.get(Constants.MAIN_URL)
    yield browser
    browser.quit()
