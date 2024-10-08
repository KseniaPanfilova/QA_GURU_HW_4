import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def window():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'

    yield

    browser.quit()
