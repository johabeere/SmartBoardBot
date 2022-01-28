from django.shortcuts import render
from django.http import HttpResponse, request


def TestPage(request):
    return render(request, 'test.html', {'name': "Developer"})