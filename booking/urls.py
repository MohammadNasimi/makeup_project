from django.urls import path

from . import views

app_name = 'Booking'
urlpatterns = [
    path('create_booking/', views.BookingView.as_view(), name='create_booking'),
    path('list_booking/', views.BookingListView.as_view(), name='list_booking'),
]