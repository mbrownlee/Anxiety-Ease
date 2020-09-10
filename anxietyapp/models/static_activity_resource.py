from django.db import models
from .activity_type import ActivityType


class StaticActivityResource(models.Model):
    activity_type = models.ForeignKey(ActivityType, on_delete=models.DO_NOTHING)
    resource = models.CharField(max_length=300)
    

    class Meta:
        verbose_name = ("static activity resource")
        verbose_name_plural = ("static activity resources")

    def __str__(self):
        return f'{self.resource}'