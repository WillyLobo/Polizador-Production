# Generated by Django 3.2.3 on 2021-06-15 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_nombre', models.CharField(max_length=50, verbose_name='Area')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
            },
        ),
        migrations.CreateModel(
            name='Aseguradora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aseguradora_nombre', models.CharField(max_length=255, verbose_name='Nombre Empresa Aeguradora')),
            ],
            options={
                'verbose_name': 'Aseguradora',
                'verbose_name_plural': 'Aseguradoras',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa_nombre', models.CharField(max_length=255, verbose_name='Nombre Empresa Tomadora:')),
                ('empresa_cuit', models.CharField(blank=True, max_length=11, null=True, verbose_name='CUIT:')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Receptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receptor_nombre', models.CharField(max_length=100, verbose_name='Receptor')),
            ],
            options={
                'verbose_name': 'Receptor',
                'verbose_name_plural': 'Receptores',
            },
        ),
        migrations.CreateModel(
            name='Poliza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poliza_fecha', models.DateField(verbose_name='Fecha')),
                ('poliza_expediente', models.CharField(max_length=17, verbose_name='Número de Expediente')),
                ('poliza_numero', models.IntegerField(verbose_name='Número de Póliza')),
                ('poliza_concepto', models.CharField(choices=[('C', 'Garantía de Ejecución de Contrato'), ('F', 'Garantía de Sustitución de Fondo de Reparo'), ('A', 'Garantía de Anticipo Financiero')], max_length=1, verbose_name='Concepto')),
                ('poliza_anexo', models.CharField(blank=True, max_length=40, null=True, verbose_name='Anexo de póliza')),
                ('poliza_recibo', models.CharField(max_length=100, verbose_name='Número de Recibo')),
                ('poliza_obra_nombre', models.TextField(verbose_name='Obra')),
                ('poliza_obra_convenio', models.CharField(blank=True, max_length=50, null=True, verbose_name='Convenio')),
                ('poliza_obra_expediente', models.CharField(blank=True, max_length=17, null=True, verbose_name='Número de Expediente de la Obra')),
                ('poliza_monto_pesos', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Monto Sustituido Pesos')),
                ('poliza_monto_uvi', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Monto Sustituido UVI')),
                ('poliza_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carga.area')),
                ('poliza_aseguradora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carga.aseguradora')),
                ('poliza_receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carga.receptor')),
                ('poliza_tomador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carga.empresa')),
            ],
            options={
                'verbose_name': 'Póliza',
                'verbose_name_plural': 'Pólizas',
            },
        ),
    ]
