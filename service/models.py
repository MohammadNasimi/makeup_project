from django.db import models
from core.models import BaseModel


# Create your models here.
class Service(BaseModel):
    name = models.CharField(max_length=40)
    time = models.PositiveIntegerField(null=False, default=1, verbose_name='Time_Service')
    cost = models.PositiveIntegerField(null=False, verbose_name='Price_Service')
