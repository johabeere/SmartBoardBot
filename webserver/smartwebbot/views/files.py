from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from smartwebbot.models.Document import Document


def upload(request):
    file = request.FILES['file']
    if file.name.endswith('.pdf'):
        document = Document.create(request.user, file.name, file.read(),'PDF' , True)
        return render(request, 'panels/uploads/partials/filerow.html', {'file': document})
    return HttpResponse(file.name)
