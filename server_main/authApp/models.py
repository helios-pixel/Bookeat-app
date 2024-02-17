from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.


"""
there are 3 users in the system:
1. admin
2. resturent owner
3. customer
"""

"""
creation of customer model
"""

class Customer(BaseModel):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    is_otp_verified = models.BooleanField(default=False)
    address = models.TextField(blank=True, null=True)
    otp = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return self.phone_number + " - " + self.profile.first_name + " " + self.profile.last_name
    
    
"""
creation of resturent owner model
"""

class ResturentOwner(BaseModel):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    is_otp_verified = models.BooleanField(default=False)
    otp  = models.CharField(max_length=6, blank=True, null=True)
    license_num = models.CharField(max_length=100, blank=True, null=True)
    pan = models.CharField(max_length=100, blank=True, null=True)
    gstin = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.phone_number + " - " + self.profile.first_name + " " + self.profile.last_name
    
