from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from .models import Album
from django.shortcuts import render
# Create your views here.

def index(request):
    # Simple all to database that selects all objects from Album column
    all_albums = Album.objects.all()
    # V using django.template loader
    # template = loader.get_template('music/index.html')
    context = {'all_albums': all_albums,}
    # Commenting everything out
    #html = ''
    # For loop that displays album title that when clicked
    # Will take them to the detailed page of the Album with songs,a =  artist etc.
    #for album in all_albums:
    #    url = '/music/' + str(album.id) + '/'
    #    html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return render(request,'music/index.html', context)

def detail(request, album_id):
    return HttpResponse("<h2>Detaisl for Album_id: " + str(album_id) + "</h2>")

# Connected to the database and got all albums. For each album, I looped through it and displayed it in the HTTPResponse
# when clicked takes you to the detailed page.
