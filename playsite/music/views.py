from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
# Create your views here.

def index(request):
    # Simple all to database that selects all objects from Album column
    all_albums = Album.objects.all()
    html = ''
    # For loop that displays album title that when clicked
    # Will take them to the detailed page of the Album with songs, artist etc.
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'


    return HttpResponse(html)

def detail(request, album_id):
    return HttpResponse("<h2>Detaisl for Album_id: " + str(album_id) + "</h2>")
