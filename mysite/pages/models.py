from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=2)
     
    def __str__(self):
            return self.name

   