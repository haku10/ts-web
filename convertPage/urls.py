from django.conf.urls import url
from django.contrib.auth import views as auth_views
from convertPage.view import top
from django.urls import path, include
from django.contrib.auth import views as auth_views 

app_name = 'convertPage'

urlpatterns = [
    path('login', auth_views.LoginView.as_view),
    path('', top.index, name='index'),
    path('texttospeech', top.texttospeech, name='texttospeech'),
    path('download', top.donwload, name='donwload'),
    path('save', top.save, name='save'),
    path('surmmarize', top.surmmarize, name='surmmarize'),
]
