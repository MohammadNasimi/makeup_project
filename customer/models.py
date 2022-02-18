from django.db import models
from core.models import BaseModel


# Create your models here.

class Customer(BaseModel):
    first_name = models.CharField(max_length=150, verbose_name='first_name')
    last_name = models.CharField(max_length=150, verbose_name='last_name')
    email = models.EmailField(max_length=250)
    Password = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    