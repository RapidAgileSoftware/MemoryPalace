from django.urls import path
from . import views

app_name = 'casting'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:actor_id>/', views.detail, name='detail'),
    path('rehearsal/', views.rehearsal, name='rehearsal'),
]
