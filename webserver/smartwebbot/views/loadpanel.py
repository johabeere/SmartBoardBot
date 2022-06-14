import os

from django.shortcuts import render
from smartwebbot.models.Media import Media

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
        img_dir = os.getcwd() + "/smartwebbot/static/img/photos/"

        filename = "not_found"
        for i in range(0,100000):
            if not os.path.exists(img_dir+"image"+str(i)+".jpg"):
                break
            else:
                filename = "image"+str(i)

        return render(request, 'panels/camera/show-camera.html', {'img_url': "/static/img/photos/"+filename+".jpg"})
    else:
        return render(request, 'panels/error.html')
