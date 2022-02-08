from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from service.models import Service


class ServiceCreateView(CreateView):
    model = Service
    fields = ['name', 'time', 'cost']
    template_name = 'Service/create_Service.html'
    success_url = reverse_lazy('service:create')


class ServiceListView(ListView):
    model = Service
    fields = ['name', 'time', 'cost']
    template_name = 'Service/list_Service.html'


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['name', 'time', 'cost']
    template_name = 'Service/update_Service.html'
    success_url = reverse_lazy('service:list')


class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'Service/delete_Service.html'
    success_url = reverse_lazy('service:list')
