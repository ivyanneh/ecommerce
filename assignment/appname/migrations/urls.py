from django.contrib import admin
from django.urls import path
from sales import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('customer/add/', views.add_customer, name='add_customer'),
    path('customer/<int:customer_id>/order/add/', views.add_order, name='add_order'),
]

