import allure
from allure_commons.types import AttachmentType
from selene import have
from selene.support.shared import browser
from src.LoginPage import LoginPage
from src.LoginSteps import LoginSteps

base_url = "https://delo-prod.skblab.ru/login"


class LoginChecks:

    def open_login_page(self):
        LoginSteps().open().title_page_login_password()
        return self

    @allure.step('Проверка заголовка')
    def check_title(self, title_text):
        LoginSteps().check_title(title_text)
        return self

    def check_input_login(self, user):
        LoginSteps().input_login(user.name)
        return self

    def check_input_password(self, user):
        LoginSteps().input_password(user.passw)
        return self

    @allure.step('Нажимаем кнопку войти')
    def check_press_button(self):
        LoginSteps().press_button()
        return self

    def check_insert_sms(self, user):
        LoginSteps().insert_sms(user.sms)
        return self

    @allure.step('Проверяем наличие ошибки')
    def check_error(self, text_error):
        LoginPage().error.should(have.text(text_error), timeout=3)
        return self

    @allure.step('Разлогинивание - выйти из профиля')
    def check_logout_manual_quit(self):
        LoginSteps().logout_manual_quit() \
            .title_page_login_password()

    @allure.step('Разлогинивание - сменить пользователя')
    def logout_manual_change_user(self):
        LoginSteps().logout_manual_change_user() \
            .title_page_login_password()
