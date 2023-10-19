import re

def alphanumeric(password):
    if len(password) == 0:
        return False
    checked_password = re.search("[0-9a-zA-Z]*", password)
    if checked_password == None:
        return False
    print(checked_password.group())
    if checked_password.group() != password:
        return False
    return True
