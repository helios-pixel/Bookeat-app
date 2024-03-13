from django.urls import path

from . import views

urlpatterns = [
    path('create_customer/', views.create_customer, name='create_customer'),
    path('create_resturent_owner/', views.create_resturent_owner, name='create_resturent_owner'),
    path('customer_login/', views.customerLogin, name='customer_login'),
    path('resturent_owner_login/', views.restaurantOwnerLogin, name='resturent_owner_login'),
    path('customer_otp_verify/', views.verify_otp, name='customer_otp_verify'),
    path("update_customer/", views.update_customer, name="update_customer"),
    path("forgot_password/", views.forgot_password, name="forgot_password"),
    path("validate_otp/", views.validate_otp, name="reset_password"),
    path("reset_password/", views.reset_password, name="reset_password"),
]