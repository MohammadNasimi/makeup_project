from django import forms
from models import Service


class CustomerForm(forms.ModelForm):
    class Meta:
        model: Service
        fields = ['name', 'time', 'cost']