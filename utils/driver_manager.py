from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from typing import Optional, Dict, Any


class DriverManager:
    @staticmethod
    def get_chrome_options(is_mobile: bool = False, device_name: Optional[str] = None,
                           is_headless: bool = False) -> webdriver.ChromeOptions:
        """
        Configure Chrome options for WebDriver

        Args:
            is_mobile: Whether to enable mobile emulation
            device_name: Mobile device to emulate (e.g. 'iPhone 12 Pro')
            is_headless: Whether to run Chrome in headless mode
        """
        chrome_options = webdriver.ChromeOptions()

        # Basic Chrome options
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        if is_headless:
            chrome_options.add_argument('--headless')

        if not is_mobile:
            chrome_options.add_argument('--window-size=1920,1080')

        # Configure mobile emulation if requested
        if is_mobile:
            if device_name:
                mobile_emulation = {
                    "deviceName": device_name
                }
            else:
                # Default mobile configuration if no device specified
                mobile_emulation = {
                    "deviceMetrics": {
                        "width": 390,
                        "height": 844,
                        "pixelRatio": 3.0
                    },
                    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 Pro like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/604.1"
                }
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        return chrome_options

    @staticmethod
    def create_driver(browser_type: str = "chrome",
                      is_mobile: bool = False,
                      device_name: Optional[str] = None,
                      is_headless: bool = False,
                      implicit_wait: int = 10) -> webdriver.Remote:
        """
        Create and configure WebDriver instance

        Args:
            browser_type: Type of browser ('chrome' supported for now)
            is_mobile: Whether to enable mobile emulation
            device_name: Mobile device to emulate
            is_headless: Whether to run in headless mode
            implicit_wait: Implicit wait timeout in seconds
        """
        if browser_type.lower() == "chrome":
            chrome_options = DriverManager.get_chrome_options(
                is_mobile=is_mobile,
                device_name=device_name,
                is_headless=is_headless
            )

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.implicitly_wait(implicit_wait)

            return driver
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")
