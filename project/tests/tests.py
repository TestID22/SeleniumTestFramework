import time

from framework.page.main_page import MainPage
from framework.utils.test_step import TestStep as test_step


def test_main_page_title(driver):
    with test_step("1. Check that the title is correct"):
        assert driver.title == "Playground for the QA automation engineers"


def test_iframe_box_is_exist(driver):
    # page object
    main_page = MainPage()

    with test_step("1. Click iframe box"):
        main_page.click.click_iframe_box()

    with test_step("2. Verify page URL contains 'iframe'"):
        assert "iframe" in driver.current_url
