from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Customer, ResturentOwner
from django.http import JsonResponse
import re
from base.helpers import *
import json
# Create your views here.

def create_customer(request):
    if request.method == 'POST':
        """
        taking all the required data from the request
        """
        data = json.loads(request.body.decode('utf-8'))
        first_name, last_name = data.get('name').split(' ')
        phone = data.get('phone')
        password = data.get('password')
        address = data.get('address')
        confirm_password = data.get('confirm_password')
        
        if password != confirm_password:
            return JsonResponse({'status': 'failed', 'message': 'password and confirm password does not match'})
        """
        validate the phone number
        """
        is_valid_phone = is_valid_phone(phone)
        if not is_valid_phone:
            return JsonResponse({'status': 'failed', 'message': 'invalid phone number'})
        """
        create the user and customer
        """
        user = User.objects.create(username=phone, first_name=first_name, last_name=last_name)
        user.set_password(password)
        otp = create_otp()
        user.save()
        customer = Customer.objects.create(profile=user, phone_number=phone, address=address, otp=otp)
        customer.save()
        #send_otp(phone, otp)
        """
        sending a final response
        """
        return JsonResponse({'status': 'success', 'message': 'customer created successfully', "data" : {
            "id": customer.id,
            "username": customer.profile.username,
            "email": customer.profile.email,
            "phone": customer.phone_number,
            "address": customer.address,
            "otp": customer.otp,
        }})
    return JsonResponse({'status': 'error', 'message': 'Invalid Request'})

def create_resturent_owner(request):
    if request.method == "POST":
        """
        taking all the required data from the request
        """
        data = json.loads(request.body.decode('utf-8'))
        first_name, last_name = data.get('name').split(' ')
        phone = data.get('phone')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        """
        validate the email and phone number
        """
        
        is_valid_phone = is_valid_phone(phone)
        if not is_valid_phone:
            return JsonResponse({'status': 'failed', 'message': 'invalid phone number'})
        
        if(password!=confirm_password):
            return JsonResponse({'status': 'failed', 'message': 'password and confirm password does not match'})
        """
        create the user and resturent owner
        """
        # transaction
        user = User.objects.create(username=phone, first_name=first_name, last_name=last_name)
        user.set_password(password)
        otp = create_otp()
        user.save()
        resturent_owner = ResturentOwner.objects.create(profile=user, phone_number=phone, otp=otp)
        resturent_owner.save()
        # send_otp(phone, otp)
        """
        sending a final response
        """
        return JsonResponse({'status': 'success', 'message': 'resturent owner created successfully', "data" : {
            "id": resturent_owner.id,
            "username": resturent_owner.profile.username,
            "email": resturent_owner.profile.email,
            "phone": resturent_owner.phone_number,
            "otp": resturent_owner.otp,
        }})
    return JsonResponse({'status': 'error', 'message': 'Invalid Request'})
    

def customerLogin(request):
    if request.method == "POST":
        """
        taking all the required data from the request
        """
        data = json.loads(request.body.decode('utf-8'))
        phone = data.get('phone')
        password = data.get('password')
        """
        validate phone number
        """
        """
        create the user and resturent owner
        """
        if phone:
            user = User.objects.filter(username=phone).first()
            if not user:
                return JsonResponse({'status': 'failed', 'message': 'phone number does not exist'})
            if(user.check_password(password)):
                return JsonResponse({'status': 'failed', 'message': 'Password Incorrect'})
            customer = Customer.objects.filter(profile=user).first()
            if not customer:
                return JsonResponse({'status': 'failed', 'message': 'invalid credentials'})
        """
        sending a final response
        """
        return JsonResponse({'status': 'success', 'message': 'customer logged in successfully', "data" : {
            "id": customer.id,
            "username": customer.profile.username,
            "phone": customer.phone_number,
            "address": customer.address
        }})
    return JsonResponse({'status': 'error', 'message': 'Invalid Request'})
    
def restaurantOwnerLogin(request):
    if request.method == "POST":
        """
        taking all the required data from the request
        """
        data = json.loads(request.body.decode('utf-8'))
        phone = data.get('phone')
        password = data.get('password')
        """
        validate phone number
        """
        is_valid_phone = is_valid_phone(phone)
        if not is_valid_phone:
            return JsonResponse({'status': 'failed', 'message': 'invalid phone number'})
        if(user.check_password(password)):
            return JsonResponse({'status': 'failed', 'message': 'Password Incorrect'})
        
        """
        create the user and resturent owner
        """
        if phone:
            user = User.objects.filter(username=phone).first()
            if not user:
                return JsonResponse({'status': 'failed', 'message': 'User does not exist'})
            restaurantOwner = ResturentOwner.objects.filter(profile=user).first()
            if not restaurantOwner:
                return JsonResponse({'status': 'failed', 'message': 'invalid credentials'})
        """
        sending a final response
        """
        return JsonResponse({'status': 'success', 'message': 'resturent owner logged in successfully', "data" : {
            "id": restaurantOwner.id,
            "username": restaurantOwner.profile.username,
            "phone": restaurantOwner.phone_number,
        }})
    return JsonResponse({'status': 'error', 'message': 'Invalid Request'})