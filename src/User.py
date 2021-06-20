class User:
    def __init__(self, name, passw, sms):
        self.name = name
        self.passw = passw
        self.sms = sms

    def __repr__(self):
        return f"{self.name}, {self.passw}, {self.sms}"


right = User("335026", "1234", "1234")
wrong_login = User("ff", "1234", "1234")
wrong_password = User("testuser25", "2222", "1234")
wrong_sms = User("testuser24", "1234", "2222")
