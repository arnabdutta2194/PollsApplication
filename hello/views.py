from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def myview(request):
    resp = HttpResponse()
    resp.set_cookie('dj4e_cookie','ad7ed5d4',max_age=1000)

    return resp