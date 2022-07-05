# Generated by Django 3.2.4 on 2022-03-02 14:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carga', '0002_auto_20220224_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poliza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poliza_fecha', models.DateField(verbose_name='Fecha')),
                ('poliza_expediente', models.CharField(max_length=17, verbose_name='Expediente')),
                ('poliza_numero', models.IntegerField(verbose_name='Número de Póliza')),
                ('poliza_concepto', models.CharField(choices=[('C', 'Garantía de Ejecución de Contrato'), ('F', 'Garantía de Sustitución de Fondo de Reparo'), ('A', 'Garantía de Anticipo Financiero')], max_length=1, verbose_name='Concepto')),
                ('poliza_anexo', models.CharField(blank=True, max_length=40, null=True, verbose_name='Anexo de Póliza')),
                ('poliza_recibo', models.CharField(max_length=100, verbose_name='Número de Recibo')),
                ('poliza_monto_pesos', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Monto Sustituido en Pesos')),
                ('poliza_monto_uvi', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Monto Sustituido en UVI')),
            ],
            options={
                'verbose_name': 'Póliza',
                'verbose_name_plural': 'Pólizas',
            },
        ),
        migrations.CreateModel(
            name='Poliza_Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poliza_movimiento_fecha', models.DateField(verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'Poliza_Movimiento',
                'verbose_name_plural': 'Polizas_Movimiento',
            },
        ),
        migrations.AlterField(
            model_name='legacypoliza',
            name='legacy_poliza_editor',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='legacy_poliza_editor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='poliza_movimiento',
            name='poliza_movimiento_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carga.area'),
        ),
        migrations.AddField(
            model_name='poliza_movimiento',
            name='poliza_movimiento_editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='poliza_movimiento',
            name='poliza_movimiento_numero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carga.poliza'),
        ),
        migrations.AddField(
            model_name='poliza_movimiento',
            name='poliza_movimiento_receptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carga.receptor'),
        ),
        migrations.AddField(
            model_name='poliza',
            name='poliza_aseguradora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carga.aseguradora'),
        ),
        migrations.AddField(
            model_name='poliza',
            name='poliza_creador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='poliza',
            name='poliza_editor',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poliza_editor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='poliza',
            name='poliza_obra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carga.obra'),
        ),
        migrations.AddField(
            model_name='poliza',
            name='poliza_tomador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carga.empresa'),
        ),
        migrations.AddConstraint(
            model_name='poliza',
            constraint=models.UniqueConstraint(fields=('poliza_fecha', 'poliza_numero', 'poliza_aseguradora', 'poliza_tomador'), name='poliza-constraint'),
        ),
    ]
