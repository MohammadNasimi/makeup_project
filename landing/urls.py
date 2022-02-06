from django.urls import path

from . import views

app_name = 'landing'
urlpatterns = [
    path('', views.HomeView.as_view(), name='Home'),
    path('contact_us/', views.ContactusView.as_view(), name='contact_us'),
    path('about_us/', views.AboutView.as_view(), name='about_us'),
]