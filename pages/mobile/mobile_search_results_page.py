from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.mobile.mobile_streamer_page import StreamerPage
from utils.allure_decorators import allure_step


class SearchResultsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.streamer_loc = (By.CSS_SELECTOR, "article a[href*='/'][href$='/home']")

    @allure_step("Select first visible streamer")
    def select_visible__streamer(self):
        """
        Selects the streamer that is currently visible in the viewport
        Raises:
            TimeoutException: If no visible streamer is found
        """
        # Get all streamer elements
        streamers = self.driver.find_elements(*self.streamer_loc)

        # Find the first visible streamer
        visible_streamer = None
        for streamer_el in streamers:
            if self.is_element_visible(streamer_el):
                visible_streamer = streamer_el
                break

        if visible_streamer is None:
            raise NoSuchElementException("No visible streamers found on screen")

        # Click the first visible streamer
        visible_streamer.click()
        return StreamerPage(self.driver)
