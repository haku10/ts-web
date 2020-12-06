from django.conf.urls import url
from django.contrib.auth import views as auth_views
from convertPage.view import top
from django.urls import path, include
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('login', auth_views.LoginView.as_view),
    path('', top.index, name='index'),
    path('texttospeech', top.texttospeech, name='texttospeech'),
    path('speechtotext', top.speechtotext, name='speechtotext'),
    path('download', top.download, name='download'),
    path('upload', top.upload, name='upload'),
    path('save', top.save, name='save'),
    path('surmmarize', top.surmmarize, name='surmmarize'),
    # Ajaxでの処理
    path("texttospeech/upload", top.csv_parse, name='csv_parse'),
]
