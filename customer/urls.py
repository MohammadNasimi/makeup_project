from django.urls import path

from . import views

app_name = 'customer'
urlpatterns = [
    path('create/', views.CustomerCreateView.as_view(), name='create'),
    path('list/', views.CustomerListView.as_view(), name='list'),
    path('update/<int:pk>', views.CustomerUpdateView.as_view(), name='update'),
    path('Delete/<int:pk>', views.CustomerDeleteView.as_view(), name='delete'),
    path('m_create/', views.create_message, name='m_create'),
    path('contact_us/', views.ContactusView.as_view(), name='contact'),
    path('r_create/', views.view_message, name='r_create'),
]
