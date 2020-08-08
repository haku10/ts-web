from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime

def index(request):
    map = {
        'hour': datetime.now().hour,
        'message': 'Sample message',
    }
    return render(request, './convertPage/index.html' , map)
