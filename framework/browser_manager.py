from selenium.webdriver.chrome.webdriver import WebDriver

from framework.browser_factory import BrowserFactory


class BrowserManager:
    _driver = None

    @classmethod
    def get_driver(cls, browser_name, headless=False) -> WebDriver:
        """
        we use @classmethod because we want to call the same driver thgrou all drivers.
        :return:
        """
        if cls._driver is None:
            cls._driver = BrowserFactory.get_browser(browser_name, headless=headless)
        return cls._driver

    @classmethod
    def close_driver(cls):
        if cls._driver:
            cls._driver.close()
            cls._driver = None
