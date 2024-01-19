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
    path('get_customer_table_booking/', views.get_customer_table_booking, name='get_customer_table_booking'),
]