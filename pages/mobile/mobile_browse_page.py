from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from elements.mobile.search import Search
from pages.base_page import BasePage
from pages.mobile.mobile_search_results_page import SearchResultsPage
from utils.allure_decorators import allure_step


class BrowsePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.search_el = Search(driver)

    def search(self, search_query):
        """
        Make a search and select the result
        """
        self.search_el.search(search_query)
        return SearchResultsPage(self.driver)
