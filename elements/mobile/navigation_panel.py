
from selenium.webdriver.common.by import By

from elements.mobile.button import Button
from pages.mobile.mobile_browse_page import BrowsePage
from pages.mobile.mobile_home_page import HomePage


class NavigationPanel:

    def __init__(self, driver):
        self.driver = driver
        self.home_button = Button(driver, (By.XPATH, "//div[text()='Home']"))
        self.browse_button = Button(driver, (By.XPATH, "//div[text()='Browse']"))
        self.activity_button = Button(driver, (By.XPATH, "//div[text()='Activity']"))
        self.profile_button = Button(driver, (By.XPATH, "//div[text()='Profile']"))

    def go_to_home_page(self):
        """Click the home navigation button"""
        self.home_button.click()
        return HomePage(self.driver)

    def go_to_browse_page(self):
        """Click the browse navigation button"""
        self.browse_button.click()
        return BrowsePage(self.driver)
