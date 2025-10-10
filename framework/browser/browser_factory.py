from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


class BrowserFactory:
    """
    Responses only for creating WebDriver instances.
    """
    @staticmethod
    def get_browser(self, browser_name='chrome', headless=True) -> WebDriver:
        browser_name = browser_name.lower()

        if browser_name == 'chrome':
            options = ChromeOptions()
            if headless:
                options.add_argument('--headless')

            options.add_argument("--start-maximized")
            service = ChromeService(ChromeDriverManager().install())
        else:
            raise ValueError("Browser name must be 'chrome'")

        return webdriver.Chrome(service=service, options=options)

