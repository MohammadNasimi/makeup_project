from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from Agent.models import Agent, Weekend


class AgentCreateView(CreateView):
    model = Agent
    fields = ['first_name', 'last_name', 'descriptions', 'experience_year', 'count_service', 'image']
    template_name = 'Agent/create_Agent.html'
    success_url = reverse_lazy('Agent:create_Agent')


class AgentListView(ListView):
    model = Agent
    fields = ['first_name', 'last_name', 'descriptions', 'experience_year', 'count_service', 'image']
    template_name = 'Agent/list_agent.html'


class AgentUpdateView(UpdateView):
    model = Agent
    fields = ['first_name', 'last_name', 'descriptions', 'experience_year', 'count_service', 'image']
    template_name = 'Agent/update_agent.html'
    success_url = reverse_lazy('Agent:list_agent')


class AgentDeleteView(DeleteView):
    model = Agent
    template_name = 'Agent/delete_agent.html'
    success_url = reverse_lazy('Agent:list_agent')


class WeekendCreateView(CreateView):
    model = Weekend
    fields = ['Agent', 'start_time', 'end_time']
    template_name = 'Agent/create_Weekend.html'
    success_url = reverse_lazy('Agent:create_weekend')


class WeekendListView(ListView):
    model = Weekend
    fields = ['Agent', 'start_time', 'end_time']
    template_name = 'Agent/list_weekend.html'


class WeekendUpdateView(UpdateView):
    model = Weekend
    fields = ['Agent', 'start_time', 'end_time']
    template_name = 'Agent/update_weekend.html'
    success_url = reverse_lazy('Agent:list_weekend')


class WeekendDeleteView(DeleteView):
    model = Weekend
    template_name = 'Agent/delete_weekend.html'
    success_url = reverse_lazy('Agent:delete_weekend')
