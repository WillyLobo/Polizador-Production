from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from carga import models

class ReceptorResource(resources.ModelResource):
	class Meta:
		model = models.Receptor

class AreaResource(resources.ModelResource):
	class Meta:
		model = models.Area

class AseguradoraResource(resources.ModelResource):
	class Meta:
		model = models.Aseguradora

class EmpresaResource(resources.ModelResource):
	class Meta:
		model = models.Empresa

class PolizaResource(resources.ModelResource):
	poliza_receptor 	= fields.Field(column_name="poliza_receptor", attribute="poliza_receptor", widget=ForeignKeyWidget(models.Receptor, 'receptor_nombre',))
	poliza_area			= fields.Field(column_name="poliza_area", attribute="poliza_area", widget=ForeignKeyWidget(models.Area, 'area_nombre',))
	poliza_aseguradora	= fields.Field(column_name="poliza_aseguradora", attribute="poliza_aseguradora", widget=ForeignKeyWidget(models.Aseguradora, 'aseguradora_nombre',))
	poliza_tomador		= fields.Field(column_name="poliza_tomador", attribute="poliza_tomador", widget=ForeignKeyWidget(models.Empresa, 'empresa_nombre',))

	class Meta:
		model = models.Poliza
		fields = (
			"id",
			"poliza_fecha",
			"poliza_expediente",
			"poliza_receptor",
			"poliza_area",
			"poliza_numero",
			"poliza_concepto",
			"poliza_anexo",
			"poliza_recibo",
			"poliza_aseguradora",
			"poliza_tomador",
			"poliza_obra_nombre", 
			"poliza_obra_convenio",
			"poliza_obra_expediente",
			"poliza_monto_pesos",
			"poliza_monto_uvi",
		)

class ProgramaResource(resources.ModelResource):
	class Meta:
		model = models.Programa

class DepartamentoResource(resources.ModelResource):
	class Meta:
		model = models.Departamento

class LocalidadResource(resources.ModelResource):
	class Meta:
		model = models.Localidad

class MunicipioResource(resources.ModelResource):
	class Meta:
		model = models.Municipio

class ObraResource(resources.ModelResource):
	class Meta:
		model = models.Obra

class AgenteResource(resources.ModelResource):
	class Meta:
		model = models.Agente

class CertificadoResource(resources.ModelResource):
	class Meta:
		model = models.Certificado