# Generated by Django 4.2.5 on 2023-11-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_datas_regulatorias', '0007_remove_tarefaregulatoria_atividade_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefaregulatoria',
            name='produto',
        ),
        migrations.AddField(
            model_name='tarefaregulatoria',
            name='produto',
            field=models.ManyToManyField(to='app_datas_regulatorias.produto'),
        ),
    ]