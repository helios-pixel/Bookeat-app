from django.http import JsonResponse
import json
from .models import *
from authApp.models import *
# import csrf_exmepy
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def create_resturent(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        restaurantOwner = data['id']
        name = data['name']
        address = data['address']
        is_active = data['is_active']
        restaurant_image = data['restaurant_image']
        print(restaurantOwner, name, address, is_active, restaurant_image)

        restaurant_owner = ResturentOwner.objects.filter(id=restaurantOwner).first()

        if restaurant_owner is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid restaurant owner'})
        
        resturent = Resturent.objects.create(resturent_owner=restaurant_owner, name=name, address=address, is_active=is_active, resturent_image=restaurant_image);
        resturent.save()

        return JsonResponse({'status': 'success', 'message': 'resturent created successfully', "data" : {
            "id": resturent.id,
            "name": resturent.name,
            "address": resturent.address,
            "is_active": resturent.is_active,
        }})

@csrf_exempt
def create_resturent_menu(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        resturent_user = data['resturent_userId']
        resturent = data['resturentId']
        name = data['name']
        food_image = data['food_image']
        description = data['description']
        price = float(data['price'])
        is_active = data['is_active']
        stock = int(data['stock'])

        resturent_user_obj = ResturentOwner.objects.filter(id=resturent_user).first()
        if resturent_user_obj is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid user'})

        resturent = Resturent.objects.filter(id=resturent).first()

        if resturent is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        
        if resturent_user_obj != resturent.resturent_owner:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent user'})
        
        resturent_menu = ResturentFoodItem.objects.create(resturent=resturent, name=name, food_image=food_image, description=description, price=price, is_active=is_active, stock=stock)
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

@csrf_exempt
def create_resturent_table(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        resturent_user = data['resturent_userId']
        resturent = data['resturent']
        table_number = int(data['table_number'])
        is_available = data['is_available']

        resturent_user_obj = ResturentOwner.objects.filter(id=resturent_user).first()

        if resturent_user_obj is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid user'})

        resturent = Resturent.objects.filter(id=resturent).first()

        if resturent is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})

        if resturent_user_obj != resturent.resturent_owner:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent user'})
        
        resturent_table = ResturentTables.objects.create(resturent=resturent, table_number=table_number, is_available=is_available)
        resturent_table.save()

        return JsonResponse({'status': 'success', 'message': 'resturent table created successfully', "data" : {
            "id": resturent_table.id,
            "table_number": resturent_table.table_number,
            "is_available": resturent_table.is_available,
        }})

@csrf_exempt
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
            resturent_menu = ResturentFoodItem.objects.filter(id=item).first()
            if resturent_menu is None:
                return JsonResponse({'status': 'failed', 'message': 'invalid resturent menu'})
            customer_purchase.purchased_items.add(resturent_menu)

        return JsonResponse({'status': 'success', 'message': 'customer purchase created successfully', "data" : {
            "id": customer_purchase.id,
            "is_paid": customer_purchase.is_paid,
            "is_delivered": customer_purchase.is_delivered,
            "is_cancelled": customer_purchase.is_cancelled,
        }})

@csrf_exempt
def create_customer_table_booking(request):
    pass

def get_resturent(request):
    if request.method == 'GET':
        resturent = Resturent.objects.all()
        if resturent is None:
            return JsonResponse({'status': 'failed', 'message': 'No resturents found'})
        data = []
        for item in resturent:
            data.append({
                "id": item.id,
                "name": item.name,
                "address": item.address,
                "table": item.table,
                "is_active": item.is_active,
            })
        return JsonResponse({'status': 'success', 'message': 'resturent fetched successfully', "data" : data})

@csrf_exempt
def get_resturent_menu(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        resturent = data['resturent']

        resturent = Resturent.objects.filter(id=resturent).first()

        if resturent is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        
        resturent_menu = ResturentFoodItem.objects.filter(resturent=resturent)
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
def get_customer_table_booking(request):
    pass


@csrf_exempt
def get_your_restaurant(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        resturent_owner = data['id']

        resturent_owner = ResturentOwner.objects.filter(id=resturent_owner).first()

        if resturent_owner is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent owner'})
        
        resturent = Resturent.objects.filter(resturent_owner=resturent_owner).all()
        list_resturent = []
        for item in resturent:
            print(item.resturent_image)
            list_resturent.append({
                "id": item.id,
                "name": item.name,
                "address": item.address,
                "is_active": item.is_active,
                "resturent_image": item.resturent_image,
            })
        if resturent is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        return JsonResponse({'status': 'success', 'message': 'resturent fetched successfully', "data" : list_resturent})