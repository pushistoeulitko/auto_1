import time
import requests
import allure
from allure_commons.types import AttachmentType
from selene import browser
from selene.support import by
from selene.support.conditions import have
from selene.support.jquery_style_selectors import s, ss
#from selene.support.shared import browser, config


url="https://delo-prod.skblab.ru/login"

class Elements(object):

    def __init__(self):
        self.login = s('input.with-icon.text')
        self.password = s('input[type=password]')
        self.submint_buttons = s('ui-button.button-login')
        self.input_sms = s('div.sms-input-container')
        self.input_sms_only = ss('input[type = "number"]')
        self.error = s('div.errors')
        self.profile = s(by.xpath("//div[@id = 'logout-button']"))
        self.change_user = s(by.xpath("//a[contains(text(), 'Сменить пользователя')]"))


    def open(self):
        browser.open_url(url)
        return self


    @allure.step(f'Вводим логин')
    def step_with_title1(self,  user):
        pass

    def input_login(self, user):
        self.step_with_title1(user.name)
        self.login.set_value(user.name)
        return self

    @allure.step('Вводим пароль')
    def step_with_title2(self, password):
        pass

    def input_password(self, user):
        self.step_with_title2(user.passw)
        self.password.set_value(user.passw)
        return self

    @allure.step('Нажимаем кнопку войти')
    def step_with_title3(self, button):
        pass

    def press_button(self):
        self.step_with_title3(self.submint_buttons)
        self.submint_buttons.click()
        return self


    # def login_as(self, user):
    #     with allure.step('Вводим логин'):
    #         try:
    #             self.login.set_value(user.name)
    #             selene.browser.take_screenshot()
    #         except IOError as e:
    #             print(e)
    #         #allure.attach('Логин', user.name)
    #     with allure.step('Вводим пароль'):
    #         self.password.set_value(user.passw)
    #         selene.browser.take_screenshot()
    #         #allure.attach('Пароль', user.passw)
    #     with allure.step('Нажимаем кнопку войти'):
    #         self.submint_buttons.click()
    #         selene.browser.take_screenshot()
    #         #allure.attach('Локатор', self.submint_bottons)
    #     time.sleep(2)
    #     # with allure.step('Успешный ввод'):
    #     #     allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    #     return self

    @allure.step('Проверка заголовка')
    def step_with_title4(self, title_text):
        pass

    def check_title(self, title_text):
        self.step_with_title4(title_text)
        browser.should(have.title_containing(title_text))
        return self

    @allure.step('Ввод смс-ки')
    def step_with_title5(self, sms):
        pass

    def insert_sms(self, user):
        self.step_with_title5(user.sms)
        sms_num = list(user.sms)
        for i in range(len(sms_num)):
            self.input_sms_only[i].set(sms_num[i])
           # selene.browser.take_screenshot()
        return self


    @allure.step('Проверяем наличие ошибки')
    def step_with_title6(self, sms):
        pass

    def check_error(self, text_error):
        self.step_with_title6(text_error)
        try:
            self.error.should(have.text(text_error)), f"Не удалось зарегистрироваться {text_error}"
           # selene.browser.take_screenshot()
        except IOError as e:
            print(e)


    def logout_manual(self):
        self.profile.click()
        self.change_user.click()

    def logout(self):
        response = requests.get('https://delo-prod.skblab.ru/json/logout')
        print(response.status_code)
        #assert response.content == '{"success":true}'
        #assert response.status_code == '<Response [200]>'
        time.sleep(6)
        return self

    def clear_cookie(self):
        browser.driver().delete_all_cookies()

    # def at_page_main(self):
    #     return MainPage

