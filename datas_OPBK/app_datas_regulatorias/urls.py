from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('atividades/', views.atividade_list, name='atividade_list'),
    path('tarefas/', views.tarefas_list, name='tarefas_list'),
]
