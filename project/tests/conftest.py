import json

import pytest

from framework.api.APIclient import APIClient
from framework.browser.browser_manager import BrowserManager

@pytest.fixture()
def config():
    with open("project/configuration/test_env.json") as f:
        return json.load(f)


@pytest.fixture()
def driver(config):
    driver = BrowserManager.get_driver(browser_name="chrome", headless=False)
    test_url = config.get("test_environment_url")
    BrowserManager.set_test_environment(test_url)
    yield driver
    BrowserManager.close_driver()


@pytest.fixture()
def api():
    api_client = APIClient()
    api_client.authorize()
    return api_client