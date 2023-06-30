import random

class SpecialCharacters:
    def __init__(self, characters):
        self._characters = characters

    def generate(self, length=1):
        return ''.join(random.choice(self._characters) for _ in range(length))




