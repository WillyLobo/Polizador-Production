from rest_framework import serializers

from carga import models

class ReceptorAPI(serializers.ModelSerializer):
	class Meta:
		model = models.Receptor
		fields = "__all__"

class AreaAPI(serializers.ModelSerializer):
	class Meta:
		model = models.Area
		fields = "__all__"

class AseguradoraAPI(serializers.ModelSerializer):
	class Meta:
		model = models.Aseguradora
		fields = "__all__"

class EmpresaAPI(serializers.ModelSerializer):
	class Meta:
		model = models.Empresa
		fields = "__all__"

class PolizaAPI(serializers.ModelSerializer):
	my_absolute_url			= serializers.URLField(source="get_absolute_url", read_only=True)
	poliza_fecha			= serializers.DateField(format="%d-%m-%Y", input_formats=None)
	poliza_receptor         = ReceptorAPI()
	poliza_area             = AreaAPI()
	poliza_aseguradora      = AseguradoraAPI()
	poliza_tomador          = EmpresaAPI()
	poliza_monto_pesos		= serializers.DecimalField(max_digits=12, decimal_places=2, localize=True)
	poliza_monto_uvi		= serializers.DecimalField(max_digits=12, decimal_places=2, localize=True)
	poliza_concepto			= serializers.CharField(source="get_poliza_concepto_display")
	poliza_creador			= serializers.StringRelatedField()
	poliza_editor			= serializers.StringRelatedField()

	class Meta:
		model = models.Poliza
		fields = "__all__"

class ProgramaAPI(serializers.ModelSerializer):
	class Meta:
		model = models.Programa
		fields = "__all__"

class DepartamentoAPI(serializers.ModelSerializer):
	class Meta:
		model = models.Departamento
		fields = "__all__"

class MunicipioAPI(serializers.ModelSerializer):
	class Meta:
		model = models.Municipio
		fields = "__all__"

	municipio_departamento	= DepartamentoAPI()

class LocalidadAPI(serializers.ModelSerializer):
	class Meta:
		model = models.Localidad
		fields = "__all__"

	localidad_departamento	= DepartamentoAPI()
	localidad_municipio		= MunicipioAPI()

class ObraAPI(serializers.ModelSerializer):
	class Meta:
		model = models.Obra
		fields = "__all__"
	
	obra_empresa	= EmpresaAPI()
	obra_localidad	= LocalidadAPI()
	obra_programa	= ProgramaAPI()
	obra_licitacion_tipo = serializers.CharField(source="get_obra_licitacion_tipo_display")
	obra_inspector	= serializers.StringRelatedField(many=True)

class PrototipoAPI(serializers.ModelSerializer):
	class Meta:
		model = models.Prototipo
		fields = "__all__"
	
	prototipo_obra = ObraAPI()
	prototipo_tipo = serializers.CharField(source="get_prototipo_tipo_display")

class CertificadoAPI(serializers.ModelSerializer):
	class Meta:
		model = models.Certificado
		fields = "__all__"
	
	certificado_programa	= ProgramaAPI()
	certificado_obra		= ObraAPI()
	certificado_localidad	= LocalidadAPI()
	certificado_empresa		= EmpresaAPI()
	certificado_monto_pesos = serializers.DecimalField(max_digits=12, decimal_places=2, localize=True) 
	certificado_monto_uvi	= serializers.DecimalField(max_digits=12, decimal_places=2, localize=True)