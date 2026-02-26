from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner!<br>/rango/about/About Page</a></a>")

def about(request):
    return HttpResponse("Rango says here is the about page.<br>/rango/Index</a>")
