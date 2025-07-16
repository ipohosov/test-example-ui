import allure
from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config.config import Config
from utils.allure_decorators import allure_step, logger


class BaseElement:
    def __init__(self, driver: WebDriver, locator):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.DEFAULT_TIMEOUT)
        self._locator = locator

    @allure_step("Find element by locator")
    def find_element(self):
        """Find an element with explicit wait"""
        try:
            element = self.wait.until(
                EC.presence_of_element_located(self._locator)
            )
            logger.info(f"Element found: {self._locator}")
            return element
        except TimeoutException as e:
            allure.attach(str(e), name="Element not found", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure_step("Click")
    def click(self):
        """Click an element"""
        el = self.find_element()
        el.click()

    @allure_step("Wait for element to disappear")
    def wait_for_element_to_disappear(self,):
        """Wait for an element to disappear from the page"""
        try:
            self.wait.until_not(
                EC.presence_of_element_located(self._locator)
            )
            return True
        except Exception as e:
            allure.attach(str(e), name="Element did not disappear", attachment_type=allure.attachment_type.TEXT)
            return False