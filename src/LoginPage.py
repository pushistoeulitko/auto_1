from selene.support.shared.jquery_style import s, ss
from selene import by


class LoginPage:
    login = s('input.with-icon.text')
    password = s('input[type=password]')
    submit_buttons = s('ui-button.button-login')
    input_sms = s('div.sms-input-container')
    input_sms_only = ss('input[type = "number"]')
    error = s('div.errors')
    profile = s(by.xpath("//div[@id = 'logout-button']"))
    change_user = s(by.xpath("//a[contains(text(), 'Сменить пользователя')]"))
    customers_button = s('div.user-icon')
    quit = s(by.xpath("//span[contains(text(), 'Выйти')]"))
    cancel = s('a.button-back')
