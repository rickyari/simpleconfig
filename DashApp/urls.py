from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'dashboard/', views.dashboard, name = 'dashboard'),
    url(r'tsops/$', views.show_tsops, name = 'tsops'),
    url(r'egencia/$', views.show_egencia, name = 'egencia'),
    url(r'status/$', views.show_status, name = 'status'),
    url(r'getpercent/$', views.get_percent, name = 'getpercent')

]