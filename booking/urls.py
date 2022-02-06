from django.urls import path

from . import views

app_name = 'Booking'
urlpatterns = [
    path('create_booking/', views.BookingCreateView.as_view(), name='create_booking'),
]