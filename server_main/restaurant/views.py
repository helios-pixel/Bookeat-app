from django.http import JsonResponse
import json
from .models import Resturent, ResturentMenu, ResturentTables, CustomerPurchase, CustomerTableBooking
from authApp.models import ResturentOwner, Customer

# Create your views here.


def create_resturent(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        restaurantOwner = data['restaurantOwner']
        name = data['name']
        address = data['address']
        table = int(data['table'])
        is_active = data['is_active']

        restaurant_owner = ResturentOwner.objects.filter(id=restaurantOwner).first()

        if restaurant_owner is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid restaurant owner'})
        
        resturent = Resturent.objects.create(resturent_owner=restaurant_owner, name=name, address=address, table=table, is_active=is_active)
        resturent.save()

        return JsonResponse({'status': 'success', 'message': 'resturent created successfully', "data" : {
            "id": resturent.id,
            "name": resturent.name,
            "address": resturent.address,
            "table": resturent.table,
            "is_active": resturent.is_active,
        }})


def create_resturent_menu(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        resturent = data['resturent']
        name = data['name']
        food_image = data['food_image']
        description = data['description']
        price = float(data['price'])
        is_active = data['is_active']
        stock = int(data['stock'])

        resturent = Resturent.objects.filter(id=resturent).first()

        if resturent is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        
        resturent_menu = ResturentMenu.objects.create(resturent=resturent, name=name, food_image=food_image, description=description, price=price, is_active=is_active, stock=stock)
        resturent_menu.save()

        return JsonResponse({'status': 'success', 'message': 'resturent menu created successfully', "data" : {
            "id": resturent_menu.id,
            "name": resturent_menu.name,
            "food_image": resturent_menu.food_image,
            "description": resturent_menu.description,
            "price": resturent_menu.price,
            "is_active": resturent_menu.is_active,
            "stock": resturent_menu.stock,
        }})

def create_resturent_table(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        resturent = data['resturent']
        table_number = int(data['table_number'])
        is_available = data['is_available']

        resturent = Resturent.objects.filter(id=resturent).first()

        if resturent is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        
        resturent_table = ResturentTables.objects.create(resturent=resturent, table_number=table_number, is_available=is_available)
        resturent_table.save()

        return JsonResponse({'status': 'success', 'message': 'resturent table created successfully', "data" : {
            "id": resturent_table.id,
            "table_number": resturent_table.table_number,
            "is_available": resturent_table.is_available,
        }})

def create_customer_purchase(request):
    pass

def create_customer_table_booking(request):
    pass

def get_resturent(request):
    pass

def get_resturent_menu(request):
    pass

def get_resturent_table(request):
    pass

def get_customer_purchase(request):
    pass

def get_customer_table_booking(request):
    pass