from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from booking.models import Booking


# Create your views here.
class BookingCreateView(CreateView):
    model = Booking
    fields = ['service', 'count_adult', 'count_child', 'start_time', 'agent', 'customer']
    template_name = 'Booking/create_booking.html'
    success_url = reverse_lazy('booking:create_booking')
