import allure
from framework.logger import AllureLogger

from framework.browser.browser_manager import BrowserManager

logger = AllureLogger.get_test_logger(__name__)

class TestStep:
    def __init__(self, test_step_desctiption: str):
        self.test_step_desctiption = test_step_desctiption

    def __enter__(self):
        allure.dynamic.description(f"Step: {self.test_step_desctiption}")
        logger.info(f"START: {self.test_step_desctiption}")
        allure.step(self.test_step_desctiption)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logger.error(f"FAILED: {self.test_step_desctiption} — {exc_val}")
            BrowserManager.get_driver().save_screenshot(f"screens/{self.test_step_desctiption}.png")
        else:
            logger.info(f"PASSED: {self.test_step_desctiption}")
        logger.info(f"END: {self.test_step_desctiption}")
        return False
