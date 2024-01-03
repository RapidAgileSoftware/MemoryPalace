from django.urls import path
from . import views

app_name = 'casting'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('rehearsal/', views.rehearsal, name='rehearsal'),
]
