from framework.element.element import Element
from framework.page.base_page import BasePage

from framework.page.page_category import PageCategory


class TagsPageElements:

    tag_window = Element(locator="//div[contains(@class, 'light-theme wrapper')]", element_name="tag_window")
    tag_input_filed = Element(locator="//input[@type='text']", element_name="tag input field")
    tags_list = Element(locator="//div[@class='content']//ul/li", element_name="tag list")

class TagsPage(BasePage):


    def __init__(self):
        super().__init__(*self.elements.tag_window.as_tuple())


    @property
    def elements(self):
        return TagsPageElements

    @property
    def get(self):
        return TagsPageGetters(self)

    @property
    def set(self):
        return TagsPageSetters(self)


class TagsPageSetters(PageCategory):

    def set_tag(self, key):
        self.page.elements.tag_input_filed.send_keys(key)


class TagsPageGetters(PageCategory):

    def get_tags_text(self):
        return [element.text for element in self.page.elements.tags_list.get_elements()]
