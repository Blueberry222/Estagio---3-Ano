# Generated by Django 4.2.5 on 2023-10-31 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_datas_regulatorias', '0004_atividade_status_alter_atividade_progresso_atual_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='status',
            field=models.CharField(choices=[('Em Progresso', 'Em Progresso'), ('TODO', 'TODO'), ('Atrasado', 'Atrasado'), ('Concluido', 'Concluido'), ('N/A', 'N/A')], default='TODO', max_length=20),
        ),
    ]
