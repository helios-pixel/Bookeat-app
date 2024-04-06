from django.urls import path

from . import views

urlpatterns = [
    path('create_resturent/', views.create_resturent, name='create_resturent'),
    path('create_resturent_menu/', views.create_resturent_menu, name='create_resturent_menu'),
    path('create_resturent_table/', views.create_resturent_table, name='create_resturent_table'),
    path('create_customer_purchase/', views.create_customer_purchase, name='create_customer_purchase'),
    path('create_customer_table_booking/', views.create_customer_table_booking, name='create_customer_table_booking'),
    path('get_resturent/', views.get_resturent, name='get_resturent'),
    path('get_resturent_menu/', views.get_resturent_menu, name='get_resturent_menu'),
    path('get_resturent_table/', views.get_resturent_table, name='get_resturent_table'),
    path('get_customer_purchase/', views.get_customer_purchase, name='get_customer_purchase'),
    path("get_customer_purchase_for_owner/", views.get_customer_purchase_for_owner, name="get_customer_purchase_for_owner"),
    path('get_customer_table_booking/', views.get_customer_table_booking, name='get_customer_table_booking'),
    path('get_your_resturent/', views.get_your_restaurant, name='get_your_resturent'),
    path('update_resturent/', views.update_resturent, name='update_resturent'),
    path("get_your_resturent_details/", views.get_your_restaurant_details, name="get_your_resturent_details"),
    path("update_resturent_details/", views.update_restaurant_details, name="update_resturent_details"),
    path("get_table_amount/", views.get_table_amount, name="get_table_amount"),
    path("get_order_amount/", views.get_order_amount, name="get_order_amount"),
]