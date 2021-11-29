import random
import string

class Password:

    def __init__(self):
        self.password = None

    def set(self, length: int, digits=bool, alphabets=bool, specialchars=bool):
        list_digits = list(string.digits)
        list_alphabets = list(string.ascii_letters)
        list_specialchars = list("!@#$%^&*()")
        password = ""
        password_chars = []
        chars = []

        if digits:
            chars += list_digits
        if alphabets:
            chars += list_alphabets
        if specialchars:
            chars += list_specialchars

        for i in range(length):
            password_chars.append(random.choice(chars))

        random.shuffle(password_chars)

        for char in password_chars:
            password += char

        self.password = password

    def get(self):
        return self.password