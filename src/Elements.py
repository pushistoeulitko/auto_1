import time
from webbrowser import Chrome
import requests
import allure
from selene import by, be, have, Browser, Config
from selene.config import base_url
from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser, config

config.base_url = "https://delo-prod.skblab.ru/login"


# config.start_maximized = True
# config.window_width = 1250


class Elements(object):

    def __init__(self):
        self.login = s('input.with-icon.text')
        self.password = s('input[type=password]')
        self.submit_buttons = s('ui-button.button-login')
        self.input_sms = s('div.sms-input-container')
        self.input_sms_only = ss('input[type = "number"]')
        self.error = s('div.errors')
        self.profile = s(by.xpath("//div[@id = 'logout-button']"))
        self.change_user = s(by.xpath("//a[contains(text(), 'Сменить пользователя')]"))
        # self.customers_button =s('#customers-button')
        self.customers_button = s('div.user-icon')
        self.quit = s(by.xpath("//span[contains(text(), 'Выйти')]"))


    def open(self):
        try:
            browser.open(base_url)
        except IOError as e:
            print(e)
        return self

    @allure.step(f'Вводим логин')
    def step_with_title1(self, user, locator):
        pass

    def input_login(self, user):
        self.step_with_title1(user.name, str(self.login))
        try:
            self.login.set_value(user.name)
        except IOError as e:
            print(e)
        return self

    @allure.step('Вводим пароль')
    def step_with_title2(self, locator, password):
        pass

    def input_password(self, user):
        self.step_with_title2(str(self.password), user.passw)
        try:
            self.password.set_value(user.passw)
            browser.take_screenshot()
        except IOError as e:
            print(e)
        return self

    @allure.step('Нажимаем кнопку войти')
    def step_with_title3(self, locator):
        pass

    def press_button(self):
        self.step_with_title3(str(self.submit_buttons))
        try:
            self.submit_buttons.click()
            browser.take_screenshot()
        except IOError as e:
            print(e)
        return self

    @allure.step('Проверка заголовка')
    def step_with_title4(self, title_text):
        pass

    def check_title(self, title_text):
        self.step_with_title4(title_text)
        try:
            browser.should(have.title_containing(title_text))
            browser.take_screenshot()
        except IOError as e:
            print(e)
        return self

    @allure.step('Ввод смс-ки')
    def step_with_title5(self, locator, sms):
        pass

    def insert_sms(self, user):
        self.step_with_title5(str(self.input_sms_only), user.sms)
        try:
            sms_num = list(user.sms)
            for i in range(len(sms_num)):
                self.input_sms_only[i].set_value(sms_num[i])
                browser.take_screenshot()
        except IOError as e:
            print(e)
        return self

    @allure.step('Проверяем наличие ошибки')
    def step_with_title6(self, locator, text_error):
        pass

    def check_error(self, text_error):
        self.step_with_title6(str(self.error), text_error)
        try:
            browser.take_screenshot()
            self.error.should(have.text(text_error), timeout=3), f"Не удалось зарегистрироваться {text_error}"
        except IOError as e:
            print(e)

    # разлогинивание

    def logout_manual(self):
        self.profile.click()
        self.change_user.click()

    def logout_manual2(self):
        self.customers_button.click()
        self.quit.click()
        self.change_user.click()

    def logout(self):
        response = requests.get('https://delo-prod.skblab.ru/json/logout')
        print(response.status_code)
        # assert response.content == '{"success":true}'
        # assert response.status_code == '<Response [200]>'
        time.sleep(6)
        return self

    def clear_cookie(self):
        browser.driver().delete_all_cookies()

    # def at_page_main(self):
    #     return MainPage
