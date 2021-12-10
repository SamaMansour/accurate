from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.TextField()
    frequency = models.TextField()
    