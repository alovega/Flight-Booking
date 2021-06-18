import datetime

import django.utils.timezone
from django.db import models

# Create your models here.


class Flight(models.Model):
    beginning = models.CharField(max_length=500, null=False, blank=False)
    destination = models.CharField(max_length=500, null=False, blank=False)
    start_date = models.DateTimeField(default=django.utils.timezone.now, null=False, blank=False)
    return_date = models.DateTimeField(default=django.utils.timezone.now, null=False, blank=False)
    adult = models.IntegerField(null=True, blank=True, default=1)
    children = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '%s %s'%(self.beginning, self.destination)