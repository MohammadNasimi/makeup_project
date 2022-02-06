from django.db import models
from core.models import BaseModel
from Agent.models import Agent
from customer.models import Customer
from service.models import Service


# Create your models here.
class Booking(BaseModel):
    service = models.ForeignKey(Service, on_delete=models.RESTRICT, verbose_name='service')
    count_adult = models.PositiveIntegerField(default=0)
    count_child = models.PositiveIntegerField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    cost_final = models.PositiveIntegerField(default=0)
    agent = models.ForeignKey(Agent, on_delete=models.RESTRICT, verbose_name='Agent')
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, verbose_name='Customer')
