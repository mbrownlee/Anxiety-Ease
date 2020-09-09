from django.db import models
from django.contrib.auth.models import User
from .activity_type import ActivityType


class ActivityDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    activity_type = models.ForeignKey(ActivityType, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True, blank=True)
    note = models.CharField(null=True, blank=True, max_length=450)

    

    class Meta:
        verbose_name = ("activity detail")
        verbose_name_plural = ("activity details")

    def __str__(self):
         return f'Activity was completed at {self.created_at}. Notes: {self.note}.'