from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from framework.browser.browser_manager import BrowserManager


class Element:
    def __init__(self, locator, element_name, by: By = By.XPATH):
        self._locator = locator
        self._element_name = element_name
        self._by = by
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)

    @property
    def driver(self):
        return BrowserManager.get_driver()

    def locator(self):
        return self._locator

    def as_tuple(self):
        return self._locator, self._element_name, self._by

    def is_exist(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))

    def find_element(self):
        return self.driver.find_element(self.by, self._locator)

    def click(self):
        self.wait.until(EC.presence_of_element_located((self._by, self._locator)))
        element = self.driver.find_element(self._by, self._locator)
        element.click()

    def send_keys(self, key):
        element = self.wait.until(EC.presence_of_element_located((self._by, self._locator)))
        element.send_keys(key)

    def push_enter(self):
        self.send_keys(Keys.ENTER)

    def wait_for_visible(self, attempts: int = 3):
        self.wait.until(EC.visibility_of_element_located((self._by, self._locator)))

