from django.contrib import admin
from .models import Customer, Order

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email','phone_number','address')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date','payment_method','payment_status','shipping_address')
    list_filter = ('order_date',)
    search_fields = ('customer__name',)

# Alternatively, you can register the models using admin.site.register
# admin.site.register(Customer, CustomerAdmin)
# admin.site.register(Order, OrderAdmin)





# Register your models here.
