from django.http import JsonResponse
import json
from .models import *
from authApp.models import *
from django.views.decorators.csrf import csrf_exempt
import math
from django.conf import settings
import razorpay

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
        source = data['source']
        destination = data['destination']
        print(restaurantOwner, name, address, is_active, restaurant_image)

        restaurant_owner = ResturentOwner.objects.filter(id=restaurantOwner).first()

        if restaurant_owner is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid restaurant owner'})
        
        resturent = Resturent.objects.create(resturent_owner=restaurant_owner, name=name, address=address, is_active=is_active, resturent_image=restaurant_image, source=source, destination=destination)
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
        order_id = data['order_id']
        payment_id = data['payment_id']
        signature = data['signature']
        amount_paid = data['amount']
        restaurant = data['restaurant']
        customer = data['customer']
        menu_items = data['menu_items']
        is_paid = data['is_paid']
        time = data['time']

        resturent = Resturent.objects.filter(id=restaurant).first()
        customer = Customer.objects.filter(id=customer).first()

        if not resturent:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        if not customer:
            return JsonResponse({'status': 'failed', 'message': "customer doesn't exist"})
        
        purchase = CustomerOrderItem.objects.create(
            resturent = resturent,
            customer = customer,
            amount_paid = amount_paid/100,
            is_paid = is_paid,
            order_id = order_id,
            payment_id = payment_id,
            payment_signature = signature,
            time = time,
        )
        purchase.save()

        for item in menu_items:
            print(item)
            resturent_menu = ResturentFoodItem.objects.filter(id=item['id']).first()
            if not resturent_menu:
                return JsonResponse({'status': 'failed', 'message': 'invalid resturent menu'})
            purchase_details = CustomerOrderItemDetails.objects.create(order_item=purchase, food_item=resturent_menu, price=resturent_menu.price, quantity=item['quantity'])
            purchase_details.save()

        return JsonResponse({'status': 'success', 'message': 'customer purchase created successfully', "data" : {
            "id": purchase.id,
            "is_paid": purchase.is_paid,
            "order_id": purchase.order_id,
            "payment_id": purchase.payment_id,
            "amount_paid": purchase.amount_paid,
        }})
    return JsonResponse({'status': 'failed', 'message': 'invalid request'})
        

@csrf_exempt
def create_customer_table_booking(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        restaurant = data['restaurant']
        customer = data['customer']
        no_of_diners = data['no_of_diners']
        tables = data['tables']
        is_paid = data['is_paid']
        order_id = data['order_id']
        payment_id = data['payment_id']
        payment_signature = data['signature']
        amount_paid = data['amount']

        resturent = Resturent.objects.filter(id=restaurant).first()
        customer = Customer.objects.filter(id=customer).first()

        if not resturent:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        if not customer:
            return JsonResponse({'status': 'failed', 'message': "customer doesn't exist"})
        
        tables_available = ResturentTables.objects.filter(resturent=resturent, is_available=True).all()
        if not tables_available:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent table'})
        booking = CustomerTableBooking.objects.create(
            resturent = resturent,
            customer = customer,
            no_of_diners = no_of_diners,
            tables = tables,
            is_paid = is_paid,
            order_id = order_id,
            payment_id = payment_id,
            payment_signature = payment_signature,
            amount_paid = amount_paid/100,
        )
        booking.save()

        # update resturent table
        your_table_numbers = []
        if len(tables_available) >= int(tables):
            for i in range(0, int(tables)):
                if tables_available[i].is_available:
                    tables_available[i].is_available = False
                    tables_available[i].booked_by = customer    
                    tables_available[i].save()
                    your_table_numbers.append(tables_available[i].table_number)
                else:
                    continue
        else:
            print("else block")
            return JsonResponse({'status': 'failed', 'message': 'invalid no of tables'})

        booking.table_numbers = ",".join([str(i) for i in your_table_numbers])
        booking.save()
        print("here...")
        return JsonResponse({'status': 'success', 'message': 'customer table booking created successfully', "data" : {
            "id": booking.id,
            "is_paid": booking.is_paid,
            "order_id": booking.order_id,
            "payment_id": booking.payment_id,
            "amount_paid": booking.amount_paid,
            "no_of_diners": booking.no_of_diners,
            "tables": booking.tables,
            "your_booked_table_numbers" : booking.table_numbers
        }})
    return JsonResponse({'status': 'failed', 'message': 'invalid request'})

def get_resturent(request):
    if request.method == 'GET':
        resturent = Resturent.objects.all()
        if not resturent:
            return JsonResponse({'status': 'failed', 'message': 'No resturents found'})
        data = []
        for item in resturent:
            data.append({
                "id": item.id,
                "name": item.name,
                "address": item.address,
                "is_active": item.is_active,
                "owner": item.resturent_owner.profile.first_name + " " + item.resturent_owner.profile.last_name,
                "tables_available" : len(ResturentTables.objects.filter(resturent=item, is_available=True)),
                "source" : item.source,
                "destination" : item.destination,
            })
        return JsonResponse({'status': 'success', 'message': 'resturent fetched successfully', "data" : data})
    return JsonResponse({'status': 'failed', 'message': 'invalid request'})

@csrf_exempt
def get_resturent_menu(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        resturent = data['id']

        resturent = Resturent.objects.filter(id=resturent).first()
        if not resturent:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        
        resturent_menu = ResturentFoodItem.objects.filter(resturent=resturent).all()
        if not resturent_menu:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent menu'})
        
        list_menu = []
        for item in resturent_menu:
            list_menu.append({
                "id": item.id,
                "name": item.name,
                "description": item.description,
                "price": item.price,
                "is_active": item.is_active,
                "stock": item.stock,
            })

        return JsonResponse({'status': 'success', 'message': 'resturent menu fetched successfully', "data" : list_menu})
    return JsonResponse({'status': 'failed', 'message': 'invalid request'})

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
    return JsonResponse({'status': 'failed', 'message': 'invalid request'})

@csrf_exempt
def get_customer_purchase(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        customer = data['customer']

        customer = Customer.objects.filter(id=customer).first()

        if not customer:
            return JsonResponse({'status': 'failed', 'message': 'invalid customer'})
        
        customer_purchase = CustomerOrderItem.objects.filter(customer=customer).all()
        if not customer_purchase:
            return JsonResponse({'status': 'failed', 'message': 'No purchase found'})
        
        data = []
        for item in customer_purchase:
            data.append({
                "user_name": item.customer.profile.first_name + " " + item.customer.profile.last_name,
                "restaurant_name": item.resturent.name,
                "order_id": item.order_id,
                "amount_paid": item.amount_paid,
                "time" : item.time,
                "menu_items": [i.food_item.name for i in CustomerOrderItemDetails.objects.filter(order_item=item)],
                "quantity": [i.quantity for i in CustomerOrderItemDetails.objects.filter(order_item=item)],
            })

        return JsonResponse({'status': 'success', 'message': 'customer purchase fetched successfully', "data" : data})
    return JsonResponse({'status': 'failed', 'message': 'invalid request'})

@csrf_exempt
def get_customer_purchase_for_owner(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        restaurant_id = data['id']

        resturent = Resturent.objects.filter(id=restaurant_id).first()

        if not resturent:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        
        customer_purchase = CustomerOrderItem.objects.filter(resturent=resturent).all()
        if not customer_purchase:
            return JsonResponse({'status': 'failed', 'message': 'No purchase found'})
        
        data = []
        for item in customer_purchase:
            data.append({
                "user_name": item.customer.profile.first_name + " " + item.customer.profile.last_name,
                "restaurant_name": item.resturent.name,
                "order_id": item.order_id,
                "amount_paid": item.amount_paid,
                "time" : item.time,
                "menu_items": [i.food_item.name for i in CustomerOrderItemDetails.objects.filter(order_item=item)],
                "quantity": [i.quantity for i in CustomerOrderItemDetails.objects.filter(order_item=item)],
            })

        return JsonResponse({'status': 'success', 'message': 'customer purchase fetched successfully', "data" : data})
    return JsonResponse({'status': 'failed', 'message': 'invalid request'})
    
            

@csrf_exempt
def get_customer_table_booking(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        customer = data['customer']

        customer = Customer.objects.filter(id=customer).first()

        if not customer:
            return JsonResponse({'status': 'failed', 'message': 'invalid customer'})
        
        customer_table_booking = CustomerTableBooking.objects.filter(customer=customer).all()
        if not customer_table_booking:
            return JsonResponse({'status': 'failed', 'message': 'No table booking found'})
        
        my_table_booking = []
        tables = ResturentTables.objects.filter(booked_by=customer).all()
        print("tables are =============",tables)

        data = []
        for item in customer_table_booking:
            data.append({
                "user_name": item.customer.profile.first_name + " " + item.customer.profile.last_name,
                "restaurant_name": item.resturent.name,
                "no_of_diners": item.no_of_diners,
                "tables": item.tables,
                "is_paid": item.is_paid,
                "order_id": item.order_id,
                "amount_paid": item.amount_paid,
                "your_booked_table_numbers" : item.table_numbers.split(","),
            })
        
        return JsonResponse({'status': 'success', 'message': 'customer table booking fetched successfully', "data" : data })
    return JsonResponse({'status': 'failed', 'message': 'invalid request'})


@csrf_exempt
def get_your_restaurant(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        resturent_owner = data['id']

        resturent_owner = ResturentOwner.objects.filter(id=resturent_owner).first()

        if resturent_owner is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent owner'})
        
        resturent = Resturent.objects.filter(resturent_owner=resturent_owner).all()
        if not resturent:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        list_resturent = []
        for item in resturent:
            print(item.resturent_image)
            list_resturent.append({
                "id": item.id,
                "name": item.name,
                "address": item.address,
                "is_active": item.is_active,
                # "resturent_image": item.resturent_image,
                "owner" : item.resturent_owner.profile.first_name + " " + item.resturent_owner.profile.last_name, 
                "tables_available": len(ResturentTables.objects.filter(resturent=item, is_available=True)),
            })
        return JsonResponse({'status': 'success', 'message': 'resturent fetched successfully', "data" : list_resturent})
    return JsonResponse({'status': 'failed', 'message': 'invalid request'})

@csrf_exempt
def update_resturent(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        uid = data['uid']
        restaurant_id = data['id']
        name = data['name']
        address = data['address']
        is_active = data['is_active']
        menu_items = data['menu_items']
        tables = data['tables']

        resturent_owner = ResturentOwner.objects.filter(id=uid).first()

        if resturent_owner is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent owner'})
        
        resturent = Resturent.objects.filter(id=restaurant_id).first()

        if resturent is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        
        if resturent_owner != resturent.resturent_owner:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent owner'})
        
        resturent.name = name
        resturent.address = address
        resturent.is_active = is_active
        resturent.save()

        for item in menu_items:
            if item["name"] != "" and item["price"] != "" and item["stock"] != "":
                # check if the same restaurant have the same item then do not update it
                resturent_menu = ResturentFoodItem.objects.filter(resturent=resturent, name=item['name']).first()
                if resturent_menu is None:
                    resturent_menu = ResturentFoodItem.objects.create(resturent=resturent, name=item['name'], food_image=item['image'], description="", price=item['price'], is_active=True, stock=item['stock']) 
                    resturent_menu.save()  
                # else update the item
                else:
                    resturent_menu.food_image = item['image']
                    resturent_menu.price = item['price']
                    resturent_menu.stock = item['stock']
                    resturent_menu.save() 

        if tables != '0' and tables != 0 and tables != '':
            for i in range(1, int(tables)+1):
                resturent_table = ResturentTables.objects.create(resturent=resturent, table_number=len(ResturentTables.objects.filter(resturent=resturent))+1, is_available=True)
                resturent_table.save()
                

        return JsonResponse({'status': 'success', 'message': 'resturent updated successfully'})
    return JsonResponse({'status': 'failed', 'message': 'invalid request'})

@csrf_exempt
def get_your_restaurant_details(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        uid = data['uid']
        restaurant_id = data['id']

        resturent_owner = ResturentOwner.objects.filter(id=uid).first()

        if resturent_owner is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent owner'})
        
        resturent = Resturent.objects.filter(id=restaurant_id).first()

        if resturent is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        
        if resturent_owner != resturent.resturent_owner:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent owner'})
        
        resturent_menu = ResturentFoodItem.objects.filter(resturent=resturent)
        resturent_table = ResturentTables.objects.filter(resturent=resturent)

        list_menu = []
        for item in resturent_menu:
            list_menu.append({
                "id": item.id,
                "name": item.name,
                "description": item.description,
                "price": item.price,
                "is_active": item.is_active,
                "stock": item.stock,
            })
        
        list_table = []
        for item in resturent_table:
            if item.booked_by:
                list_table.append({
                    "id": item.id,
                    "table_number": item.table_number,
                    "is_available": item.is_available,
                    "booked_by": item.booked_by.profile.first_name + " " + item.booked_by.profile.last_name,
                })
            else:
                list_table.append({
                    "id": item.id,
                    "table_number": item.table_number,
                    "is_available": item.is_available,
                    "booked_by": False,
                })
        
        return JsonResponse({'status': 'success', 'message': 'resturent details fetched successfully', "data" : {
            "id": resturent.id,
            "name": resturent.name,
            "address": resturent.address,
            "is_active": resturent.is_active,
            "menu_items": list_menu,
            "tables": list_table,
        }})
    return JsonResponse({'status': 'failed', 'message': 'invalid request'})

@csrf_exempt
def update_restaurant_details(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        uid = data['uid']
        restaurant_id = data['id']
        name = data['name']
        address = data['address']
        is_active = data['is_active']
        menu_items = data['menu_items']
        table_status = data['table_status']

        resturent_owner = ResturentOwner.objects.filter(id=uid).first()

        if resturent_owner is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent owner'})
        
        resturent = Resturent.objects.filter(id=restaurant_id).first()

        if resturent is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        
        if resturent_owner != resturent.resturent_owner:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent owner'})
        
        resturent.name = name
        resturent.address = address
        resturent.is_active = is_active
        resturent.save()

        for item in menu_items:
            resturent_menu = ResturentFoodItem.objects.filter(id=item['id']).first()
            if resturent_menu is None:
                return JsonResponse({'status': 'failed', 'message': 'invalid resturent menu'})
            resturent_menu.name = item['name']
            resturent_menu.food_image = item['image']
            resturent_menu.price = item['price']
            resturent_menu.stock = item['stock']
            resturent_menu.save()

        for item in table_status:
            resturent_table = ResturentTables.objects.filter(table_number=item['table_number']).first()
            if resturent_table is None:
                return JsonResponse({'status': 'failed', 'message': 'invalid resturent table'})
            resturent_table.is_available = item['is_available']
            if item['is_available']:
                resturent_table.booked_by = None
            resturent_table.save()

        return JsonResponse({'status': 'success', 'message': 'resturent updated successfully'})
    return JsonResponse({'status': 'failed', 'message': 'invalid request'})
        

@csrf_exempt
def get_table_amount(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        resturent = data['resturent']
        no_of_people = int(data['no_of_diners'])
        no_of_table = int(data['tables'])
        max_capacity = 4
        per_table_price = 100

        resturent = Resturent.objects.filter(id=resturent).first()
        if resturent is None:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        
        no_of_table_should_be = math.ceil(no_of_people / max_capacity)
        if no_of_table_should_be > no_of_table:
            return JsonResponse({'status': 'failed', 'message': 'invalid no of table'})
        
        resturent_table = ResturentTables.objects.filter(resturent=resturent, is_available=True).all()
        if not resturent_table:
            return JsonResponse({'status': 'failed', 'message': 'Resturent table not available'})
        
        if len(resturent_table) < no_of_table:
            return JsonResponse({'status': 'failed', 'message': 'Resturent table not available'})
        
        amount = no_of_table * per_table_price
        key_id = settings.KEY_ID

        # creating order 

        client = razorpay.Client(auth=(settings.KEY_ID, settings.KEY_SECRET))
        DATA = {
            "amount": amount*100,
            "currency": "INR",
        }

        response = client.order.create(data=DATA)

        return JsonResponse({'status': 'success', 'message': 'Amount calculated successfully', "data" : {
            "amount": response.get("amount"),
            "key_id": key_id,
            "order_id" : response.get("id")
        }})
    return JsonResponse({'status': 'failed', 'message': 'invalid request'})

@csrf_exempt
def get_order_amount(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        resturent = data['resturent']
        menu_ids = data['menu_items_ids']

        resturent = Resturent.objects.filter(id=resturent).first()
        if not resturent:
            return JsonResponse({'status': 'failed', 'message': 'invalid resturent'})
        
        print("menu_ids are =============",menu_ids)
        # menu_ids are ============= [{'id': '26', 'quantity': '3'}]

        # menu_items = ResturentFoodItem.objects.filter(id__in=menu_ids.keys()).all()
        menu_items = []
        for item in menu_ids:
            menu_item = ResturentFoodItem.objects.filter(id=item['id']).first()
            if not menu_item:
                return JsonResponse({'status': 'failed', 'message': 'invalid menu items'})
            menu_items.append(menu_item)
        print("menu_items are =============",menu_items)
        if not menu_items:
            return JsonResponse({'status': 'failed', 'message': 'invalid menu items'})
        
        # menu_ids are ============= [{'id': '27', 'quantity': '4'}]
        # menu_items are ============= [<ResturentFoodItem: Dal mkhi>]

        amount = 0
        for item in menu_items:
            amount += item.price * int(menu_ids[menu_items.index(item)]['quantity'])

        key_id = settings.KEY_ID
        
        # creating order
        client = razorpay.Client(auth=(settings.KEY_ID, settings.KEY_SECRET))
        DATA = {
            "amount": amount*100,
            "currency": "INR",
        }

        response = client.order.create(data=DATA)

        return JsonResponse({'status': 'success', 'message': 'Amount calculated successfully', "data" : {
            "amount": response.get("amount"),
            "key_id": key_id,
            "order_id" : response.get("id")
        }})
    return JsonResponse({'status': 'failed', 'message': 'invalid request'})