from subprocess import call
import pytest
from selene import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='module')
def setup_module():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    browser.set_driver(driver)
    # yield driver
    # browser.quit()

@pytest.fixture(scope='module')
def teardown_module():
    # def generate_report():
    #     call(["./tests/reports/allure", "generate", "report"], cwd="../")  # generate_report()
    # generate_report()
    browser.quit()


# @pytest.fixture(scope='module')
# def setup():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     browser.set_driver(driver)
#     yield driver
#     browser.quit()