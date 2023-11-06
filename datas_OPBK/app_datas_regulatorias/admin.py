from django.contrib import admin
from .models import Atividade, Informe, Produto, TarefaRegulatoria
from django.utils import timezone
from django.http import HttpResponse
from reportlab.pdfgen import canvas

class Atividade_Admin(admin.ModelAdmin):
    list_display = ('descricao', 'data_entrega', 'display_status_progress', 'formatted_progresso_atual', 'formatted_progresso_necessario')
    list_filter = ['data_entrega']
    date_hierarchy = 'data_entrega'
    search_fields = ['descricao']
    
    def formatted_progresso_atual(self, obj):
        return f"{obj.progresso_atual}%"
    formatted_progresso_atual.short_description = 'Progresso Atual (%)'

    def formatted_progresso_necessario(self, obj):
        return f"{obj.progresso_necessario}%"
    formatted_progresso_necessario.short_description = 'Progresso Necessário (%)'

    def display_status_progress(self, obj):
        if obj.progresso_necessario == 0:
            return "Cancelado"
        
        progresso_porcentagem = (obj.progresso_atual / obj.progresso_necessario) * 100
        if progresso_porcentagem >= 100:
            return "Concluído"
        elif timezone.now().date() > obj.data_entrega:
            return "Atrasado"
        elif progresso_porcentagem > 0:
            return "Em Progresso"
        return "TODO"
    
    display_status_progress.short_description = 'Status'

class Informe_Admin(admin.ModelAdmin):
    list_display = ['numero', 'link']
    search_fields = ['numero']
    
class Produto_Admin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')
    list_filter = ['tipo']
    
class Tarefa_Admin(admin.ModelAdmin):
    list_display = ('titulo', 'escopo')

admin.site.register(Atividade, Atividade_Admin)

admin.site.register(Informe, Informe_Admin)

admin.site.register(Produto, Produto_Admin)

admin.site.register(TarefaRegulatoria, Tarefa_Admin)
