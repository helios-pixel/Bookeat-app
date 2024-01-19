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
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        restaurant = data['restaurant']
        customer = data['customer']
        purchased_items = data['purchased_items']
        is_paid = data['is_paid']
        is_delivered = data['is_delivered']
        is_cancelled = data['is_cancelled']

        resturent = Resturent.objects.filter(id=restaurant).first()
        customer = Customer.objects.filter(id=customer).first()

        if resturent is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        if customer is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid customer'})
        
        customer_purchase = CustomerPurchase.objects.create(resturent=resturent, customer=customer, is_paid=is_paid, is_delivered=is_delivered, is_cancelled=is_cancelled)
        customer_purchase.save()

        for item in purchased_items:
            resturent_menu = ResturentMenu.objects.filter(id=item).first()
            if resturent_menu is None:
                return JsonResponse({'status': 'failed', 'message': 'invalid resturent menu'})
            customer_purchase.purchased_items.add(resturent_menu)

        return JsonResponse({'status': 'success', 'message': 'customer purchase created successfully', "data" : {
            "id": customer_purchase.id,
            "is_paid": customer_purchase.is_paid,
            "is_delivered": customer_purchase.is_delivered,
            "is_cancelled": customer_purchase.is_cancelled,
        }})

def create_customer_table_booking(request):
    pass

def get_resturent(request):
    if request.method == 'GET':
        resturent = Resturent.objects.all()
        if resturent is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        return JsonResponse({'status': 'success', 'message': 'resturent fetched successfully', "data" : {
            "id": resturent.id,
            "name": resturent.name,
            "address": resturent.address,
            "table": resturent.table,
            "is_active": resturent.is_active,
        }})

def get_resturent_menu(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        resturent = data['resturent']

        resturent = Resturent.objects.filter(id=resturent).first()

        if resturent is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        
        resturent_menu = ResturentMenu.objects.filter(resturent=resturent)
        if resturent_menu is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent menu'})
        return JsonResponse({'status': 'success', 'message': 'resturent menu fetched successfully', "data" : {
            "id": resturent_menu.id,
            "name": resturent_menu.name,
            "food_image": resturent_menu.food_image,
            "description": resturent_menu.description,
            "price": resturent_menu.price,
            "is_active": resturent_menu.is_active,
            "stock": resturent_menu.stock,
        }})

def get_resturent_table(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        resturent = data['resturent']

        resturent = Resturent.objects.filter(id=resturent).first()

        if resturent is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        
        resturent_table = ResturentTables.objects.filter(resturent=resturent)
        if resturent_table is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent table'})
        return JsonResponse({'status': 'success', 'message': 'resturent table fetched successfully', "data" : {
            "id": resturent_table.id,
            "table_number": resturent_table.table_number,
            "is_available": resturent_table.is_available,
        }})

def get_customer_purchase(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        customer = data['customer']

        customer = Customer.objects.filter(id=customer).first()

        if customer is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid customer'})
        
        customer_purchase = CustomerPurchase.objects.filter(customer=customer)
        if customer_purchase is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid customer purchase'})
        return JsonResponse({'status': 'success', 'message': 'customer purchase fetched successfully', "data" : {
            "id": customer_purchase.id,
            "is_paid": customer_purchase.is_paid,
            "is_delivered": customer_purchase.is_delivered,
            "is_cancelled": customer_purchase.is_cancelled,
        }})

def get_customer_table_booking(request):
    pass