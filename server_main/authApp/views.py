from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Customer, ResturentOwner
from django.http import JsonResponse
import re
# Create your views here.

def create_customer(request):
    if request.method == 'POST':
        """
        taking all the required data from the request
        """
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name, last_name = request.POST.get('name').split(' ')
        """
        validate the email and phone number
        """
        is_valid_email = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
        if not is_valid_email:
            return JsonResponse({'status': 'failed', 'message': 'invalid email'})
        is_valid_phone = re.search(r'^[0-9]{10}$', phone)
        if not is_valid_phone:
            return JsonResponse({'status': 'failed', 'message': 'invalid phone number'})
        """
        create the user and customer
        """
        user = User.objects.create_user(username=email, password=password, email=email, first_name=first_name, last_name=last_name)
        otp = create_otp()
        user.save()
        customer = Customer.objects.create(profile=user, phone_number=phone, address=address, otp=otp)
        customer.save()
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

def create_resturent_owner(request):
    if request.method == "POST":
        """
        taking all the required data from the request
        """
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        first_name, last_name = request.POST.get('name').split(' ')

        """
        validate the email and phone number
        """
        is_valid_email = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
        if not is_valid_email:
            return JsonResponse({'status': 'failed', 'message': 'invalid email'})
        is_valid_phone = re.search(r'^[0-9]{10}$', phone)
        if not is_valid_phone:
            return JsonResponse({'status': 'failed', 'message': 'invalid phone number'})
        """
        create the user and resturent owner
        """
        user = User.objects.create_user(username=email, password=password, email=email, first_name=first_name, last_name=last_name)
        otp = create_otp()
        user.save()
        resturent_owner = ResturentOwner.objects.create(profile=user, phone_number=phone, otp=otp)
        resturent_owner.save()
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
    

def customerLogin(request):
    if request.method == "POST":
        """
        taking all the required data from the request
        """
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        """
        validate the email and phone number
        """
        is_valid_email = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
        if not is_valid_email:
            return JsonResponse({'status': 'failed', 'message': 'invalid email'})
        """
        create the user and resturent owner
        """
        if email:
            user = User.objects.filter(username=email).first()
            if not user:
                return JsonResponse({'status': 'failed', 'message': 'invalid email'})
            customer = Customer.objects.filter(profile=user).first()
        if phone:
            customer = Customer.objects.filter(phone_number=phone).first()
            if not customer:
                return JsonResponse({'status': 'failed', 'message': 'invalid phone number'})
        if not customer:
            return JsonResponse({'status': 'failed', 'message': 'invalid credentials'})
        """
        sending a final response
        """
        return JsonResponse({'status': 'success', 'message': 'customer logged in successfully', "data" : {
            "id": customer.id,
            "username": customer.profile.username,
            "email": customer.profile.email,
            "phone": customer.phone_number,
            "address": customer.address
        }})
    
def restaurantOwnerLogin(request):
    if request.method == "POST":
        """
        taking all the required data from the request
        """
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        """
        validate the email and phone number
        """
        is_valid_email = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
        if not is_valid_email:
            return JsonResponse({'status': 'failed', 'message': 'invalid email'})
        """
        create the user and resturent owner
        """
        if email:
            user = User.objects.filter(username=email).first()
            if not user:
                return JsonResponse({'status': 'failed', 'message': 'invalid email'})
            restaurantOwner = ResturentOwner.objects.filter(profile=user).first()
        if phone:
            restaurantOwner = ResturentOwner.objects.filter(phone_number=phone).first()
            if not restaurantOwner:
                return JsonResponse({'status': 'failed', 'message': 'invalid phone number'})
            
        if not restaurantOwner:
            return JsonResponse({'status': 'failed', 'message': 'invalid credentials'})
        """
        sending a final response
        """
        return JsonResponse({'status': 'success', 'message': 'resturent owner logged in successfully', "data" : {
            "id": restaurantOwner.id,
            "username": restaurantOwner.profile.username,
            "email": restaurantOwner.profile.email,
            "phone": restaurantOwner.phone_number,
        }})

        
        

def create_otp():
    pass