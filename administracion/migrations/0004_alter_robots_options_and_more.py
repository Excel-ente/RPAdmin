# Generated by Django 4.1.5 on 2023-01-22 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_gerencia_horas_beneficio_alter_incidencias_estado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='robots',
            options={'verbose_name': 'Robot', 'verbose_name_plural': 'Robots'},
        ),
        migrations.AlterField(
            model_name='ejecucionesprocesos',
            name='DURACION_TAREA_MINUTOS_MANUAL',
            field=models.IntegerField(null=True, verbose_name='DURACION DE LA TAREA (manualmente) Min.'),
        ),
    ]
