"""_summary_
Basic Selenium
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def test_title(firefox_browser):
    """
    Test the title of the Python.org website
    """
    firefox_browser.get("https://www.python.org")
    assert firefox_browser.title == "Welcome to Python.org"


def test_search(firefox_browser):
    """
    Test the search functionality of the DuckDuckGo website
    """
    url = "https://duckduckgo.com/"
    search_term = "Pytest with Eric"
    # Navigate to the Google home page.
    firefox_browser.get(url)
    # Find the search box using its name attribute value.
    search_box = firefox_browser.find_element(By.ID, value="searchbox_input")
    # Enter a search query and submit.
    search_box.send_keys(search_term + Keys.RETURN)
    # Assert that the title contains the search term.
    assert search_term in firefox_browser.title


def test_login_functionality(firefox_browser):
    """
    Test the login functionality of the Practice Test Automation website
    """
    url = "https://practicetestautomation.com/practice-test-login/"
    # Navigate to the login page
    firefox_browser.get(url)
    # Find and fill the username and password fields
    firefox_browser.find_element(By.ID, "username").send_keys("student")
    firefox_browser.find_element(By.ID, "password").send_keys("Password123")
    # Find and click the login button
    firefox_browser.find_element(By.ID, "submit").click()
    # Verify that the login was successful
    # by checking the presence of a logout button
    # Option 1: Locate by class name (if unique and reliable)
    try:
        logout_button = firefox_browser.find_element(
            By.CLASS_NAME, "wp-block-button__link"
        )
        assert logout_button.is_displayed(), "Logout button is not displayed."
    except NoSuchElementException:
        assert False, "Logout button does not exist."
    # Option 2: Locate by link text (if the text is unique and reliable)
    try:
        logout_button = firefox_browser.find_element(By.LINK_TEXT, "Log out")
        assert logout_button.is_displayed(), "Logout button is not displayed."
    except NoSuchElementException:
        assert False, "Logout button does not exist."
