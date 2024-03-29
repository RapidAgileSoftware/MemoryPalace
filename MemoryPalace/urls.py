"""
URL configuration for MemoryPalace project.
"""
from django.contrib import admin
from django.urls import include,path

from . import views

app_name = 'MemoryPalace'
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('casting/', include('casting.urls')),
    path('images/', include('images.urls')),
]
