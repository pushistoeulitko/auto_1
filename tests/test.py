import allure
import pytest
from future.backports.datetime import time
from selene import browser
from selene.conditions import text
from selene.support.conditions import have
from selene.support.jquery_style_selectors import s
from Elements import Elements
from MainPage import MainPage
from User import User
from subprocess import call
import pytest
from selene import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Work(object):

    def __init__(self):
        self.login = s('.input__box>[placeholder="Логин"]')
        self.password = s('input[placeholder="Пароль"]')
        self.submint_bottons = s('.button__title')
        self.confirm = s('[data-confirm="true"]')

    # def login_login(self, user):
    #     self.login.send_keys(user.name)
    #     self.password.send_keys(user.passw)
    #     self.submint_bottons.click()
    #     return self
    #
    # def at_main_page(self):
    #     return MainPage


right = User("335026", "1234", "1234")
wrong1 = User("ff", "1234", "1234")
wrong2 = User("testuser25", "2222", "1234")
wrong3 = User("testuser24", "1234", "2222")


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


@allure.epic('Регресс --> авторизации')
# with allure.step('step 1'): — с помощью этого контекстного менеджера тело теста делится на шаги, понятные в отчете.
# @pytest.mark.parametrize("user", [right, wrong1, wrong2])
@allure.feature('Вход в ДБО')
@allure.story('Ввод верного логина и пароля')
@allure.description('тестируем вход с верным логином и смс')
# что проверяется
# какие данные вводятся
def test_log():
    Elements().open().login_as(right)
    s('div.title').should(have.text('Подтверждение входа'))
    Elements().insert_sms(right).clear_cookie()
    # browser.title().should_have(text('Делобанк'))
    # time.sleep(2)


# browser.WebDriver().delete_all_cookies()
# driver.delete_all_cookies()
# should(have.title('Делобанк'))
# time.sleep(5)


@allure.epic('Регресс --> авторизации')
@allure.feature('Вход в ДБО')
@allure.story('Ввод неверного логина или пароля')
@allure.description('тестируем вход с верным логином и смс')
@pytest.mark.parametrize("user", [wrong1, wrong2])
def test_log2(user):
    Elements().open().login_as(user)
    s('div.errors').is_displayed()


@allure.epic('Регресс --> авторизации')
@allure.description('тестируем вход с неверной смс')
@allure.feature('Вход в ДБО')
@allure.story('Ввод неверной смс')
def test_log3(wrong3):
    Elements().open().login_as(wrong3).insert_sms(wrong3).check_error('Введен неправильный одноразовый код')


@allure.epic('Регресс --> авторизации')
@allure.feature('Вход в ДБО')
@allure.story('Сломаный тест')
@allure.description('тестируем вход Сломаный тест')
def test_log4(right):
    Elements().open().login_as(right).s('div.errojgjhsdjghrs').is_displayed()
