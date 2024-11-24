import hashlib # I will use it to hash the password
import getpass # I will use to allow the user to write the password without showing password on the screen ; It can be used on terminal, The IDLE REPL does not meet this requirement.
import re

password_manager = {} # Dictionary to store the passwords and their "corresponding" hash values


def validate_password(password):
    """
    This function validates that the password followed the mesure security requirements.
    :param password: the password to validate
    :type password: str
    :return: True if the password follows the mesure security requirements, False otherwise
    :rtype: bool
    """
    if len(password) < 8:
        print("Password must be at least 8 characters long ! ")
        return False
    elif not re.search("[A-Z]", password):
        print("Password must integers at least one uppercase character ! ")
        return False
    elif not re.search("[a-z]", password):
        print("Password must integers at least one lowercase character ! ")
        return False
    elif not re.search("/d", password):
        print("Password must integers at least one number ! ")
        return False
    elif not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        print("Password must not contain special characters ! ")
        return False
    print("Password is valid!")
    return True

