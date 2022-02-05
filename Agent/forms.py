from django import forms
from models import Agent, Weekend


class AgentForm(forms.ModelForm):
    class Meta:
        model: Agent
        fields = ['first_name', 'last_name', 'descriptions', 'experience_year', 'count_service', 'image']


class WeekendForm(forms.ModelForm):
    class Meta:
        model: Weekend
        fields = ['Agent', 'start_time', 'end_time']
