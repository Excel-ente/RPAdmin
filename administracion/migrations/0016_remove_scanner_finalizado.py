# Generated by Django 4.1.5 on 2023-02-22 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0015_rename_hora_scanner_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scanner',
            name='Finalizado',
        ),
    ]
