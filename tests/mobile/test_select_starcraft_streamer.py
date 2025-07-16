import allure

from elements.mobile.navigation_panel import NavigationPanel
from pages.mobile.mobile_home_page import HomePage


@allure.feature("Twitch Search")
@allure.story("Search streamers by category")
class TestMobileTwitchSearch:

    @allure.title("Test searching by category(StarCraft II) and select random streamer")
    def test_select_starcraft_streamer(self, driver):
        search_query = "StarCraft II"
        home_page = HomePage(driver)
        navigation = NavigationPanel(driver)

        home_page.go_to_url()
        browse_page = navigation.go_to_browse_page()
        search_results_page = browse_page.search(search_query)
        search_results_page.scroll_the_page(2)
        streamer_page = search_results_page.select_visible__streamer()
        streamer_page.close_modal_if_present()

        # Assertion
        assert streamer_page.wait_for_complete_load(), "Page did not load completely"

        streamer_page.take_screenshot()
