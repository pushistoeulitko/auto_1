import allure
from src.LoginChecks import LoginChecks
from src.LoginSteps import right
import pytest
from src.User import wrong_login, wrong_password, wrong_sms


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
            .check_input_login(right).check_input_password(right).check_press_button()\
            .check_title('Делобанк - Подтверждение входа').check_insert_sms(right)\
            .check_title('Делобанк')
        LoginChecks().check_logout_manual_quit()


    @pytest.mark.test_negative
    @pytest.mark.parametrize("user", [wrong_login, wrong_password])
    @allure.story('Ввод неверного логина или пароля')
    @allure.title(f'Тест 2 - Негативный сценарий авторизации в ДБО (ввод не верного правильного логина или пароля)')
    @allure.description('Тестируем вход с верным логином и смс')
    @allure.issue('http://testlink.org', name='здесь мог бы быть номер тест-кейса')
    def test_log_wrong_login_or_password(self, user):
        LoginChecks().open_login_page()\
            .check_input_login(user).check_input_password(user).check_press_button()\
            .check_error('Указан неверный логин или пароль')

    @pytest.mark.test_negative
    @allure.story('Ввод неверной смс')
    @allure.title(f'Тест 3 - Негативный сценарий авторизации в ДБО (ввод не верного смс)')
    @allure.description('Тестируем вход с неверной смс')
    @allure.issue('http://testlink.org', name='здесь мог бы быть номер тест-кейса')
    @allure.severity('trivial')
    def test_log_wrong_sms(self):
        LoginChecks().open_login_page()\
            .check_input_login(wrong_sms).check_input_password(wrong_sms).check_press_button().check_insert_sms(wrong_sms)
        LoginChecks().check_error('Введен неправильный одноразовый код')
        LoginChecks().logout_manual_change_user()

    @pytest.mark.broken
    @allure.story('Сломаный тест')
    @allure.title(f'Тест 4 - Сломаный тест')
    @allure.severity('trivial')
    @allure.description('Тестируем вход Сломаный тест')
    @allure.issue('http://testlink.org', name='здесь мог бы быть номер тест-кейса')
    def test_log_broken(self):
        LoginChecks().open_login_page() \
            .check_input_login(right).check_input_password(right).check_press_button() \
            .check_tile('Делобанк - Подтверждение входа')

