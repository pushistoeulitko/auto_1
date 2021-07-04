import allure
from src.LoginChecks import LoginChecks
import pytest

from src.Text import Text
from src.User import User

right = User("335026")
wrong_login = User("ff")
wrong_password = User("testuser25", "2222", "1234")
wrong_sms = User("testuser24", "1234", "2222")

@allure.suite('Регресс')
@allure.epic('Регресс --> авторизации')
@allure.feature('Вход в ДБО')
class TestAuth:

    @pytest.mark.test_positive
    @allure.story('Ввод верного логина и пароля')
    @allure.title('Тест 1 - Положительный сценарий авторизации в ДБО (ввод правильного логина, пароля, смс)')
    @allure.issue('http://testlink.org', name='здесь мог бы быть номер тест-кейса')
    @allure.description('Тестируем вход с верным логином и смс')
    def test_log_right_authorization(self):
        LoginChecks().open_login_page()\
            .auth_login_and_password(right).check_press_button()\
            .check_title(Text.DBO_enter_confirn).check_insert_sms(right)\
            .check_title(Text.Bank)
        LoginChecks().check_logout_manual_quit()


    @pytest.mark.test_negative
    @pytest.mark.parametrize("user", [wrong_login, wrong_password])
    @allure.story('Ввод неверного логина или пароля')
    @allure.title(f'Тест 2 - Негативный сценарий авторизации в ДБО (ввод не верного правильного логина или пароля)')
    @allure.description('Тестируем вход с верным логином и смс')
    @allure.issue('http://testlink.org', name='здесь мог бы быть номер тест-кейса')
    def test_log_wrong_login_or_password(self, user):
        LoginChecks().open_login_page()\
            .auth_login_and_password(user).check_press_button()\
            .check_error(Text.Error_login_or_password)

    @pytest.mark.test_negative
    @allure.story('Ввод неверной смс')
    @allure.title(f'Тест 3 - Негативный сценарий авторизации в ДБО (ввод не верного смс)')
    @allure.description('Тестируем вход с неверной смс')
    @allure.issue('http://testlink.org', name='здесь мог бы быть номер тест-кейса')
    @allure.severity('trivial')
    def test_log_wrong_sms(self):
        LoginChecks().open_login_page()\
            .auth_login_and_password(wrong_sms).check_press_button().check_insert_sms(wrong_sms)
        LoginChecks().check_error(Text.Error_sms)
        LoginChecks().logout_manual_change_user()

    @pytest.mark.broken
    @allure.story('Сломаный тест')
    @allure.title(f'Тест 4 - Сломаный тест')
    @allure.severity('trivial')
    @allure.description('Тестируем вход Сломаный тест')
    @allure.issue('http://testlink.org', name='здесь мог бы быть номер тест-кейса')
    def test_log_broken(self):
        LoginChecks().open_login_page() \
            .auth_login_and_password(right).check_press_button() \
            .check_tile(Text.DBO_enter_confirn)

