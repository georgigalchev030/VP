class InvalidCommand(Exception):
    def __init__(self, message):
        self.message = message


class InvalidDataFormat(Exception):
    def __init__(self, message):
        self.message = message


class CharacterExists(Exception):
    def __init__(self, message):
        self.message = message


class InvalidCharacterClass(Exception):
    def __init__(self, message):
        self.message = message


class CharacterNotFound(Exception):
    def __init__(self, message):
        self.message = message
