import re
import random
import string

def isValidPhone(phone):
    return re.search(r'^[0-9]{10}$', phone)

def create_otp():
    return ''.join(random.choices(string.digits, k=6))