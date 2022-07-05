# Generated by Django 3.2.4 on 2022-06-21 13:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carga', '0003_auto_20220302_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificado',
            name='certificado_acum_pct',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Acumulado %'),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='certificado_ante_pct',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Anterior %'),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='certificado_devolucion_expte',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='Número de Expediente Devolución'),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='certificado_expediente',
            field=models.CharField(max_length=18, verbose_name='Número de Expediente'),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='certificado_mes_pct',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Mes %'),
        ),
        migrations.AlterField(
            model_name='legacypoliza',
            name='legacy_poliza_creador',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='obra',
            name='obra_expediente',
            field=models.CharField(max_length=18, verbose_name='Expediente'),
        ),
        migrations.AlterField(
            model_name='obra',
            name='obra_expediente_costo',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='Expediente de Costos'),
        ),
        migrations.AlterField(
            model_name='poliza',
            name='poliza_creador',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='poliza',
            name='poliza_expediente',
            field=models.CharField(max_length=18, verbose_name='Expediente'),
        ),
    ]
