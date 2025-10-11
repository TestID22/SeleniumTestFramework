from abc import ABC, abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from framework.browser.browser_manager import BrowserManager

class BasePage(ABC):
    def __init__(self, locator, page_name, by: By = By.XPATH):
        self._locator = locator
        self._page_name = page_name
        self._by = by
        self._wait = WebDriverWait(self.driver, 10, poll_frequency=1)

    @property
    def driver(self):
        return BrowserManager().get_driver()

    @abstractmethod
    def is_opened(self):
        pass

    def execute_script(self, script: str):
        return self.driver.execute_script(script, self.find_element())

    def screenshot(self, path):
        self.find_element().screenshot(path)


    def refresh_page(self):
        self.driver.refresh()