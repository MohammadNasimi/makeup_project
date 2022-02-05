from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from Agent.models import Agent, Weekend


class AgentCreateView(CreateView):
    model = Agent
    fields = ['first_name', 'last_name', 'descriptions', 'experience_year', 'count_service', 'image']
    template_name = 'Agent/create_Agent.html'
    success_url = reverse_lazy('Agent:create_Agent')


class WeekendCreateView(CreateView):
    model = Weekend
    fields = ['Agent', 'start_time', 'end_time']
    template_name = 'Agent/create_Weekend.html'
    success_url = reverse_lazy('Agent:create_weekend')
