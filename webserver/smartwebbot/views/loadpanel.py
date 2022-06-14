import os

from django.shortcuts import render
from smartwebbot.models.Media import Media
from smartwebbot.boardfunctions import camera

def loadpanel(request):
    target = request.POST.get('target')
    if target == 'show-connection':
        return render(request, 'panels/connection/show-connection.html')
    elif target == 'connection-log':
        return render(request, 'panels/connection/show-connection.html')
    elif target == 'connection-stats':
        return render(request, 'panels/connection/show-connection.html')
    elif target == 'show-uploads':
        return render(request, 'panels/connection/show-connection.html')
    elif target == 'my-uploads':
        files = Media.objects.all()
        return render(request, 'panels/uploads/my-uploads.html', {'files': files})
    elif target == 'show-camera':
        img_url = camera.get_current_filename_web()
        return render(request, 'panels/camera/show-camera.html', {'img_url': img_url})
    else:
        return render(request, 'panels/error.html')
