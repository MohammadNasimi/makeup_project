from django.db import models
from core.models import BaseModel
from Agent.models import Agent
from customer.models import Customer
from service.models import Service


# Create your models here.
class Booking(BaseModel):
    service = models.ForeignKey(Service, on_delete=models.RESTRICT)
    count_adult = models.PositiveIntegerField(default=0)
    count_child = models.PositiveIntegerField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    cost_final = models.PositiveIntegerField(default=0)
    agent = models.ForeignKey(Agent, on_delete=models.RESTRICT)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.service} {self.cost_final}'

    @property
    def list_time(self):
        return [i for i in range(8, 17, self.service.time * (self.count_child + self.count_adult))]
        # start work in 8 end work 17 list time for this book

    @property
    def cost_all(self):
        return self.service.cost * (self.count_child + self.count_adult)  # price child and adult is same
