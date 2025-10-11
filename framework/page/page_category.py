

class PageCategory:
    """
    Very important to be able to call all GooglePage properties we have created Category Class with page field
    *set property has page and it is an object of GooglePage class, so we have possibility to call all googlepage methods
    via page field.
    """
    def __init__(self, page):
        self.page = page
