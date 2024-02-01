from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register((Resturent, ResturentFoodItem , ResturentTables, CustomerOrderItem , CustomerTableBooking, CustomerOrderItemDetails))
