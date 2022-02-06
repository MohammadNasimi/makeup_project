from django import forms
from models import Agent, Weekend


class AgentForm(forms.ModelForm):
    class Meta:
        model: Agent
        fields = ['first_name', 'last_name', 'descriptions', 'experience_year', 'count_service', 'image']
        labels = {
            'first_name': 'name'
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={'name': 'first_name', 'class': 'bg-info  justify-content-center form-control',
                       'id': 'name_id'}, ),
            'last_name': forms.TextInput(
                attrs={'name': 'last_name', 'class': 'bg-info  justify-content-center form-control',
                       'id': 'name_id'}, ),
            'descriptions': forms.TextInput(
                attrs={'name': 'descriptions', 'class': 'bg-info  justify-content-center form-control',
                       'id': 'name_id'}, ),
            'experience_year': forms.NumberInput(
                attrs={'name': 'experience_year',
                       'class': 'bg-info  justify-content-center form-control',
                       'id': 'name_id'}, ),
            'count_service': forms.NumberInput(
                attrs={'name': 'name_id',
                       'class': 'bg-info  justify-content-center form-control',
                       'id': 'name_id'}, ),
            'Image': forms.FileInput(
                attrs={'name': 'Image', 'class': 'bg-info  justify-content-center form-control',
                       'id': 'name_id'}, ),
        }


class WeekendForm(forms.ModelForm):
    class Meta:
        model: Weekend
        fields = ['Agent', 'start_time', 'end_time']

        widgets = {
            'Agent': forms.TextInput(
                attrs={'name': 'Agent', 'class': 'bg-warning  justify-content-center form-control'}, ),
            'start_time': forms.DateInput(
                attrs={'type': 'date', 'name': 'start_time', 'class': 'bg-warning  justify-content-center form-control',
                       'id': 'name_id'}, ),
            'end_time': forms.DateInput(
                attrs={'type': 'date', 'name': 'end_time', 'class': 'bg-warning  justify-content-center form-control',
                       'id': 'name_id'}, ),
        }
