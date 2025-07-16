from selenium.webdriver.common.by import By

from elements.base_element import BaseElement
from elements.mobile.dummy_element import DummyElement
from utils.allure_decorators import allure_step


class Search(BaseElement):
    def __init__(self, driver):
        super().__init__(driver, (By.CSS_SELECTOR, "input[type='search'][data-a-target='tw-input']"))

    @allure_step("Enter search query: {query}")
    def search(self, query: str):
        """Enter text into the search field and select the result from list"""
        search_input = DummyElement(self.driver, self._locator).find_element()
        search_input.clear()
        search_input.send_keys(query)

        # Remove overlay layer if it's presented
        DummyElement(self.driver, (By.CSS_SELECTOR, 'div.tw-modal-layer')).remove_element_from_dom()

        results_link = f"a[href='/directory/category/{query.lower().replace(" ", "-")}']"
        result_el = DummyElement(self.driver, (By.CSS_SELECTOR, results_link))
        result_el.click()
