from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from customer.models import Customer


class CustomerCreateView(CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'email', 'Password']
    template_name = 'customer/create_customer.html'
    success_url = reverse_lazy('customer:create')


class CustomerListView(ListView):
    model = Customer
    fields = ['first_name', 'last_name', 'email', 'Password']
    template_name = 'customer/list_customer.html'


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['first_name', 'last_name', 'email', 'Password']
    template_name = 'customer/update_customer.html'
    success_url = reverse_lazy('customer:list')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer/delete_customer.html'
    success_url = reverse_lazy('customer:list')
