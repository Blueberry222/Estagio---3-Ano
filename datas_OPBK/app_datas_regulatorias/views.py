from django.shortcuts import render
from .models import Atividade, TarefaRegulatoria
from datetime import date

def home(request):
    
    return render(request, 'home.html')

def atividade_list(request):
    atividades = Atividade.objects.all()

    # Calculate the status for each activity
    today = date.today()
    for atividade in atividades:
        progresso_atual = atividade.progresso_atual
        progresso_necessario = atividade.progresso_necessario
        progress_percentage = (progresso_atual / progresso_necessario) * 100

        data_entrega = atividade.data_entrega

        if progress_percentage >= 100:
            atividade.status = "Concluído"
        elif data_entrega < today:
            atividade.status = "Atrasado"
        elif progresso_atual <= 0:
            atividade.status = "TODO"
        else:
            atividade.status = "Em Progresso"

    return render(request, 'atividade_list.html', {'atividades': atividades})

def tarefas_list(request):
    tarefas = TarefaRegulatoria.objects.all()
    
    return render(request, 'tarefas_list.html', {'tarefas': tarefas})

