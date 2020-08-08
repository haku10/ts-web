from django.shortcuts import render
from django.views.generic import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, './convertPage/index.html')

    def post(self, request, *args, **kwargs):
        text = {
        'convertStr': request.POST.get('convertStr')
        }
        return render(request, './convertPage/index.html', text)
index = IndexView.as_view()
