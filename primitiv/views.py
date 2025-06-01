from django.shortcuts import render
from . import templates


def web1(request):
    return render(request, 'site1.html')


def home(request):
    return render(request, 'home.html', {})