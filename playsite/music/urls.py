from django.conf.urls import url
from . import views

app_name = 'music'

# Create music

urlpatterns = [
    # V default homepage (index for each individual app)
    url(r'^$', views.index, name='index'),

    #  /music/<albumid>/

    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

]