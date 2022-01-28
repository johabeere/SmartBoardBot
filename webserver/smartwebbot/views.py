from django.http import HttpResponse, request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")
def TestPage(request):
    return render(request, 'test.html', {'name': "Developer"})
    #return render(request, 'test.html')