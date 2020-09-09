from django.db import models


class ActivityType(models.Model):

    name = models.CharField(max_length=55)

    class Meta:
        verbose_name = ("activity type")
        verbose_name_plural = ("activity types")

    def __str__(self):
        return self.name