from django.conf.urls import url
from . import views

# Create music

urlpatterns = [
    # V default homepage (index for each individual app)
    url(r'^$', views.index, name='index'),

]