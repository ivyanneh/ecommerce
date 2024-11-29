from django.http import HttpResponse

def home(request):
    return HttpResponse("I am doing cat 2!")

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Customer, Order
from .forms import CustomerForm, OrderForm

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = customer.orders.all()
    return render(request, 'customer_detail.html', {'customer': customer, 'orders': orders})

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customer_list'))
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

def add_order(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = customer
            order.save()
            return HttpResponseRedirect(reverse('customer_detail', args=[customer.id]))
    else:
        form = OrderForm()
    return render(request, 'add_order.html', {'form': form, 'customer': customer})

