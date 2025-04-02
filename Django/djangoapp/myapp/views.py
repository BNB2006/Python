#Example: 1
from django.shortcuts import render

#create your vew here
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello, welcome to django!</h2>")

#Example: 2
import datetime
from django.http import HttpResponse

def index(request):
    now =  datetime.datetime.now()
    html1 = "<html><body><h3>Now time is %s.</h3><body></html>" %now
    return HttpResponse(html1) #render the templete in HttpResponse