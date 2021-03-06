from django.contrib import admin

from import_export.admin import ImportExportMixin

from carga import models
from carga import resources

# Register your models here.
class ReceptorAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = resources.ReceptorResource
class AreaAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = resources.AreaResource
class AseguradoraAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = resources.AseguradoraResource
class EmpresaAdmin(ImportExportMixin, admin.ModelAdmin):
	list_display = ["id", "empresa_nombre", "empresa_cuit"]
	ordering = ["id"]
	resource_class = resources.EmpresaResource
class PolizaAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = resources.PolizaResource

class PolizaMovimientoAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = resources.PolizaMovimientoResource

class LegacyPolizaAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = resources.LegacyPolizaResource
	list_display = ("legacy_poliza_receptor", "legacy_poliza_concepto", "legacy_poliza_numero", "legacy_poliza_tomador")

class ProgramaAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = resources.ProgramaResource

class DepartamentoAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = resources.DepartamentoResource
	list_display = ("id", "departamento_nombre")

class LocalidadAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = resources.LocalidadResource
	list_display = ("id", "localidad_nombre", "localidad_municipio", "localidad_departamento", "localidad_funcion")

class MunicipioAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = resources.MunicipioResource
	list_display = ("id", "municipio_nombre", "municipio_departamento")

class ObraAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = resources.ObraResource

class PrototipoAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = resources.PrototipoResource

class AgenteAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = resources.AgenteResource

class CertificadoAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = resources.CertificadoResource

class ConjuntoLicitadoAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = resources.ConjuntoLicitadoResource

class SubConjuntoLicitadoAdmin(ImportExportMixin, admin.ModelAdmin):
	resource_class = resources.SubConjuntoLicitadoResource

admin.site.register(models.Receptor, ReceptorAdmin)
admin.site.register(models.Area, AreaAdmin)
admin.site.register(models.Aseguradora, AseguradoraAdmin)
admin.site.register(models.Empresa, EmpresaAdmin)
admin.site.register(models.LegacyPoliza, LegacyPolizaAdmin)
admin.site.register(models.Programa, ProgramaAdmin)
admin.site.register(models.Departamento, DepartamentoAdmin)
admin.site.register(models.Localidad, LocalidadAdmin)
admin.site.register(models.Municipio, MunicipioAdmin)
admin.site.register(models.Obra, ObraAdmin)
admin.site.register(models.Prototipo, ProgramaAdmin)
admin.site.register(models.Agente, AgenteAdmin)
admin.site.register(models.Certificado, CertificadoAdmin)
admin.site.register(models.Poliza, PolizaAdmin)
admin.site.register(models.Poliza_Movimiento, PolizaMovimientoAdmin)
admin.site.register(models.ConjuntoLicitado, ConjuntoLicitadoAdmin)
admin.site.register(models.SubConjuntoLicitado, SubConjuntoLicitadoAdmin)