from django.shortcuts import render
from . import templates


def web1(request):
    return render(request, templates.site1)

# Create your views here.
