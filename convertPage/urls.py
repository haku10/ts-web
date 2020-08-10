from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download', views.donwload, name='donwload'),
    path('save', views.save, name='save'),
]
