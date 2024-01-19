from django.contrib import admin
from .models import Customer, ResturentOwner

# Register your models here.

admin.site.register((Customer, ResturentOwner))
