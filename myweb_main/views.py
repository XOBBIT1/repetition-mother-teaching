from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'myweb_main/index.html')

def about(request):
    return render(request, "myweb_main/index_about.html")
