import time

from framework.page.google_page import GooglePage
from framework.page.main_page import MainPage
from framework.page.tags_page import TagsPage
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


def test_tag_search(driver, config):
    """
    this is a fake test there is nothing to test
    """
    # page object
    main_page = MainPage()
    tags_page = TagsPage()
    expected_resolution = {'width': 1936, 'height': 1056}

    with TestStep("1. Open Google"):
        driver.get("https://qaplayground.dev/apps/tags-input-box/")

    with TestStep("2. Fill in search query field"):
        tags_page.is_opened()
        tags_page.set.set_tag("test")

    with TestStep("3. Check the start url"):
        tags_page.elements.tag_input_filed.push_enter()
        tags_page.refresh_page()
        assert tags_page.get_current_url() == config['tags_page'], "Start url is incorrect"

    with (TestStep("4. Check window size via staticmethod")):
        actual_window_size = GooglePage.get_window_size()
        assert ([actual_window_size['width'],actual_window_size['height']] == [expected_resolution['width'],
                                                                               expected_resolution['height']],
                                                                               "window size is incorrect")

    # todo: We need to add validation in real world example, but I won't do this.
def test_check_tags(driver, config):

    tags_page = TagsPage()
    expected_tags = ['node', 'javascript']
    with TestStep("1. Open TagsPage"):
        driver.get(config['tags_page'])

    with TestStep("2. Fill in search query field"):
        tags_page.is_opened()
        tags_page.set.set_tag("test")
        actual_tags_list = tags_page.get.get_tags_text()

    with TestStep("3. Verify page URL contains 'tags'"):
        assert expected_tags == actual_tags_list, "Lists are not equal/same"


def test_api_authentication(api):
    expected_product = {'id': 1, 'title': 'Essence Mascara Lash Princess'}

    with TestStep("1. Check if 'Essence Mascara Lash Princess' is in 'products list'"):
        response = api.products.get_products()
        if response.status_code != 200:
            raise AssertionError

    with TestStep("2: Check the first product in 'products list'"):
        product = response.json()['products'][0]
        assert product['id'] == expected_product['id'], "Product is not in 'products list'"

