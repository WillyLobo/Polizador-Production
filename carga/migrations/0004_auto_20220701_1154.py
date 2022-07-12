# Generated by Django 3.2.4 on 2022-07-01 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0003_legacypoliza_legacy-poliza-constraint'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConjuntoLicitado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conjunto_nombre', models.TextField(verbose_name='Nombre')),
                ('conjunto_soluciones', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=5, null=True, verbose_name='Cantidad de Soluciones')),
                ('conjunto_resolucion', models.CharField(blank=True, max_length=15, null=True, verbose_name='Resolucion')),
            ],
        ),
        migrations.RemoveField(
            model_name='obra',
            name='obra_conjunto',
        ),
        migrations.AddField(
            model_name='obra',
            name='obra_conjunto_licitado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='carga.conjuntolicitado', verbose_name='ConjuntoLicitado'),
        ),
    ]