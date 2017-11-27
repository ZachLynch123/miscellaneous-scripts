from .models import Album, Song
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Album
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailsView(generic.DetailView):
    model = Album

    template_name = 'music/detail.html'