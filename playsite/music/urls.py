from django.conf.urls import url
from . import views
# Added app_name and added it to index.html so that when other apps have the same 'detail' url, django knows which
#  detail.html to look for
app_name = 'music'

# Create music

urlpatterns = [
    # V default homepage (index for each individual app)
    url(r'^$', views.index, name='index'),

    #  /music/<albumid>/

    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
     # /music/<albumid>/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    # /music/<albumid>/unfav)
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.unfav, name='unfav'),

]