# Generated by Django 4.1.5 on 2023-02-22 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0014_scanner_hora'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scanner',
            old_name='hora',
            new_name='Hora',
        ),
    ]
