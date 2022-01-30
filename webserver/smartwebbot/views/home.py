from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    if not request.user.is_authenticated:
        return HttpResponse("403")
    return render(request, 'core/home.html')