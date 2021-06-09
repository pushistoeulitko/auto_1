import time
import pytest
import requests
import allure
from allure_commons.types import AttachmentType
from selene import by, be, have, Browser, Config
from selene.config import base_url
from selene.core.query import screenshot
from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser, config


class Decorator:
    def __init__(self, func):
        print('> Класс Decorator метод __init__')
        self.func = func

    def __call__(self, *args):
        print('> до вызова из класса...', self.func.__name__)
        self.func(*args)
        print('> после вызова из класса')


@Decorator
def wrapped(self, *args):
    try:
        self.func(*args)
    except AssertionError as e:
        allure.attach.file(browser.save_screenshot(), name="Screenshot", attachment_type=AttachmentType.PNG)
        raise print(e)
    return wrapped



class Elements(object):

    def __init__(self):
        self.login = s('input.with-icon.text')
        # self.login = s('input.wi')
        self.password = s('input[type=password]')
        #self.password = s('input[t')
        self.submit_buttons = s('ui-button.button-login')
        self.input_sms = s('div.sms-input-container')
        self.input_sms_only = ss('input[type = "number"]')
        self.error = s('div.errors')
        self.profile = s(by.xpath("//div[@id = 'logout-button']"))
        self.change_user = s(by.xpath("//a[contains(text(), 'Сменить пользователя')]"))
        # self.customers_button =s('#customers-button')
        self.customers_button = s('div.user-icon')
        self.quit = s(by.xpath("//span[contains(text(), 'Выйти')]"))
        self.cancel = s('a.button-back')

    # сделать скрин
    def screenshot(self):
        # browser.last_screenshot()
        # allure.attach(browser.last_screenshot(), name="Screenshot", attachment_type=AttachmentType.PNG)
        allure.attach.file(browser.save_screenshot(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def decorator_screenshot(self, func):
        def wrapper(*args):
            try:
                func(*args)
            except AssertionError as e:
                allure.attach.file(browser.save_screenshot(), name="Screenshot", attachment_type=AttachmentType.PNG)
                raise print(e)
        return wrapper




    @allure.step(f'Открываем сайт')
    # def step_with_title0(self, url):
    #     pass

    #@Decorator
    #@decorator_screenshot
    def open(self):
        # self.step_with_title0(self, str(base_url))
        browser.open(base_url)
        return self

    @allure.step(f'Вводим логин')
    def step_with_title1(self, user, locator):
        pass

    def input_login(self, user):
        try:
            self.step_with_title1(user.name, self.get_locator(self.login))
            self.login.set_value(user.name)
        except Exception as e:
            self.screenshot()
            assert False, print('Что то пошло не так, мы уже работаем над этим', e)
        return self

    @allure.step('Вводим пароль')
    def step_with_title2(self, locator, password):
        pass

    def input_password(self, user):
        self.step_with_title2(self.get_locator(self.password), user.passw)
        try:
            self.password.set_value(user.passw)
        except Exception as e:
            self.screenshot()
            assert False, print('Что то пошло не так, мы уже работаем над этим', e)
        return self

    @allure.step('Нажимаем кнопку войти')
    def step_with_title3(self, locator):
        pass

    def press_button(self):
        self.step_with_title3(self.get_locator(self.submit_buttons))
        try:
            self.submit_buttons.click()
        except Exception as e:
            self.screenshot()
            assert False, print('Что то пошло не так, мы уже работаем над этим', e)
        return self

    @allure.step('Проверка заголовка')
    def step_with_title4(self, title_text):
        pass

    def check_title(self, title_text):
        self.step_with_title4(title_text)
        try:
            browser.should(have.title_containing(title_text))
        except Exception as e:
            self.screenshot()
            assert False, print('Что то пошло не так, мы уже работаем над этим', e)
        return self

    @allure.step('Ввод смс-ки')
    def step_with_title5(self, locator, sms):
        pass

    def insert_sms(self, user):
        self.step_with_title5(self.get_locator(self.input_sms_only[0]), user.sms)
        try:
            sms_num = list(user.sms)
            for i in range(len(sms_num)):
                self.input_sms_only[i].set_value(sms_num[i])
        except Exception as e:
            self.screenshot()
            assert False, print('Что то пошло не так, мы уже работаем над этим', e)
        return self

    @allure.step('Проверяем наличие ошибки')
    def step_with_title6(self, locator, text_error):
        pass

    def check_error(self, text_error):
        self.step_with_title6(self.get_locator(self.error), text_error)
        try:
            self.error.should(have.text(text_error), timeout=3), f"Не удалось зарегистрироваться {text_error}"
        except Exception as e:
            self.screenshot()
            print(e)
            assert False, print('Что то пошло не так, мы уже работаем над этим')

    # разлогинивание

    def logout_manual(self):
        self.profile.click()
        self.change_user.click()

    def logout_manual2(self):
        self.customers_button.click()
        self.quit.click()
        self.change_user.click()

    def logout_manual3(self):
        self.cancel.click()

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

    #  преобразование элемента
    def get_locator(self, selene_element):
        locator = str(selene_element)[17:-3]
        return locator
