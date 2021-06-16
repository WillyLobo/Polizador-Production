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
	
	class Meta:
		model = models.Poliza
		fields = "__all__"
