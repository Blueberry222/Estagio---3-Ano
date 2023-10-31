from django.urls import path
from . import views

urlpatterns = [
    path('atividades/', views.atividade_list, name='atividade_list'),
]
