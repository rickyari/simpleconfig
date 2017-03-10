from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^$', views.user_login, name='login'),
    url(r'dashboard/$', views.dashboard, name = 'dashboard'),
    url(r'logout/$', views.user_logout, name = 'logout'),
]