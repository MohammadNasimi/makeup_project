from django.db import models
from core.models import BaseModel
from Agent.models import Agent
from customer.models import Customer
from service.models import Service


# Create your models here.
class Booking(BaseModel):
    service = models.ForeignKey('Service', on_delete=models.SET_NULL, verbose_name='service')
    Agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, verbose_name='Agent')
    Customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, verbose_name='Customer')
    count_adult = models.PositiveIntegerField(default=0)
    count_child = models.PositiveIntegerField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    cost_final = models.PositiveIntegerField(default=0)
