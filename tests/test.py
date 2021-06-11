import allure
from src.Elements import Elements
from src.User import User
import pytest

right = User("335026", "1234", "1234")
wrong_login = User("ff", "1234", "1234")
wrong_password = User("testuser25", "2222", "1234")
wrong_sms = User("testuser24", "1234", "2222")


class TestAuth(object):
    pass

    @pytest.mark.test_positive
    @allure.suite('Регресс')
    @allure.epic('Регресс --> авторизации')
    @allure.feature('Вход в ДБО')
    @allure.story('Ввод верного логина и пароля')
    @allure.title('Тест 1 - Положительный сценарий авторизации в ДБО (ввод правильного логина, пароля, смс)')
    @allure.issue('http://testlink.org', name='здесь мог бы быть номер тест-кейса')
    @allure.description('Тестируем вход с верным логином и смс')
    def test_log(self):
        Elements().open().input_login(right).input_password(right).press_button()
        Elements().check_title('Делобанк - Подтверждение входа')
        Elements().insert_sms(right).check_title('Делобанк')
        Elements().logout_manual1()


    @pytest.mark.test_negative
    @allure.suite('Регресс')
    @allure.epic('Регресс --> авторизации')
    @allure.feature('Вход в ДБО')
    @pytest.mark.parametrize("user", [wrong_login, wrong_password])
    @allure.story('Ввод неверного логина или пароля')
    @allure.title(f'Тест 2 - Негативный сценарий авторизации в ДБО (ввод не верного правильного логина или пароля)')
    @allure.description('Тестируем вход с верным логином и смс')
    @allure.issue('http://testlink.org', name='здесь мог бы быть номер тест-кейса')
    def test_log2(self, user):
        Elements().open().input_login(user).input_password(user).press_button().check_error('Указан неверный логин или пароль')


    @pytest.mark.test_negative
    @allure.suite('Регресс')
    @allure.epic('Регресс --> авторизации')
    @allure.feature('Вход в ДБО')
    @allure.story('Ввод неверной смс')
    @allure.title(f'Тест 3 - Негативный сценарий авторизации в ДБО (ввод не верного смс)')
    @allure.description('Тестируем вход с неверной смс')
    @allure.issue('http://testlink.org', name='здесь мог бы быть номер тест-кейса')
    @allure.severity('trivial')
    def test_log3(self):
        Elements().open().input_login(wrong_sms).input_password(wrong_sms).press_button().insert_sms(wrong_sms)
        Elements().check_error('Введен неправильный одноразовый код')
        Elements().logout_manual2()


    @pytest.mark.broken
    @allure.suite('Регресс')
    @allure.epic('Регресс --> авторизации')
    @allure.feature('Вход в ДБО')
    @allure.story('Сломаный тест')
    @allure.title(f'Тест 4 - Сломаный тест')
    @allure.severity('trivial')
    @allure.description('Тестируем вход Сломаный тест')
    @allure.issue('http://testlink.org', name='здесь мог бы быть номер тест-кейса')
    def test_log4(self):
        Elements().open().input_login(right).input_password(right).press_button().check_tite()


