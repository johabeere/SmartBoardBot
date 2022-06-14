from django.shortcuts import render
from smartwebbot.models.Media import Media

def loadpanel(request):
    target = request.POST.get('target')
    if target == 'show-connection':
        return render(request, 'panels/connection/show-connection.html')
    elif target == 'connection-log':
        return render(request, 'panels/connection/connection-log.html')
    elif target == 'connection-stats':
        return render(request, 'panels/connection/show-connection.html')
    elif target == 'show-uploads':
        return render(request, 'panels/connection/show-connection.html')
    elif target == 'my-uploads':
        files = Media.objects.all()
        return render(request, 'panels/uploads/my-uploads.html', {'files': files})
    else:
        return render(request, 'panels/error.html')
