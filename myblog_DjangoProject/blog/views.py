from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.

def homepage(request):
    view = "homepage"
    html = "<html><body>this is %s view </body></html>" % view
    return HttpResponse(html)
