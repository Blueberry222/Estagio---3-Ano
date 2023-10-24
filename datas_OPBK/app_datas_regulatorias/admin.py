from django.contrib import admin
from .models import Atividade, Informe, Produto, TarefaRegulatoria

class Atividade_Admin(admin.ModelAdmin):
    list_display = ['descricao', 'data_entrega', 'progresso_atual', 'progresso_atual']
    list_filter = ['data_entrega']
    date_hierarchy = 'data_entrega'
    search_fields = ['descricao']
    
class Informe_Admin(admin.ModelAdmin):
    list_display = ['numero', 'link']
    search_fields = ['numero']
    
class Produto_Admin(admin.ModelAdmin):
    pass

admin.site.register(Atividade, Atividade_Admin)

admin.site.register(Informe, Informe_Admin)

admin.site.register(Produto)

admin.site.register(TarefaRegulatoria)
