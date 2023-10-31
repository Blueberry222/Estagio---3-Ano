from django.shortcuts import render
from .models import Atividade  # Import your Atividade model

def atividade_list(request):
    atividades = Atividade.objects.all()
    return render(request, 'atividade_list.html', {'atividades': atividades})
