# Creating the app's URL Dispatcher
from django.conf.urls import url
from . import views
# This pattern checks that the URL has an empty path, which will go to home page
# the "$" terminates it so that not all empty strings lead to the same home page
# Get from the views.py file, the index function
urlpatterns = [
    url(r'^$', views.index),

]