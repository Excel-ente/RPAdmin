# Generated by Django 4.1.4 on 2023-03-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0016_remove_scanner_finalizado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='PreMonitoreo',
        ),
        migrations.DeleteModel(
            name='Scanner',
        ),
    ]
