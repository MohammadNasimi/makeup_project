from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Agent(BaseModel):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    descriptions = models.CharField(max_length=1000)
    experience_year = models.PositiveIntegerField(default=0)
    count_service = models.PositiveIntegerField()
    image = models.FileField(null=True, default=None, upload_to='Agent_pic', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        # verbose_name = 'مشتری'
        # verbose_name_plural = 'مشتری ها'
        verbose_name = _('Agent')
        verbose_name_plural = _('Agents')


class Weekend(BaseModel):
    Agent = models.ForeignKey(Agent, on_delete=models.RESTRICT, verbose_name='Agent',
                              related_name='Agent')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.Agent} {self.start_time}'
