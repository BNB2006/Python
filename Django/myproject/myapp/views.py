from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# template function
# def index(request):
#     return render(request, 'myapp/index.html')

def hello(request):
    return HttpResponse('<h1>This is Http GET request.</h1>')


# Student form 
from myapp.forms import StuForm

def index(request):
    stu = StuForm()
    return render(request, "myapp/index.html", {"form": stu})
