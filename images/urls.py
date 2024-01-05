from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'images'

urlpatterns = [
                  path('', views.index, name='index'),
                  path('label_prediction/', views.label_prediction, name='label_prediction')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
