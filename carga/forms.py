from django import forms

from django.contrib.auth.forms import AuthenticationForm

from django_select2 import forms as s2forms

from carga import models

class LoginForm(AuthenticationForm):
	def confirm_login_allowed(self, user):
		pass

class TomadorWidget(s2forms.ModelSelect2Widget):
	search_fields = [
		"empresa_nombre__icontains"
	]

class PolizaForm(forms.ModelForm):
	CONCEPTO = (
        ("C", "Garantía de Ejecución de Contrato"),
        ("F", "Garantía de Sustitución de Fondo de Reparo"),
        ("A", "Garantía de Anticipo Financiero")
    )
	poliza_concepto = forms.ChoiceField(choices=CONCEPTO)
	poliza_fecha	= forms.DateField(input_formats=['%d/%m/%Y'], localize=True)
	
	class Meta:
		model = models.Poliza
		fields = "__all__"
		widgets = {
			"poliza_tomador" : TomadorWidget
		}

class EmpresaForm(forms.ModelForm):
	class Meta:
		model = models.Empresa
		fields = "__all__"
