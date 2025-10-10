from abc import ABC, abstractmethod


class BasePage(ABC):
    def __init__(self, locator, page_name, search_condition='xpath'):
        self._locator = locator
        self._page_name = page_name

    @property
    @abstractmethod
    def driver(self):
        pass

