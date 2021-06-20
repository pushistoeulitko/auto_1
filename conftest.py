import allure
import pytest
from selene.support.shared import browser


def pytest_exception_interact(node, call, report):
    if pytest.fail:
        allure.attach(
            body=browser.driver.get_screenshot_as_png(),
            name='Screenshot',
            attachment_type=allure.attachment_type.PNG,
            extension='png'
        )
