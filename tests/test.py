import allure
from selene.config import base_url
from selene.support.shared.jquery_style import s
from src.Elements import Elements
from src.User import User
import pytest


class Work(object):

    def __init__(self):
        self.login = s('.input__box>[placeholder="Логин"]')
        self.password = s('input[placeholder="Пароль"]')
        self.submint_bottons = s('.button__title')
        self.confirm = s('[data-confirm="true"]')


right = User("335026", "1234", "1234")
wrong1 = User("ff", "1234", "1234")
wrong2 = User("testuser25", "2222", "1234")
wrong3 = User("testuser24", "1234", "2222")

@allure.suite('Регресс')
@allure.epic('Регресс --> авторизации')
@allure.feature('Вход в ДБО')
@allure.story('Ввод верного логина и пароля')
@allure.title('Тест 1 - Положительный сценарий авторизации в ДБО (ввод правильного логина, пароля, смс)')
@allure.issue('http://testlink.org', name='здесь мог бы быть номер тест-кейса')
@allure.description('Тестируем вход с верным логином и смс')
def test_log():
    Elements().open().input_login(right).input_password(right).press_button().check_title('Делобанк - Подтверждение входа')
    Elements().insert_sms(right).check_title('Делобанк')
    Elements().logout_manual2()
    #Elements().clear_cookie()


@allure.suite('Регресс')
@allure.epic('Регресс --> авторизации')
@allure.feature('Вход в ДБО')
@pytest.mark.parametrize("user", [wrong1, wrong2])
@allure.story('Ввод неверного логина или пароля')
@allure.title(f'Тест 2 - Негативный сценарий авторизации в ДБО (ввод не верного правильного логина или пароля)')
@allure.description('Тестируем вход с верным логином и смс')
@allure.issue('http://testlink.org', name='здесь мог бы быть номер тест-кейса')

def test_log2(user):
    Elements().open().input_login(user).input_password(user).press_button().check_error('Указан неверный логин или пароль')


@allure.suite('Регресс')
@allure.epic('Регресс --> авторизации')
@allure.feature('Вход в ДБО')
@allure.story('Ввод неверной смс')
@allure.title(f'Тест 3 - Негативный сценарий авторизации в ДБО (ввод не верного смс)')
@allure.description('Тестируем вход с неверной смс')
@allure.issue('http://testlink.org', name='здесь мог бы быть номер тест-кейса')
@allure.severity('trivial')
def test_log3():
    Elements().open().input_login(wrong3).input_password(wrong3).press_button().insert_sms(wrong3)
    Elements().check_error('Введен неправильный одноразовый код')



@allure.suite('Регресс')
@allure.epic('Регресс --> авторизации')
@allure.feature('Вход в ДБО')
@allure.story('Сломаный тест')
@allure.title(f'Тест 4 - Сломаный тест')
@allure.severity('trivial')
@allure.description('Тестируем вход Сломаный тест')
@allure.issue('http://testlink.org', name='здесь мог бы быть номер тест-кейса')
def test_log4():
    Elements().open().input_login(right).input_password(right).press_button().check_tite()

