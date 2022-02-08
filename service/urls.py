from django.urls import path

from . import views

app_name = 'service'
urlpatterns = [
    path('create/', views.ServiceCreateView.as_view(), name='create'),
    path('list/', views.ServiceListView.as_view(), name='list'),
    path('update/<int:pk>', views.ServiceUpdateView.as_view(), name='update'),
    path('Delete/<int:pk>', views.ServiceDeleteView.as_view(), name='delete'),
]