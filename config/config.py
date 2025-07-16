from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


class Config:
    # Selenium configuration
    BROWSER_TYPE = os.getenv('BROWSER_TYPE', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
    MOBILE = os.getenv('MOBILE', 'false').lower() == 'true'
    DEVICE = os.getenv('DEVICE', 'Pixel_4')
    DEFAULT_TIMEOUT = 10
    IMPLICIT_WAIT = 5

    # URLs
    BASE_URL = os.getenv('BASE_URL', 'https://www.twitch.tv')
