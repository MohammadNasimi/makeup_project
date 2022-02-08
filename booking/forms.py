from django import forms
from booking.models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model: Booking
        fields = ['service', 'count_adult', 'count_child', 'start_time', 'agent', 'customer']
