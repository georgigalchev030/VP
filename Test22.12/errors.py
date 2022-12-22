class InvalidCommand(Exception):
    def __init__(self, message):
        self.message = message


class InvalidDataFormat(Exception):
    def __init__(self, message):
        self.message = message


class InvalidAccCurrency(Exception):
    def __init__(self, message):
        self.message = message


class InvalidAccType(Exception):
    def __init__(self, message):
        self.message = message


class UserNotFound(Exception):
    def __init__(self, message):
        self.message = message


class AccNotFound(Exception):
    def __init__(self, message):
        self.message = message