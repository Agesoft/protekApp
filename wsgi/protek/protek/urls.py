"""protek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
	url(r'^admin/', include(admin.site.urls)),
	url(r'^user/(\w+)/$', user_page),
  (r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^contact/', contact, name="contact"),
	
	
def conact(request):
	return render(request, 'core/contact.html')
"""
from django.conf.urls import include, url
from django.contrib import admin
from protekApp.views import *  

#from . import views

urlpatterns = [
    url(r'^$', home, name="home"),	
	url(r'^account/(\w+)/$', account_new, name="account"),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^contact/', contact, name="contact"),
]
