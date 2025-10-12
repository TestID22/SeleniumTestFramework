from abc import ABC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

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

    def is_opened(self):
        try:
            self._wait.until(EC.presence_of_element_located((self._by, self._locator)))
        except TimeoutException as e:
            print(f"Timed out {e}")
            return False
        return True

    def execute_script(self, script: str):
        return self.driver.execute_script(script, self.find_element())

    def screenshot(self, path):
        self.driver.save_screenshot(path)

    def refresh_page(self):
        self.driver.refresh()

    def get_current_url(self):
        return self.driver.current_url

    @staticmethod
    def get_window_size():
        return BrowserManager.get_driver().get_window_size()
