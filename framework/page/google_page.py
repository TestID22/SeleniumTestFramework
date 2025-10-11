from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from framework.page.base_page import BasePage
from framework.element.element import Element



class PageCategory:
    """
    Very important to be able to call all GooglePage properties we have created Category Class with page field
    *set property has page and it is an object of GooglePage class, so we have possibility to call all googlepage methods
    via page field.
    """
    def __init__(self, page):
        self.page = page


class GooglePageElement:

    search_field = Element(locator="//textarea[@name='q']", element_name="search_field")
    submit_button = Element(locator="(//input[@type='submit' and @name='btnK'])[2]", element_name="click_button")

class GooglePage(BasePage):

    def __init__(self):
        super().__init__(page_name='GoogleMainPage', locator="TDB")

    @property
    def elements(self):
        return GooglePageElement

    @property
    def set(self):
        return GooglePageSets(self)

    @property
    def click(self):
        return GooglePageClick(self)

    def is_opened(self):
        print(f"Waiting till {self._page_name} is opened")
        return self._wait.until(EC.presence_of_element_located((self._by, self.elements.search_field._locator)))


class GooglePageSets(PageCategory):

    def set_search(self, search_query):
        self.page.elements.search_field.send_keys(search_query)


class GooglePageClick(PageCategory):

    def click_submit_button(self):
        self.page.elements.submit_button.click()

    def push_enter(self):
        self.page.elements.submit_button.send_keys(Keys.ENTER)
