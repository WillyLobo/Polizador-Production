# Generated by Django 3.2.4 on 2022-02-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0013_alter_obra_obra_nomenclatura'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificado',
            name='certificado_acum_pct',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Acumulado %'),
        ),
        migrations.AddField(
            model_name='certificado',
            name='certificado_ante_pct',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Anterior %'),
        ),
        migrations.AddField(
            model_name='certificado',
            name='certificado_devolucion_expte',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='Número de Expediente'),
        ),
        migrations.AddField(
            model_name='certificado',
            name='certificado_devolucion_monto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Monto en Pesos'),
        ),
        migrations.AddField(
            model_name='certificado',
            name='certificado_mes_pct',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Mes %'),
        ),
        migrations.AddField(
            model_name='certificado',
            name='certificado_monto_cobrar',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=12, verbose_name='Monto a Cobrar'),
        ),
        migrations.AddField(
            model_name='certificado',
            name='certificado_periodo',
            field=models.CharField(default=0, max_length=13, verbose_name='Periodo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='empresa_inscripcion',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Inscripción:'),
        ),
        migrations.AlterField(
            model_name='obra',
            name='obra_nomenclatura',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Nomenclatura Catastral'),
        ),
    ]
