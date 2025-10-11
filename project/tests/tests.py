import time

from framework.page.google_page import GooglePage
from framework.page.main_page import MainPage
from framework.utils.test_step import TestStep


def test_main_page_title(driver):
    with TestStep("1. Check that the title is correct"):
        assert driver.title == "Playground for the QA automation engineers"


def test_iframe_box_is_exist(driver):
    # page object
    main_page = MainPage()

    with TestStep("1. Click iframe box"):
        main_page.click.click_iframe_box()

    with TestStep("2. Verify page URL contains 'iframe'"):
        assert "iframe" in driver.current_url


def test_search(driver):
    # page object
    google_page = GooglePage()
    with TestStep("1. Open Google"):
        driver.get("https://www.google.com")

    with TestStep("2. Fill in search query field"):
        google_page.is_opened()
        google_page.set.set_search("tets")

    with TestStep("3. Click submit button"):
        google_page.click.push_enter()
        google_page.refresh_page()

    # todo: We need to add validation in real world example, but I won't do this.