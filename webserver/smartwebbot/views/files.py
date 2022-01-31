from django.http import HttpRequest, HttpResponse

from smartwebbot.models.Document import Document


def upload(request):
    file = request.FILES['file']
    if file.name.endswith('.pdf'):
        document = Document.create(request.user, file.name, file.read(), True)
        return HttpResponse(document)
    return HttpResponse(file.name)
