from django import forms
from booking.models import Booking


# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['service', 'count_adult', 'count_child', 'start_time', 'Agent']
class BookingForm(forms.Form):
    service = forms.IntegerField(label='service', widget=forms.Select(attrs={'id': 'id_service'}))
    adult_count = forms.IntegerField(label='Adult', initial=0, widget=forms.NumberInput(attrs={'min': '0'}))
    child_count = forms.IntegerField(label='Child', initial=0, widget=forms.NumberInput(attrs={'min': '0'}))
    start_time = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}, format='%Y-%m-%d'))
    Agent = forms.IntegerField(label='agent', widget=forms.Select(attrs={'id': 'id_agent'}))
