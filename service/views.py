from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from service.models import Service


class ServiceCreateView(CreateView):
    model = Service
    fields = ['name', 'time', 'cost']
    template_name = 'Service/create_Service.html'
    success_url = reverse_lazy('service:create')
