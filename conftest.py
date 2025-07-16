import pytest
from typing import Generator
from selenium.webdriver.remote.webdriver import WebDriver

from config.config import Config
from enums.devices import DEVICES
from utils.driver_manager import DriverManager


@pytest.fixture
def driver(request) -> Generator[WebDriver, None, None]:
    """
    Fixture to create and configure WebDriver instance
    """

    # Convert device option to actual device name
    device_name = DEVICES.get(Config.DEVICE)
    if not device_name:
        raise ValueError(f"Unknown device. Available devices: {list(DEVICES.keys())}")

    # Create driver instance
    driver = DriverManager.create_driver(
        browser_type=Config.BROWSER_TYPE,
        is_mobile=Config.MOBILE,
        device_name=device_name,
        is_headless=Config.HEADLESS
    )

    yield driver

    # Cleanup
    driver.quit()


@pytest.fixture
def mobile_driver(driver) -> WebDriver:
    """
    Fixture that ensures the driver is configured for mobile testing
    """
    if not driver.execute_script("return window.navigator.userAgent").lower().__contains__("mobile"):
        pytest.skip("This test requires mobile emulation mode. Use --mobile flag")
    return driver