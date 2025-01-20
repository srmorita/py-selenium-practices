"""
conftest.py
"""
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def firefox_browser():
    """
    Setting a firefox browser fixture
    """
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
