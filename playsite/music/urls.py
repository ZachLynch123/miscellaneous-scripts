from django.conf.urls import url
from . import views
# Added app_name and added it to index.html so that when other apps have the same 'detail' url, django knows which
#  detail.html to look for
app_name = 'music'

# Create music

urlpatterns = [
    # V default homepage (index for each individual app)
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),
     # /music/<albumid>/add
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    # /music/album/2
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    # /music/album/2/delete
    url(r'^(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),


]