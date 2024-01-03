"""
URL configuration for MemoryPalace project.
"""
from django.contrib import admin
from django.urls import include,path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('casting/', include('casting.urls')),
]
