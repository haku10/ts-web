from django.shortcuts import render
from django.views.generic import View
from django.http import FileResponse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from convertPage.service.gcp_module import gcp
from convertPage.service.parse_csv import parse_csv
from io import TextIOWrapper, StringIO
import os
import base64
import wave
import logging

logger = logging.getLogger('development')

class LoginView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, './convertPage/login.html')
login = LoginView.as_view()

class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, './convertPage/index.html')
index = IndexView.as_view()

class TextToSpeechView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, './convertPage/texttospeech.html')

    def post(self, request, *args, **kwargs):
        text = {
        'convertStr': request.POST.get('convertStr')
        }
        return render(request, './convertPage/texttospeech.html', text)
texttospeech = TextToSpeechView.as_view()

class SpeechToText(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, './convertPage/speechtotext.html')
speechtotext = SpeechToText.as_view()

class DownloadView(View):
    def post(self, request, *args, **kwargs):
        ctext = request.POST.get('converttext')
        download_file, filename = gcp.text_to_speech(ctext)
        # ダウンロードファイルは削除
        os.remove(filename)
        return download_file
download = DownloadView.as_view()

class SaveView(View):
    def post(self, request, *args, **kwargs):
        ctext = request.POST.get('converttext')
        gcp.cloud_storage(ctext)
        sp = {
        'sp': 1
        }
        return render(request, './convertPage/index.html', sp)
save = SaveView.as_view()

class UploadView(View):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST' and request.FILES['speech']:
            file = request.FILES['speech']
            gcp.speechtotext(file)
        return render(request, './convertPage/speechtotext.html')
upload = UploadView.as_view()

class SurmmarizeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, './convertPage/surmmarize.html')
surmmarize = SurmmarizeView.as_view()

def csv_parse(request):
    if request.method == 'POST':
        data1 = TextIOWrapper(request.FILES['csvfile'].file, encoding='utf-8')
        response_json = parse_csv.csv_parse_speechtext(data1)
        print(response_json)
        return HttpResponse(response_json)
