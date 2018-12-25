import secrets
import string
from pyperclip import copy
from validators import validators

secure_random = secrets.SystemRandom()
letters = string.ascii_letters
digits = string.digits
special = string.punctuation
validator = [
              validators.long_enough,
              validators.has_lowercase,
              validators.has_uppercase,
              validators.has_numeric,
              validators.has_special
            ]

def test_password(pw, validators = validator):
    for test in validators:
        if not test(pw):
            return False
    return True

def password_generator(password_len, name=None):
    if validators.short_enough(password_len):
        password_scope = letters + digits + special
        list_of_random_characters = secure_random.sample(password_scope, password_len)
        password = ''.join(list_of_random_characters)
        if not test_password(password):
            password_generator(password_len)
        else:
            # copies generated password to the clipbord
            copy(password)
            if name == None:
                print( password)
            else:
                print('Generated password for {} account is {} '.format(name, password))
    else:
        print(validators.short_enough.__doc__)

