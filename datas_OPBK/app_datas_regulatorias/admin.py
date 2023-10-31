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
'''
    def export_as_pdf(modeladmin, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="atividades.pdf"'

        # Create a PDF document
        p = canvas.Canvas(response)
        p.drawString(100, 750, "Atividade Table")

        # Get the data and render it as a table in the PDF
        data = queryset.values_list('descricao', 'data_entrega', 'progresso_atual', 'progresso_necessario')
        y = 700  # Y-coordinate to start rendering data
        p.drawString(50, y, "Descrição")
        p.drawString(125, y, "Data de Entrega")
        p.drawString(250, y, "Progresso Atual")
        p.drawString(400, y, "Progresso Necessario")

        for row in data:
            y -= 20  # Adjust the Y-coordinate for the next row
            p.drawString(50, y, str(row[0]))
            p.drawString(125, y, str(row[1]))
            p.drawString(250, y, str(row[2]))
            p.drawString(400, y, str(row[3]))


        # Close the PDF
        p.showPage()
        p.save()

        return response
    
    export_as_pdf.short_description = "Exportar Selecionados em PDF"
    actions = [export_as_pdf]
    actions_on_top = False
    actions_on_bottom = True
    '''
class Informe_Admin(admin.ModelAdmin):
    list_display = ['numero', 'link']
    search_fields = ['numero']
    
class Produto_Admin(admin.ModelAdmin):
    pass

admin.site.register(Atividade, Atividade_Admin)

admin.site.register(Informe, Informe_Admin)

admin.site.register(Produto)

admin.site.register(TarefaRegulatoria)
