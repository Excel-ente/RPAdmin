# Generated by Django 4.1.5 on 2023-02-22 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0013_scanner_finalizado'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanner',
            name='hora',
            field=models.TextField(blank=True, null=True),
        ),
    ]
