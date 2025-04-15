"""
URL configuration for myproject project.


"""
from django.contrib import admin
from django.urls import path,include 
from .views import * 

from django.conf import settings 
from django.conf.urls.static import static 

# configurations of admin 
admin.site.site_header = "Dave Webdevelopment"
admin.site.index_title = "Welcome to Dave Website"
admin.site.site_title = "Welcome to daveAdmin"



urlpatterns = [
    path('api/',include('api.urls')),
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('abt/',about,name='about'),
    path('serv/',services,name='services'),
    path('user/',include('user.urls')),
    path('emp/',include('emp.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
