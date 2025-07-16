from selenium.common import NoSuchElementException

from elements.base_element import BaseElement
from utils.allure_decorators import logger


class DummyElement(BaseElement):
    # This type of element is used to create an instance of part of complicated element

    def remove_element_from_dom(self):
        """
        Remove an element from the DOM if it exists
        """
        try:
            element = self.find_element()

            # Use JavaScript to remove the element from DOM
            self.driver.execute_script("arguments[0].remove();", element)

        except NoSuchElementException:
            logger.warning(f"Element with {self._locator[0]}='{self._locator[1]}' not found in DOM")
