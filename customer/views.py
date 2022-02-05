from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from customer.models import Customer


class CustomerCreateView(CreateView):
    model = Customer
    fields = '__all__'
