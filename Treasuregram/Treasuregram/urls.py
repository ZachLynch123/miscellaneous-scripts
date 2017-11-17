"""Treasuregram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from main_app import views
"""using urls.py from the project file to dispatch urls
"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # localhost/index
    # Instead of using urls.py in the project file to dispatch urls, each "app"
    # of the project will dispatch their own url using their specific url.py
    url(r'^',
        include('main_app.url'))
]
