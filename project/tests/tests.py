import time

from framework.page.main_page import MainPage


def test_main_page_title(driver):
    assert driver.title == "Playground for the QA automation engineers"


def test_iframe_box_is_exist(driver):
    # page object
    main_page = MainPage()

    main_page.click.click_iframe_box()
