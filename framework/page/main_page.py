from selenium.webdriver.common.by import By

from framework.browser.browser_manager import BrowserManager
from framework.page.base_page import BasePage


class MainPage(BasePage):

    def __init__(self):
        super().__init__(page_name="Main", locator="TBD")

    @property
    def driver(self):
        return BrowserManager.get_driver(self)

    @property
    def elements(self):
        return MainPageElements

    @property
    def click(self):
        return MainPageClick(self.driver)

class MainPageElements:

    iframe_box = (By.XPATH, "//img[@src='/img/iframe.png']")

class MainPageClick:
    def __init__(self, driver):
        self.driver = driver

    def click_iframe_box(self):
        self.driver.find_element(*MainPageElements.iframe_box).click()
