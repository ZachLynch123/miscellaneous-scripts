from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

class Song(models.Model):
    # on_delete models.CASCADE
    # okay so since you have a song, and it needs to be part of an album
    # what happens when you delete the album? It deletes all songs related
    # to that specific album. So that there are no random floating songs without a
    # respective album
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)