from django.urls import path

from . import views

app_name = 'customer'
urlpatterns = [
    path('create/', views.CustomerCreateView.as_view(), name='create'),
    path('list/', views.CustomerListView.as_view(), name='list'),
    path('update/<int:pk>', views.CustomerUpdateView.as_view(), name='update'),
    path('Delete/<int:pk>', views.CustomerDeleteView.as_view(), name='delete'),
]