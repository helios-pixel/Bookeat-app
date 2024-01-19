from django.db import models
from base.models import BaseModel
from authApp.models import ResturentOwner, Customer

# Create your models here.

class Resturent(BaseModel):
    resturent_owner = models.ForeignKey(ResturentOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    table = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class ResturentMenu(BaseModel):
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    food_image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class ResturentTables(BaseModel):
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE)
    table_number = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.table_number)


class CustomerPurchase(BaseModel):
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    purchased_items = models.ManyToManyField(ResturentMenu)
    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.profile.email
    
class CustomerTableBooking(BaseModel):
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(ResturentTables, on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.profile.email
