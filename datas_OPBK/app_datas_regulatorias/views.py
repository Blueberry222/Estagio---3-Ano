from django.http import JsonResponse
from django.shortcuts import render
from .models import TarefaRegulatoria
from django.core import serializers

def dashboard_tarefa(request):
    tarefas = TarefaRegulatoria.objects.all()
    return render(request, 'dashboard_tarefa.html', {'tarefas': tarefas})