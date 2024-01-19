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

    def __str__(self):
        return self.profile.email
    
    
"""
creation of resturent owner model
"""

class ResturentOwner(BaseModel):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    is_otp_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.profile.email
    
