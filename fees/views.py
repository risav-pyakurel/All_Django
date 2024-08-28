from django.shortcuts import render

from django.http import HttpResponse


def fees_django(request):
    return render(request, 'fees.html')
