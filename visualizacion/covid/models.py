from django.contrib.auth.models import User, Group
from django.db import models

class Poi(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)

class Tracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    
