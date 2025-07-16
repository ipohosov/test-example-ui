from selenium.webdriver.common.by import By

from elements.mobile.button import Button
from pages.base_page import BasePage
from utils.allure_decorators import allure_step


class StreamerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.close_btn = Button(self.driver, (By.CSS_SELECTOR, ".modal-close-button"))

    @allure_step("Handle modal if present")
    def close_modal_if_present(self):
        """
        Check for and close a modal if it appears within the specified timeout.
        """
        try:
            # Wait for modal close button with shorter timeout

            if  self.close_btn:
                self.close_btn.click()
                # Wait for modal to disappear
                self.close_btn.wait_for_element_to_disappear()
        except Exception:
            # If no modal appears, just continue
            pass
