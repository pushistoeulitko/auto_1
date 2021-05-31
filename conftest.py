from subprocess import call
import allure
import pytest
from selene.support.shared import browser
url="https://delo-prod.skblab.ru/login"
import config

@allure.step('Инициализируем драйвер')
def step_driver(browser):
    pass

@pytest.fixture(scope='module', autouse=True)
def setup_module():
    browser.config.base_url = url
    browser.config.start_maximized = True
#     step_driver('chrome')
#     browser.config.browser_name = 'chrome'
#     browser.config.timeout = 4
#     # browser.config.window_width = 1920
#     # browser.config.window_height = 1080
#     # browser.config.window_height = 750
#     # browser.config.window_width = 1150
#     browser.config.start_maximized = True
    # yield driver
    # browser.quit()


@allure.step('Закрываем драйвер')
def step_quit(quit):
    pass

@pytest.fixture(scope='module')
def teardown_module():
    def generate_report():
        call(["../reports/allure", "generate", "report"], cwd="../")
    generate_report()
    browser.quit()


# @pytest.fixture(scope='module')
# def setup():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     browser.set_driver(driver)
#     yield driver
#     browser.quit()


# @pytest.fixture(scope="function")
# def before(request):
#     print('\nbefore()')
#
#     def after():
#         Elements().clear_cookie()
#         browser.quit()
#     request.addfinalizer(after)

    # def after():
    #     browser.quit()
    # # def generate_report():
    #     call(["./tests/reports/allure", "generate", "report"], cwd="../")  # generate_report()
    # generate_report()