from django.shortcuts import render

from django.http import HttpResponse


def fees_django(request):
    return HttpResponse('5000 rupees')
