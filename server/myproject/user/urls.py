from django.contrib import admin 
from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views 
urlpatterns = [
    path('register',views.user_register,name='register'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('change-password',views.change_password,name='change_password'),
]
