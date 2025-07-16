
from pages.base_page import BasePage
from utils.allure_decorators import allure_step


class HomePage(BasePage):
    PAGE_URL = "/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url_path = ""
