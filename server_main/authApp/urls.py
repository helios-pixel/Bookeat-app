from django.urls import path

from . import views

urlpatterns = [
    path('create_customer/', views.create_customer, name='create_customer'),
    path('create_resturent_owner/', views.create_resturent_owner, name='create_resturent_owner'),
    path('customer_login/', views.customerLogin, name='customer_login'),
    path('resturent_owner_login/', views.restaurantOwnerLogin, name='resturent_owner_login'),
]