from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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

    def is_opened(self):
        try:
            self.wait.until(EC.presence_of_element_located((self.by, self.elements.iframe_box._locator)))
        except TimeoutException:
            print("Timed out")
            return False
        return True


class MainPageElements:

    iframe_box = (By.XPATH, "//img[@src='/img/iframe.png']")

class MainPageClick:
    def __init__(self, driver):
        self.driver = driver

    def click_iframe_box(self):
        self.driver.find_element(*MainPageElements.iframe_box).click()
