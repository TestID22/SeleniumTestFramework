from selenium.webdriver.remote.webdriver import WebDriver

from framework.browser.browser_factory import BrowserFactory


class BrowserManager:
    _driver = None

    @classmethod
    def get_driver(cls, browser_name='chrome', headless=False) -> WebDriver:
        """
        we use @classmethod because we want to call the same driver shared across all tests.
        We want a single browser (singleton) shared across all tests.
        _driver belongs to the class, not any specific instance.
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

    @classmethod
    def set_test_environment(cls, url):
        cls._driver.get(url)