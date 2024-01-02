from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:actor_id>/', views.detail, name='detail'),
    path('rehearsal/<int:actor_id>/<int:prop_id>/<int:action_id>', views.rehearsal, name='rehearsal'),
]
