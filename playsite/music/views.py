from .models import Album
from django.shortcuts import render, get_object_or_404
# Create your views here.

def index(request):
    # Simple all to database that selects all objects from Album column
    all_albums = Album.objects.all()
    #  using django.template loader
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
    # Commenting out try except in favor of http404
    album = get_object_or_404(Album, pk=album_id)
    #try:
    #    album = Album.objects.get(pk=album_id)
   # except Album.DoesNotExist:
    #    raise Http404("Album not found")
    return render(request,'music/detail.html', {'album': album})

# Connected to the database and got all albums. For each album, I looped through it and displayed it in the HTTPResponse
# when clicked takes you to the detailed page.
# Notice how clean this looks without all the comments
# Theres a lot of logic going on in like 12 lines of code

