from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'dashboard/', views.dashboard, name = 'dashboard'),
    url(r'tsops/$', views.show_tsops, name = 'tsops'),
    
]