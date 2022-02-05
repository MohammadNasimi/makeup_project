from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from customer.models import Customer


class ServiceCreateView(CreateView):
    model = Customer
    fields = ['name', 'time', 'cost']
    template_name = 'customer/create_customer.html'
    success_url = reverse_lazy('customer:create')
