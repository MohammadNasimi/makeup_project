from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model: Customer
        fields = ['first_name', 'last_name', 'email', 'Password']


class contactusForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Message = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
