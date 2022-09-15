import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def window_expect_size():
    browser.open('https://demoqa.com/webtables')
    browser.config.window_width = 1260
    browser.config.window_height = 1000
    browser.config.hold_browser_open = True
    yield

