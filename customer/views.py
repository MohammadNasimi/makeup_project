from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from customer.models import Customer


class CustomerCreateView(CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'email', 'Password']
    template_name = 'customer/create_customer.html'
