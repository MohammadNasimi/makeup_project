from django.db import models
from core.models import BaseModel


# Create your models here.
class Service(BaseModel):
    name = models.CharField(max_length=40, null=True, blank=True)
    time = models.PositiveIntegerField(null=False, blank=True, default=1, verbose_name='Time_Service')
    cost = models.PositiveIntegerField(null=False, blank=True, verbose_name='Price_Service')
