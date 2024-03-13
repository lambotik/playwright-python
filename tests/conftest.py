import os

import allure
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture()
def browser():
    with sync_playwright() as browser:
        if 'CI' in os.environ:
            browser = browser.chromium.launch(headless=True, slow_mo=10)
            browser = browser.new_page()
        else:
            browser = browser.chromium.launch(headless=False, slow_mo=10)
            browser = browser.new_page()
            browser.set_viewport_size(({r"width": 1900, "height": 1020}))
        yield browser
        allure.attach(browser.screenshot(type='png'))
        browser.close()
