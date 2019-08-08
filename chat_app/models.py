from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


class OpenRoom(models.Model):
    title = models.CharField(max_length=100)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.title


class OneToOneRoom(models.Model):
    title = models.CharField(max_length=100)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    limitation = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title