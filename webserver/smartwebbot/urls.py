from urllib.parse import urlparse
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testpage', views.TestPage, name='TestPage'),
    path('home', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.home),
    path('loadpanel', views.loadpanel, name='loadpanel'),
    path('files/upload', views.upload, name='upload'),
    path('camera/take_picture', views.take_picture, name='take_picture'),
    path('motor/start_motor', views.start_motor, name='start_motor'),
    path('parser/parse_file', views.parse_file, name='parse_file'),
    path('log/getlogs', views.getlogs, name='getlogs'),
]