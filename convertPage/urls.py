from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views 

app_name = 'convertPage'

urlpatterns = [
    path('login', auth_views.LoginView.as_view),
    path('', views.index, name='index'),
    path('download', views.donwload, name='donwload'),
    path('save', views.save, name='save'),
]
