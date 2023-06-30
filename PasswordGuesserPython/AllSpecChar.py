from CheckCaractere import SpecialCharacters
import string

class AllSpecialCharacters(SpecialCharacters):
    def __init__(self):
        super().__init__(list(string.punctuation))
