from django.http.response import HttpResponse
from django.shortcuts import render


#return page from taskmanager/main/templates
def index(request):
    return  render(request, 'main/index.html')


def about(request):
    return  render(request, 'main/about.html')


# Create your views here.
