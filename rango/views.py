
from django.http import HttpResponse
from django.shortcuts import render

def index(request):# This is a view, it has a parameter. it must return a httprequest object
    #return HttpResponse("Rango says hey there partner!")
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)



def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")