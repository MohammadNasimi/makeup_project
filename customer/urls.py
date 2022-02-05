from django.urls import path

from . import views

app_name = 'customer'
urlpatterns = [
    path('create/', views.CustomerCreateView.as_view(), name='create'),
]