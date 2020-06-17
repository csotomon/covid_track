from django.contrib.auth.models import User, Group
from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Poi(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)

class Tracking(models.Model):
    owner = models.ForeignKey('auth.User', related_name='trackings', on_delete=models.CASCADE)
    date = models.DateTimeField()
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)

    #def save(self, *args, **kwargs):
    #    super(Tracking, self).save(*args, **kwargs)
    
