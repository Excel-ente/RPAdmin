# Generated by Django 4.1.5 on 2023-02-21 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0012_scanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanner',
            name='Finalizado',
            field=models.TextField(blank=True, default=0, null=True),
        ),
    ]