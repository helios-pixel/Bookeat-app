from django.db import models
from base.models import BaseModel
from authApp.models import ResturentOwner, Customer

# Create your models here.

class Resturent(BaseModel):
    resturent_owner = models.ForeignKey(ResturentOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    resturent_image = models.ImageField(upload_to='resturent_images/', blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.resturent_owner.profile.first_name + " " + self.resturent_owner.profile.last_name + " " + self.resturent_owner.phone_number
    
class ResturentFoodItem(BaseModel):
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    stock = models.IntegerField(default=0)
    food_image = models.ImageField(upload_to='food_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    

class ResturentTables(BaseModel):
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE)
    table_number = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.table_number)
    
    def __save__(self, *args, **kwargs):
        table_number = ResturentTables.objects.filter(resturent=self.resturent).count() + 1
        self.table_number = table_number
        super(ResturentTables, self).save(*args, **kwargs)


class CustomerPurchase(BaseModel):
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.profile.email
    
class CustomerOrderItem(BaseModel):
    food_item = models.ForeignKey(ResturentFoodItem, on_delete=models.CASCADE)
    customer_purchase = models.ForeignKey(CustomerPurchase, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
class CustomerTableBooking(BaseModel):
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(ResturentTables, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.profile.first_name + " " + self.customer.profile.last_name + " " + self.table.table_number
