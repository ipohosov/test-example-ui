# Selenium Framework with Allure Reports

A comprehensive Selenium test automation framework with Allure reporting and decorator-based step management.

## Features

- **Selenium WebDriver** with automatic driver management
- **Allure Reports** with detailed test reporting
- **Decorator-based Steps** for easy test step management
- **Page Object Model** for maintainable test code
- **Configuration Management** with environment variables
- **Screenshot on Failure** for debugging
- **Parallel Test Execution** support
- **Centralized Logging** with file and console output

## Project Structure

```
selenium-framework/
├── config/
│   └── config.py             # Configuration management
├── elements/
│   ├── base_element.py       # Functions for all type of elements
│   ├── search.py             # Custom element with specific logic
|   └── ...                   # other elements
├── pages/
│   ├── base_page.py          # Base functions for all pages
|   ├── mobile_browse_page.py # Browse page with elements of this page
|   └── ...                   # other pages
├── tests/
│   └── test_select_starcraft_streamer.py # Example test cases
├── utils/
│   ├── allure_decorators.py  # Allure step decorators
│   └── driver_manager.py     # WebDriver management
├── conftest.py               # Pytest configuration
├── pytest.ini               # Pytest settings
├── requirements.txt          # Dependencies
└── README.md                 # This file
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install Allure (optional, for report generation):
```bash
# On macOS
brew install allure

# On Linux
sudo apt-get install allure

# On Windows
scoop install allure
```

3. Copy environment file:
```bash
cp .env.example .env
```

## Usage

4. Run the Tests 
Make sure your virtual environment is activated before running any tests.
Run all tests:
``` 
pytest tests/
```
Run with Allure reporting:
``` 
pytest --alluredir=reports/allure-results
```
Generate and view Allure report:
``` 
allure serve ./reports/allure-results
```

## Test Recording Example
Below is a demonstration of a test execution:
![execution.gif](execution.gif)


### Creating Page Objects

```python
from base.base_page import BasePage
from utils.decorators import allure_step

class MyPage(BasePage):
    
    @allure_step("Perform action on page")
    def perform_action(self):
        # Your page logic here
        pass
```

## Available Decorators

- `@allure_step(title, description)`: Mark function as Allure step
