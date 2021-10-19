# Generated by Django 3.2.4 on 2021-10-09 15:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0010_auto_20211006_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificado',
            name='certificado_monto_pesos',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Monto en Pesos'),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='certificado_monto_uvi',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Monto en UVI'),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='certificado_rubro_691',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Decreto N°691/16 N°'),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='certificado_rubro_anticipo',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Anticipo N°'),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='certificado_rubro_devanticipo',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Devolución de Anticipo N°'),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='certificado_rubro_obra',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Obra N°'),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='certificado_rubro_recomposicion',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Recomposición N°'),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='certificado_rubro_terreno',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Terreno | Cuota N°'),
        ),
        migrations.AlterField(
            model_name='poliza',
            name='poliza_monto_pesos',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Monto Sustituido Pesos'),
        ),
        migrations.AlterField(
            model_name='poliza',
            name='poliza_monto_uvi',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Monto Sustituido UVI'),
        ),
    ]