from django.contrib import admin
from .models import Resturent, ResturentMenu, ResturentTables, CustomerPurchase, CustomerTableBooking

# Register your models here.

admin.site.register((Resturent, ResturentMenu, ResturentTables, CustomerPurchase, CustomerTableBooking))
