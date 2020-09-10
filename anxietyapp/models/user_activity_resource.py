from django.db import models
from django.contrib.auth.models import User
from .activity_type import ActivityType


class UserActivityResource(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    activity_type = models.ForeignKey(ActivityType, on_delete=models.DO_NOTHING)
    resource = models.CharField(max_length=300)
    

    class Meta:
        verbose_name = ("user activity resource")
        verbose_name_plural = ("user activity resources")

    def __str__(self):
        return f'{self.resource}'