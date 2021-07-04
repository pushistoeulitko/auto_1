class User:
    def __init__(self, name, passw="1234", sms="1234"):
        self.name = name
        self.passw = passw
        self.sms = sms

    def __repr__(self):
        return f"{self.name}, {self.passw}, {self.sms}"

