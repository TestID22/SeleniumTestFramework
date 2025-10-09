import pytest
from framework.browser_manager import BrowserManager


@pytest.fixture(scope="session")
def driver():
    """Session-wide browser fixture."""
    driver = BrowserManager.get_driver(browser_name="chrome", headless=False)
    yield driver
    BrowserManager.quit_driver()
