import secrets
import string
from pyperclip import copy
from validators import Validators

secure_random = secrets.SystemRandom()
letters = string.ascii_letters
digits = string.digits
special = string.punctuation
password_validators = [
    Validators.long_enough,
    Validators.has_lowercase,
    Validators.has_uppercase,
    Validators.has_numeric,
    Validators.has_special
]


def test_password(password):
    for test_fn in password_validators:
        if not test_fn(password):
            return False
    return True


def password_generator(password_len, name=None):
    if Validators.short_enough(password_len):
        password_scope = letters + digits + special
        list_of_random_characters = secure_random.sample(password_scope, password_len)
        password = ''.join(list_of_random_characters)
        if not test_password(password):
            password_generator(password_len)
        else:
            # copies generated password to the clipboard
            copy(password)
            if not name:
                print(password)
            else:
                print('Generated password for {} account is {} '.format(name, password))
    else:
        print(Validators.short_enough.__doc__)
