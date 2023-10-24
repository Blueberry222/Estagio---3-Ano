from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_tarefa, name='dashboard_tarefa'),
]
