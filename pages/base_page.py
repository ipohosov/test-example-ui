import os
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config
import allure

from elements.mobile.button import Button
from utils.allure_decorators import allure_step, logger


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.DEFAULT_TIMEOUT)
        self.url_path = ""

    @allure_step("Navigate to URL")
    def go_to_url(self):
        """Navigate to the specified URL by appending it to the base URL"""
        self.driver.get(Config.BASE_URL+self.url_path)

    @allure_step("Check if element is presented on the active part of screen")
    def is_element_visible(self, element: WebElement) -> bool:
        """
        Checks if an element is currently visible in the viewport
        Args:
            element: WebElement to validate
        Returns:
            bool: True if an element is in viewport
        """
        return self.driver.execute_script("""
                 var elem = arguments[0];
                 var rect = elem.getBoundingClientRect();
                 return (
                     rect.top >= 0 &&
                     rect.left >= 0 &&
                     rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                     rect.right <= (window.innerWidth || document.documentElement.clientWidth)
                 );
             """, element)

    @allure_step("Scroll page by {scroll_amount} pixels")
    def scroll_page(self, scroll_amount=200):
        """
        Safely scroll the page by the specified amount
        Args:
            scroll_amount (int): Number of pixels to scroll vertically
        """
        try:
            script = "window.scrollTo(0, window.pageYOffset + arguments[0]);"
            self.driver.execute_script(script, scroll_amount)
        except:
            # If JavaScript scrolling fails, try an alternative method
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure_step("Get page height")
    def get_page_height(self):
        """Get the total height of the page"""
        return self.driver.execute_script("return document.documentElement.scrollHeight")

    @allure_step("Scroll through search results")
    def scroll_the_page(self, max_scrolls=3):
        """
        Scroll through the search results page to load more content
        Args:
            max_scrolls (int): Maximum number of scroll attempts
        """
        scroll_count = 0
        last_height = self.get_page_height()

        while scroll_count < max_scrolls:
            self.scroll_page(2000)
            time.sleep(1)  # Short pause to allow content to load
            new_height = self.get_page_height()
            if new_height == last_height:
                break

            last_height = new_height
            scroll_count += 1

    @allure_step("Wait that page is loaded")
    def wait_for_complete_load(self):
        """
        Wait for page to be completely loaded using multiple checks
        """
        try:
            # Method 1: Document ready state
            self.wait.until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            logger.info("✓ Document ready state: complete")

            # Method 2: Wait for body element
            self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            logger.info("✓ Body element loaded")

            # Method 3: Check for jQuery if present
            try:
                self.wait.until(
                    lambda d: d.execute_script("return typeof jQuery !== 'undefined' ? jQuery.active == 0 : true")
                )
                logger.info("✓ jQuery requests completed")
            except TimeoutException:
                logger.error("! jQuery not present or still active")

            # Method 4: Check load event
            try:
                self.wait.until(
                    lambda d: d.execute_script(
                        "return window.performance.getEntriesByType('navigation')[0].loadEventEnd > 0")
                )
                logger.info("✓ Load event completed")
            except:
                logger.error("! Load event check failed")

            logger.info("✓ Page fully loaded")
            return True

        except TimeoutException as e:
            logger.error(f"✗ Page load timeout: {e}")
            return False

    @allure_step("Take screenshot of current streamer page")
    def take_screenshot(self):
        """
        Take a screenshot  and attach it to the Allure report.
        Saves the screenshot in the allure_screenshots directory with a unique name based
        on the URL and timestamp.

        Returns:
            str: Path to the saved screenshot file, or None if screenshot capture failed
        """
        name = self.driver.current_url.split("/")[-1]

        try:
            # Create a screenshots directory if it doesn't exist
            screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                           'allure_screenshots')
            os.makedirs(screenshots_dir, exist_ok=True)

            # Generate filename with timestamp
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"{name}_{timestamp}.png"
            filepath = os.path.join(screenshots_dir, filename)

            # Take and save a screenshot
            self.driver.save_screenshot(filepath)

            # Attach to Allure report
            with open(filepath, 'rb') as screenshot:
                allure.attach(
                    screenshot.read(),
                    name=name,
                    attachment_type=allure.attachment_type.PNG
                )

            return filepath
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
            return None