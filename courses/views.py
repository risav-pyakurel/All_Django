from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('<h1> Home Page </h1>')
def learn_django(request):
    cname = 'Django'
    duration = '4 months'
    seats =  19
    django_details = {'nm' : cname, 'du': duration, 'st': seats}
    return render(request, 'courses/courses.html',  django_details)

