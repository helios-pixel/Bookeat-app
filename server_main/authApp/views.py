from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Customer, ResturentOwner
from django.http import JsonResponse
import re
from base.helpers import *
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def create_customer(request):
    try:
        if request.method == 'POST':
            """
            taking all the required data from the request
            """
            data = json.loads(request.body.decode('utf-8'))
            first_name, last_name = data.get('name').split(' ')
            phone = data.get('phone')
            password = data.get('password')
            address = ''
            confirm_password = data.get('confirm_password')
            
            if password != confirm_password:
                return JsonResponse({'status': 'failed', 'message': 'password and confirm password does not match'})
            """
            validate the phone number
            """
            is_valid_phone = isValidPhone(phone)
            if not is_valid_phone:
                return JsonResponse({'status': 'failed', 'message': 'invalid phone number'})
            """
            create the user and customer
            """
            
            isUser = User.objects.filter(username=phone).first()
            if isUser:
                return JsonResponse({'status': 'failed', 'message': 'phone number already exist'})

            user = User.objects.create(username=phone, first_name=first_name, last_name=last_name)
            user.set_password(password)
            otp = create_otp()
            user.save()
            customer = Customer.objects.create(profile=user, phone_number=phone, address=address, otp=otp)
            customer.save()
            otp_response = send_otp(phone, otp)
            print(otp_response)
            # response is like this - <JsonResponse status_code=200, "application/json">
            if otp_response.status_code != 200:
                user.delete()
                customer.delete()
                return JsonResponse({'status': 'failed', 'message': 'otp not sent'})
            """
            sending a final response
            """
            return JsonResponse({'status': 'success', 'message': 'customer created successfully', "data" : {
                "id": customer.id,
                "name" : customer.profile.first_name + " " + customer.profile.last_name,
                "username": customer.profile.username,
                "email": customer.profile.email,
                "phone": customer.phone_number,
                "address": customer.address,
                "role": "customer"
            }})
        return JsonResponse({'status': 'error', 'message': 'Invalid Request'})
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'error', 'message': e})

@csrf_exempt
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
        license_num = data.get('license_num')
        pan = data.get('pan')
        gstin = data.get('gstin')
        """
        validate the email and phone number
        """
        
        is_valid_phone = isValidPhone(phone)
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
        resturent_owner = ResturentOwner.objects.create(profile=user, phone_number=phone, otp=otp, license_num=license_num, pan=pan, gstin=gstin)
        resturent_owner.save()
        print(resturent_owner)
        print(resturent_owner.otp)
        response = send_otp(phone, otp)
        print(response)
        if response.status_code != 200:
            user.delete()
            resturent_owner.delete()
            return JsonResponse({'status': 'failed', 'message': 'otp not sent'})
        """
        sending a final response
        """
        return JsonResponse({'status': 'success', 'message': 'resturent owner created successfully', "data" : {
            "id": resturent_owner.id,
            "name" : resturent_owner.profile.first_name + " " + resturent_owner.profile.last_name,
            "username": resturent_owner.profile.username,
            "email": resturent_owner.profile.email,
            "phone": resturent_owner.phone_number,
            "otp": resturent_owner.otp,
            "role": "resturent_owner"
        }})
    return JsonResponse({'status': 'error', 'message': 'Invalid Request'})
    
@csrf_exempt
def customerLogin(request):
    if request.method == "POST":
        """
        taking all the required data from the request
        """
        data = json.loads(request.body.decode('utf-8'))
        phone = data.get('phone')
        password = data.get('password')
        print(phone, password)
        """
        validate phone number
        """
        """
        create the user and resturent owner
        """
        if phone:
            user = User.objects.filter(username=phone).first()
            print(user)
            if not user:
                return JsonResponse({'status': 'failed', 'message': 'phone number does not exist'})
            print(user.check_password(password))
            if(not user.check_password(password)):
                return JsonResponse({'status': 'failed', 'message': 'Password Incorrect'})
            print('user', user)
            customer = Customer.objects.filter(profile=user).first()
            if not customer:
                return JsonResponse({'status': 'failed', 'message': 'invalid credentials'})
        """
        sending a final response
        """
        return JsonResponse({'status': 'success', 'message': 'customer logged in successfully', "data" : {
            "id": customer.id,
            "name" : customer.profile.first_name + " " + customer.profile.last_name,
            "username": customer.profile.username,
            "phone": customer.phone_number,
            "address": customer.address,
            "role": "customer"
        }})
    return JsonResponse({'status': 'error', 'message': 'Invalid Request'})
    
@csrf_exempt
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
        is_valid_phone = isValidPhone(phone)
        if not is_valid_phone:
            return JsonResponse({'status': 'failed', 'message': 'invalid phone number'})
        
        """
        create the user and resturent owner
        """
        if phone:
            user = User.objects.filter(username=phone).first()
            if not user:
                return JsonResponse({'status': 'failed', 'message': 'User does not exist'})
            
            if(not user.check_password(password)):
                return JsonResponse({'status': 'failed', 'message': 'Password Incorrect'})
            restaurantOwner = ResturentOwner.objects.filter(profile=user).first()
            if not restaurantOwner:
                return JsonResponse({'status': 'failed', 'message': 'invalid credentials'})
        """
        sending a final response
        """
        return JsonResponse({'status': 'success', 'message': 'resturent owner logged in successfully', "data" : {
            "id": restaurantOwner.id,
            "name" : restaurantOwner.profile.first_name + " " + restaurantOwner.profile.last_name,
            "username": restaurantOwner.profile.username,
            "phone": restaurantOwner.phone_number,
            "role": "resturent_owner"
        }})
    return JsonResponse({'status': 'error', 'message': 'Invalid Request'})

@csrf_exempt
def verify_otp(request):
    if request.method == "POST":
        """
        taking all the required data from the request
        """
        data = json.loads(request.body.decode('utf-8'))
        phone = data.get('phone')
        otp = data.get('otp')
        """
        validate phone number
        """
        is_valid_phone = isValidPhone(phone)
        if not is_valid_phone:
            return JsonResponse({'status': 'failed', 'message': 'invalid phone number'})
        """
        validate otp
        """
        if not otp:
            return JsonResponse({'status': 'failed', 'message': 'invalid otp'})
        """
        create the user and resturent owner
        """
        if phone:
            user = User.objects.filter(username=phone).first()
            if not user:
                return JsonResponse({'status': 'failed', 'message': 'User does not exist'})
            customer = Customer.objects.filter(profile=user).first()
            if customer:
                if otp != customer.otp:
                    return JsonResponse({'status': 'failed', 'message': 'invalid otp'})
                customer.is_otp_verified = True
                customer.otp = ""
                customer.save()
                return JsonResponse({'status': 'success', 'message': 'otp verified successfully', "data" : {
                    "id": customer.id,
                    "phone": customer.phone_number,
                }})
            restaurantOwner  = ResturentOwner.objects.filter(profile=user).first()
            if restaurantOwner:
                if otp != restaurantOwner.otp:
                    return JsonResponse({'status': 'failed', 'message': 'invalid otp'})
                restaurantOwner.is_otp_verified = True
                restaurantOwner.otp = ""
                restaurantOwner.save()

                return JsonResponse({'status': 'success', 'message': 'otp verified successfully', "data" : {
                    "id": restaurantOwner.id,
                    "phone": restaurantOwner.phone_number,
                }})

            if not customer and not restaurantOwner:
                return JsonResponse({'status': 'failed', 'message': 'invalid credentials'})
            
        return JsonResponse({'status': 'error', 'message': 'Invalid Request'})
        
    return JsonResponse({'status': 'error', 'message': 'Invalid Request'})

@csrf_exempt
def update_customer(request):
    if request.method == "POST":
        """
        taking all the required data from the request
        """
        print(request.body, "here")
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        phone = data.get('phone')
        address = data.get('address')
        email = data.get('email')
        fName = data.get('fName')
        lName = data.get('lName')
        role = data.get('role')
        
        """
        validate phone number
        """
        is_valid_phone = isValidPhone(phone)
        if not is_valid_phone:
            return JsonResponse({'status': 'failed', 'message': 'invalid phone number'})
        
        # update the user and customer
        user = User.objects.filter(username=phone).first()
        if not user:
            return JsonResponse({'status': 'failed', 'message': 'User does not exist'})
        if role == "customer":
            customer = Customer.objects.filter(profile=user).first()
            if not customer:
                return JsonResponse({'status': 'failed', 'message': 'invalid credentials'})
            if address:
                customer.address = address
            if email:
                customer.profile.email = email
            if fName:
                customer.profile.first_name = fName
            if lName:
                customer.profile.last_name = lName
            customer.save()
            customer.profile.save()

            return JsonResponse({'status': 'success', 'message': 'customer updated successfully', "data" : {
                "id": customer.id,
                "name" : customer.profile.first_name + " " + customer.profile.last_name,
                "username": customer.profile.username,
                "email": customer.profile.email,
                "phone": customer.phone_number,
                "address": customer.address,
                "role": "customer"
            }})
        if role == "resturent_owner":
            restaurantOwner = ResturentOwner.objects.filter(profile=user).first()
            if not restaurantOwner:
                return JsonResponse({'status': 'failed', 'message': 'invalid credentials'})
            if address:
                restaurantOwner.address = address
            if email:
                restaurantOwner.profile.email = email
            if fName:
                restaurantOwner.profile.first_name = fName
            if lName:
                restaurantOwner.profile.last_name = lName
            restaurantOwner.save()
            restaurantOwner.profile.save()

            return JsonResponse({'status': 'success', 'message': 'resturent owner updated successfully', "data" : {
                "id": restaurantOwner.id,
                "name" : restaurantOwner.profile.first_name + " " + restaurantOwner.profile.last_name,
                "username": restaurantOwner.profile.username,
                "email": restaurantOwner.profile.email,
                "phone": restaurantOwner.phone_number,
                "address": restaurantOwner.address,
                "role": "resturent_owner"
            }})
    return JsonResponse({'status': 'error', 'message': 'Invalid Request'})
        
@csrf_exempt
def forgot_password(request):
    if request.method == "POST":
        """
        taking all the required data from the request
        """
        data = json.loads(request.body.decode('utf-8'))
        phone = data.get('phone')

        """
        validate phone number
        """
        is_valid_phone = isValidPhone(phone)
        if not is_valid_phone:
            return JsonResponse({'status': 'failed', 'message': 'invalid phone number'})
        """
        check if the user exists
        """
        user = User.objects.filter(username=phone).first()
        if not user:
            return JsonResponse({'status': 'failed', 'message': 'User does not exist'})
        """
        check if user is customer or resturent owner
        """
        customer = Customer.objects.filter(profile=user).first()
        if customer:
            otp = create_otp()
            customer.otp = otp
            customer.save()
            response = send_otp(phone, otp)
            if response.status_code != 200:
                return JsonResponse({'status': 'failed', 'message': 'otp not sent'})
            return JsonResponse({'status': 'success', 'message': 'otp sent successfully', "data" : {
                "id": customer.id,
                "phone": customer.phone_number,
            }})
        restaurantOwner = ResturentOwner.objects.filter(profile=user).first()
        if restaurantOwner:
            otp = create_otp()
            restaurantOwner.otp = otp
            restaurantOwner.save()
            response = send_otp(phone, otp)
            if response.status_code != 200:
                return JsonResponse({'status': 'failed', 'message': 'otp not sent'})
            return JsonResponse({'status': 'success', 'message': 'otp sent successfully', "data" : {
                "id": restaurantOwner.id,
                "phone": restaurantOwner.phone_number,
            }})
        return JsonResponse({'status': 'failed', 'message': 'invalid credentials'})
    return JsonResponse({'status': 'error', 'message': 'Invalid Request'})

@csrf_exempt
def validate_otp(request):
    if request.method == "POST":
        """
        taking all the required data from the request
        """
        data = json.loads(request.body.decode('utf-8'))
        phone = data.get('phone')
        otp = data.get('otp')
        
        """
        validate phone number
        """
        # is_valid_phone = isValidPhone(phone)
        # if not is_valid_phone:
        #     return JsonResponse({'status': 'failed', 'message': 'invalid phone number'})
        """
        check if the user exists
        """
        user = User.objects.filter(username=phone).first()
        if not user:
            return JsonResponse({'status': 'failed', 'message': 'User does not exist'})
        """
        check if user is customer or resturent owner
        """
        customer = Customer.objects.filter(profile=user).first()
        if customer:
            if otp != customer.otp:
                return JsonResponse({'status': 'failed', 'message': 'invalid otp'})
            return JsonResponse({'status': 'success', 'message': 'otp verified successfully', "data" : {
                "id": customer.id,
                "phone": customer.phone_number,
            }})
        restaurantOwner = ResturentOwner.objects.filter(profile=user).first()
        if restaurantOwner:
            if otp != restaurantOwner.otp:
                return JsonResponse({'status': 'failed', 'message': 'invalid otp'})
            return JsonResponse({'status': 'success', 'message': 'otp verified successfully', "data" : {
                "id": restaurantOwner.id,
                "phone": restaurantOwner.phone_number,
            }})
        return JsonResponse({'status': 'failed', 'message': 'invalid credentials'})
    return JsonResponse({'status': 'error', 'message': 'Invalid Request'})

@csrf_exempt
def reset_password(request):
    if request.method == "POST":
        """
        taking all the required data from the request
        """
        data = json.loads(request.body.decode('utf-8'))
        phone = data.get('phone')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        
        """
        validate phone number
        """
        # is_valid_phone = isValidPhone(phone)
        # if not is_valid_phone:
        #     return JsonResponse({'status': 'failed', 'message': 'invalid phone number'})
        """
        check if the user exists
        """
        user = User.objects.filter(username=phone).first()
        if not user:
            return JsonResponse({'status': 'failed', 'message': 'User does not exist'})
        """
        check if user is customer or resturent owner
        """
        customer = Customer.objects.filter(profile=user).first()
        if customer:
            user.set_password(password)
            user.save()
            return JsonResponse({'status': 'success', 'message': 'password reset successfully', "data" : {
                "id": customer.id,
                "phone": customer.phone_number,
            }})
        restaurantOwner = ResturentOwner.objects.filter(profile=user).first()
        if restaurantOwner:
            user.set_password(password)
            user.save()
            return JsonResponse({'status': 'success', 'message': 'password reset successfully', "data" : {
                "id": restaurantOwner.id,
                "phone": restaurantOwner.phone_number,
            }})
        return JsonResponse({'status': 'failed', 'message': 'invalid credentials'})
    return JsonResponse({'status': 'error', 'message': 'Invalid Request'})
