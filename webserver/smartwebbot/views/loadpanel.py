import os


from django.shortcuts import render
from smartwebbot.models.Media import Media
from smartwebbot.boardfunctions import camera
from smartwebbot.boardfunctions import logger
def loadpanel(request):
    logger.log("Loaded a Panel!", 10)
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
    elif target == 'show-camera':
        img_url = camera.get_current_filename_web()
        return render(request, 'panels/camera/show-camera.html', {'img_url': img_url})
    elif target == 'motorcontrol':
        return render(request, 'panels/motor/motorcontrol.html')
    elif target == 'parser':
        return render(request, 'panels/parser/index.html')
    elif target == 'dashboard':
        return render(request, 'panels/dashboard/index.html')
    else:
        return render(request, 'panels/error.html')
