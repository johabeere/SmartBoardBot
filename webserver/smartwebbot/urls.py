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
    path('dashboard/start_scan', views.start_scan , name='start_scan'),
    path('dashboard/cancel_scan', views.cancel_scan , name='cancel_scan'),
    path('dashboard/cancel_drawing', views.cancel_drawing , name='cancel_drawing'),
    path('dashboard/start_drawing', views.start_drawing , name='start_drawing'),
    path('dashboard/update', views.update_dashboard, name='update_dashboard')
]