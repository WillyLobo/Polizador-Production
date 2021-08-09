# Generated by Django 3.2.4 on 2021-07-16 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0002_auto_20210714_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='empresa_direccion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección de la Empresa'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='empresa_titular',
            field=models.CharField(blank=True, max_length=140, null=True, verbose_name='Titular de la Empresa'),
        ),
    ]