from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
