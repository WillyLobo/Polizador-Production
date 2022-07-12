# Generated by Django 3.2.4 on 2022-02-24 14:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carga', '0001_squashed_0019_auto_20220222_0905'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Poliza',
            new_name='LegacyPoliza',
        ),
        migrations.AlterModelOptions(
            name='legacypoliza',
            options={'verbose_name': 'Legacy_Póliza', 'verbose_name_plural': 'Legacy_Pólizas'},
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_anexo',
            new_name='legacy_poliza_anexo',
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_area',
            new_name='legacy_poliza_area',
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_aseguradora',
            new_name='legacy_poliza_aseguradora',
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_concepto',
            new_name='legacy_poliza_concepto',
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_creador',
            new_name='legacy_poliza_creador',
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_editor',
            new_name='legacy_poliza_editor',
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_expediente',
            new_name='legacy_poliza_expediente',
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_fecha',
            new_name='legacy_poliza_fecha',
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_monto_pesos',
            new_name='legacy_poliza_monto_pesos',
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_monto_uvi',
            new_name='legacy_poliza_monto_uvi',
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_numero',
            new_name='legacy_poliza_numero',
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_obra_convenio',
            new_name='legacy_poliza_obra_convenio',
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_obra_expediente',
            new_name='legacy_poliza_obra_expediente',
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_obra_nombre',
            new_name='legacy_poliza_obra_nombre',
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_receptor',
            new_name='legacy_poliza_receptor',
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_recibo',
            new_name='legacy_poliza_recibo',
        ),
        migrations.RenameField(
            model_name='legacypoliza',
            old_name='poliza_tomador',
            new_name='legacy_poliza_tomador',
        ),
    ]