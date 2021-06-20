import allure
from allure_commons.types import AttachmentType
from selene import have
from selene.support.shared import browser
from src.LoginPage import LoginPage
from src.User import *

base_url = "https://delo-prod.skblab.ru/login"


class LoginSteps:

    @allure.step(f'Открываем сайт')
    def open(self):
        browser.open(base_url)
        return self

    def check_title(self, title_text):
        browser.should(have.title_containing(title_text))
        return self

    def title_page_login_password(self):
        self.check_title('Делобанк - Вход')
        return self

    def title_page_login_confirm_sms(self):
        self.check_title('Делобанк - Подтверждение входа')
        return self

    @allure.step(f'Вводим логин')
    def input_login(self, name):
        LoginPage.login.set_value(name)
        return self

    @allure.step('Вводим пароль')
    def input_password(self, password):
        LoginPage.password.set_value(password)
        return self

    def press_button(self):
        LoginPage.submit_buttons.click()
        return self

    @allure.step('Ввод смс-ки')
    def insert_sms(self, sms):
        sms_num = list(sms)
        for i in range(len(sms_num)):
            LoginPage.input_sms_only[i].set_value(sms_num[i])
        return self

    def logout_manual_quit(self):
        LoginPage.customers_button.click()
        LoginPage.quit.click()
        LoginPage.change_user.click()
        return self

    def logout_manual_change_user(self):
        LoginPage.cancel.click()
        return self
