from django.urls import path

from . import views

app_name = 'Agent'
urlpatterns = [
    path('create_Agent/', views.AgentCreateView.as_view(), name='create_Agent'),
    path('create_weekend/', views.WeekendCreateView.as_view(), name='create_weekend'),
]