import string

class validators:

    def long_enough(password):
        'Password must be at least 6 characters'
        check = len(password) >= 6
        if check:
            return check
        else:
            return validators.long_enough.__doc__

    def short_enough(password):
        'Password cannot be more than 32 characters'
        if password > 32:
            return False
        return True

    def has_lowercase(password):
        'Password must contain a lowercase letter'
        check = len(set(string.ascii_lowercase).intersection(password)) > 0
        if check:
            return check
        else:
            return validators.has_lowercase.__doc__

    def has_uppercase(password):
        'Password must contain an uppercase letter'
        check = len(set(string.ascii_uppercase).intersection(password)) > 0
        if check:
            return check
        else:
            return validators.has_uppercase.__doc__

    def has_numeric(password):
        'Password must contain a digit'
        check = len(set(string.digits).intersection(password)) > 0
        if check:
            return check
        else:
            return validators.has_numeric.__doc__


    def has_special(password):
        'Password must contain a special character'
        check = len(set(string.punctuation).intersection(password)) > 0
        if check:
            return check
        else:
            return validators.has_special().__doc__
