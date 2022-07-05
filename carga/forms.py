from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django_select2 import forms as s2forms
from carga import models
from datetime import datetime
import locale

def dateconverter(value):
	locale.setlocale(locale.LC_TIME, "es_AR.UTF-8")
	value = datetime.strptime(value, "%b/%y").date()
	value = "{0:%d}-{0:%m}-{0:%Y}".format(value,"day","month","year")
	print(value)
	return value

class LoginForm(AuthenticationForm):
	def confirm_login_allowed(self, user):
		pass

class EmpresaWidget(s2forms.ModelSelect2Widget):
	search_fields = [
		"empresa_nombre__icontains"
	]

class PolizaForm(forms.ModelForm):
	CONCEPTO = (
		("C", "Garantía de Ejecución de Contrato"),
		("F", "Garantía de Sustitución de Fondo de Reparo"),
		("A", "Garantía de Anticipo Financiero")
	)
	poliza_fecha	= forms.DateField(input_formats=["%d/%m/%Y"], localize=True)
	poliza_concepto = forms.ChoiceField(choices=CONCEPTO)
	
	class Meta:
		model = models.Poliza
		fields = "__all__"
		widgets = {
			"poliza_tomador" : EmpresaWidget
		}
		
class LegacyPolizaForm(forms.ModelForm):
	CONCEPTO = (
        ("C", "Garantía de Ejecución de Contrato"),
        ("F", "Garantía de Sustitución de Fondo de Reparo"),
        ("A", "Garantía de Anticipo Financiero")
    )
	legacy_poliza_concepto = forms.ChoiceField(choices=CONCEPTO)
	legacy_poliza_fecha	= forms.DateField(input_formats=['%d/%m/%Y'], localize=True)
	
	class Meta:
		model = models.LegacyPoliza
		fields = "__all__"
		widgets = {
			"legacy_poliza_tomador" : EmpresaWidget
		}

class EmpresaForm(forms.ModelForm):
	class Meta:
		model = models.Empresa
		fields = "__all__"

class ObraForm(forms.ModelForm):
	class Meta:
		model = models.Obra
		fields = "__all__"
		widgets = {
			"obra_empresa" : EmpresaWidget
		}

class CertificadoForm(forms.ModelForm):
	class Meta:
		model = models.Certificado
		fields = "__all__"

class PolizaMovimientoForm(forms.ModelForm):
	class Meta:
		model = models.Poliza_Movimiento
		fields = "__all__"