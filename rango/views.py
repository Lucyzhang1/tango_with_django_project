from django.shortcuts import render
from django.http import HttpResponse

def index(request):# This is a view, it has a parameter. it must return a httprequest object
    return HttpResponse("Rango says hey there partner!")

def about(request):
    return HttpResponse("Rango says here is the about page.")