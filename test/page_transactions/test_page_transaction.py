from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from guara.transaction import AbstractTransaction, Application
from guara import it


# Transaction for logging in
class Login(AbstractTransaction):
    def __init__(self, driver, username, password):
        super().__init__(driver)
        self.username = username
        self.password = password

    def do(self, **kwargs):
        # Navigate to the login page
        self._driver.get("https://practicetestautomation.com/practice-test-login/")

        # Fill in the username and password
        self._driver.find_element(By.ID, "username").send_keys(self.username)
        self._driver.find_element(By.ID, "password").send_keys(self.password)

        # Click the login button
        self._driver.find_element(By.ID, "submit").click()

        # Verify login by checking if the logout button appears
        try:
            logout_button = self._driver.find_element(
                By.CLASS_NAME, "wp-block-button__link"
            )
            assert logout_button.is_displayed(), "Logout button is not displayed."
        except NoSuchElementException:
            return "Logout button does not exist."

        try:
            logout_button = self._driver.find_element(By.LINK_TEXT, "Log out")
            assert logout_button.is_displayed(), "Logout button is not displayed."
        except NoSuchElementException:
            return "Logout button does not exist."

        return "Login successful"


# Example of using Guará to validate the framework's capabilities
def test_login_functionality(firefox_browser):
    # Create Application instance with Firefox WebDriver
    # Run login transaction with Guará
    Application(firefox_browser).at(
        Login,
        username="student",
        password="Password123",
    ).asserts(it.IsEqualTo, "Login successful")
