from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('<h1> Home Page </h1>')
def learn_django(request):
    return render(request, 'courses.html')

