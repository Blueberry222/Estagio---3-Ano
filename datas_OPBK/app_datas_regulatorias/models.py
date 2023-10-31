from django.db import models

# Create your models here.

class Produto(models.Model):
    
    TIPO_CHOICES = (
        ("API", "API"),
        ("Cert", "Certificados"),
        ("Other", "Outro")
    )
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
    
class Informe(models.Model):
    numero = models.CharField(max_length=100, null=False, blank=False)
    link = models.CharField(max_length=200, null=False, blank=False) # Alterar para lidar com link?
    
    class Meta:
        verbose_name = "Informe"
        verbose_name_plural = "Informes"
        
    def __str__(self):
        nome = f"Informe {self.numero}"
        return nome
    
class Atividade(models.Model):
    
    descricao = models.CharField(max_length=100, null=False, blank=False)
    data_entrega = models.DateField()
    progresso_atual = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    progresso_necessario = models.DecimalField(max_digits=5, decimal_places=2, default=100.00) 
    
    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"
    
class TarefaRegulatoria(models.Model):
    titulo = models.CharField(max_length=25, null=False, blank=False, default=" ")
    escopo = models.CharField(max_length=500, null=False, blank=False, default=" ")
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    informe = models.ForeignKey(Informe, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "Tarefa Regulatoria"
        verbose_name_plural = "Tarefa Regulatorias"
        
    def __str__(self):
        return self.titulo
    
