from django import forms
from .models import Customer, Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_date', 'total_amount']
