from django.shortcuts import render
from django.views.generic import View
from django.http import FileResponse
from convertPage.gcp_module import gcp 

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, './convertPage/index.html')

    def post(self, request, *args, **kwargs):
        text = {
        'convertStr': request.POST.get('convertStr')
        }
        # download_file = gcp.text_to_speech(text)
        return render(request, './convertPage/index.html', text)
index = IndexView.as_view()

class DownloadView(View):
    def post(self, request, *args, **kwargs):
        ctext = request.POST.get('converttext')
        download_file = gcp.text_to_speech(ctext)
        return download_file
donwload = DownloadView.as_view()
