from django.contrib import admin
from .models import Atividade, Informe, Produto, TarefaRegulatoria

admin.site.register(Atividade)
admin.site.register(Informe)
admin.site.register(Produto)
admin.site.register(TarefaRegulatoria)
