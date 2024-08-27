from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('<h1> Home Page </h1>')
def learn_django(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def learn_python(request):
    return HttpResponse('<h2> Python is a programming language that lets you work quickly '
                        'and integrate systems more effectively. </h2>')