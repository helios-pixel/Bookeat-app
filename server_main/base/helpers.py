import re
import random
import string
from django.conf import settings
from django.http import JsonResponse
from twilio.rest import Client

def isValidPhone(phone):
    return re.search(r'^[0-9]{10}$', phone)

def create_otp():
    return ''.join(random.choices(string.digits, k=6))

def send_otp(phone, otp):
    account_sid = settings.ACCOUNT_SID
    auth_token = settings.AUTH_TOKEN
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            from_='+12313594239',
            body=f'Your otp is {otp}',
            to=f'+91{phone}'
        )
        return JsonResponse({'status': "success broooo", 'message': message.sid})
    except Exception as e:
        print("here",e)
        return JsonResponse({'status': message.error_code, 'message': str(message.error_message)})