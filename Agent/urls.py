from django.urls import path

from . import views

app_name = 'Agent'
urlpatterns = [
    path('create_Agent/', views.AgentCreateView.as_view(), name='create_Agent'),
    path('list_agent/', views.AgentListView.as_view(), name='list_agent'),
    path('update_agent/<int:pk>', views.AgentUpdateView.as_view(), name='update_agent'),
    path('Delete_agent/<int:pk>', views.AgentDeleteView.as_view(), name='delete_agent'),
    path('create_weekend/', views.WeekendCreateView.as_view(), name='create_weekend'),
]