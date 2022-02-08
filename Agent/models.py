from django.db import models
from core.models import BaseModel


# Create your models here.
class Agent(BaseModel):
    first_name = models.CharField(max_length=150, verbose_name='first_name')
    last_name = models.CharField(max_length=150, verbose_name='last_name')
    descriptions = models.CharField(max_length=1000, verbose_name='descriptions')
    experience_year = models.PositiveIntegerField(default=0)
    count_service = models.PositiveIntegerField()
    image = models.FileField(null=True, default=None, upload_to='Agent_pic', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Weekend(BaseModel):
    Agent = models.ForeignKey(Agent, on_delete=models.RESTRICT, verbose_name='Agent',
                              related_name='Agent')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.Agent} {self.start_time}'
