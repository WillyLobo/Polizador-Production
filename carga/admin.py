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
	list_display = ("poliza_receptor", "poliza_concepto", "poliza_numero", "poliza_tomador")

admin.site.register(models.Receptor, ReceptorAdmin)
admin.site.register(models.Area, AreaAdmin)
admin.site.register(models.Aseguradora, AseguradoraAdmin)
admin.site.register(models.Empresa, EmpresaAdmin)
admin.site.register(models.Poliza, PolizaAdmin)
