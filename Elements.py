import time

import allure
from allure_commons.types import AttachmentType
from selene import browser
from selene.support.conditions import have
from selene.support.jquery_style_selectors import s, ss
from MainPage import MainPage
from User import User


class Elements(object):

    def __init__(self):
        self.login = s('input.with-icon.text')
        self.password = s('input[type=password]')
        self.submint_bottons = s('ui-button.button-login')
        self.input_sms = s('div.sms-input-container')
        self.input_sms_only = ss('input[type = "number"]')
        self.error = s('div.errors')

    def open(self):
        browser.open_url("https://delo-prod.skblab.ru/login")
        return self

    def login_as(self, user):
        with allure.step('Вводим логин'):
            try:
                self.login.set_value(user.name)
            except IOError as e:
                print(e)
           # allure.attach('Логин', user.name)
        with allure.step('Вводим пароль'):
            self.password.set_value(user.passw)
            #allure.attach('Пароль', user.passw)
        with allure.step('Нажимаем кнопку войти'):
            self.submint_bottons.click()
           # allure.attach('Локатор', self.submint_bottons)
        time.sleep(1)
        # with allure.step('Успешный ввод'):
        #     allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        return self

    def insert_sms(self, user):
        with allure.step('Вводим смс'):
            sms_num = list(user.sms)
            for i in range(len(sms_num)):
                self.input_sms_only[i].set(sms_num[i])
            time.sleep(1)
            return self


    def check_error(self, text_error):
        with allure.step('Проверяем наличие ошибки'):
            self.error.is_displayed().should(have.text(text_error))

    def clear_cookie(self):
        browser.driver().delete_all_cookies()

    # def at_page_main(self):
    #     return MainPage
