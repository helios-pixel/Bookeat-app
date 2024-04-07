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
    source = models.CharField(max_length=100, blank=True, null=True)
    destination = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        revenue_generated = 0
        from_table_booking = CustomerTableBooking.objects.filter(resturent=self)
        if from_table_booking:
            for table_booking in from_table_booking:
                revenue_generated += table_booking.amount_paid
        from_order_item = CustomerOrderItem.objects.filter(resturent=self)
        if from_order_item:
            for order_item in from_order_item:
                revenue_generated += order_item.amount_paid
        return self.name + " " + self.resturent_owner.profile.first_name + " " + self.resturent_owner.profile.last_name + " " + self.resturent_owner.phone_number + ", Revenue generated : ₹ " + str(revenue_generated)+"/-"
    
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
    booked_by = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.table_number) + "th table of " + self.resturent.name + " - Booked" if not self.is_available else str(self.table_number) + "th table of " + self.resturent.name + " - Available"
    
    def __save__(self, *args, **kwargs):
        table_number = ResturentTables.objects.filter(resturent=self.resturent).count() + 1
        self.table_number = table_number
        super(ResturentTables, self).save(*args, **kwargs)
    
class CustomerOrderItem(BaseModel):
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    time = models.CharField(max_length=100, blank=True, null=True)
    amount_paid = models.FloatField(default=0)
    is_paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    payment_signature = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.customer.profile.first_name + " " + self.customer.profile.last_name + " " + self.resturent.name
    
class CustomerOrderItemDetails(BaseModel):
    order_item = models.ForeignKey(CustomerOrderItem, on_delete=models.CASCADE)
    food_item = models.ForeignKey(ResturentFoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.order_item.customer.profile.first_name + " " + self.order_item.customer.profile.last_name + " " + self.food_item.name
    
class CustomerTableBooking(BaseModel):
    resturent = models.ForeignKey(Resturent, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    payment_signature = models.CharField(max_length=100, blank=True, null=True)
    amount_paid = models.FloatField(default=0)
    no_of_diners = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    tables = models.IntegerField(default=0)
    table_numbers = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.customer.profile.first_name + " " + self.customer.profile.last_name + " " + self.table_numbers if self.table_numbers else "Table Booking"
