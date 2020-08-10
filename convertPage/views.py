from django.shortcuts import render
from django.views.generic import View
from django.http import FileResponse
from convertPage.gcp_module import gcp
import os

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, './convertPage/index.html')

    def post(self, request, *args, **kwargs):
        text = {
        'convertStr': request.POST.get('convertStr')
        }
        return render(request, './convertPage/index.html', text)
index = IndexView.as_view()

class DownloadView(View):
    def post(self, request, *args, **kwargs):
        ctext = request.POST.get('converttext')
        download_file, filename = gcp.text_to_speech(ctext)
        # ダウンロードファイルは削除
        os.remove(filename)
        return download_file
donwload = DownloadView.as_view()

class SaveView(View):
    def post(self, request, *args, **kwargs):
        ctext = request.POST.get('converttext')
        gcp.cloud_storage(ctext)
        sp = {
        'sp': 1
        }
        return render(request, './convertPage/index.html', sp)
save = SaveView.as_view()
