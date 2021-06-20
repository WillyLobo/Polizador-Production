from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from carga import models, forms

class Imprimir(LoginRequiredMixin, generic.DetailView):
	login_url = "/"
	redirect_field_name = "login"

	model 			= models.Poliza
	template_name 	= "imprimir.html"

class Listado(LoginRequiredMixin, generic.ListView):
	login_url = "/"
	redirect_field_name = "login"

	model 			= models.Poliza
	template_name 	= "lista.html"

class CrearPoliza(LoginRequiredMixin, generic.CreateView):
	login_url = "/"
	redirect_field_name = "login"

	model = models.Poliza
	template_name = "crear.html"
	form_class = forms.PolizaForm
	success_url = reverse_lazy("carga:crear-poliza")

class DetallePoliza(LoginRequiredMixin, generic.UpdateView):
	login_url = "/"
	redirect_field_name = "login"

	model = models.Poliza
	template_name = "crear.html"
	form_class = forms.PolizaForm
	success_url = reverse_lazy("api:polizas")
class CrearEmpresa(LoginRequiredMixin, generic.CreateView):
	login_url = "/"
	redirect_field_name = "login"

	model = models.Empresa
	template_name = "crear-empresa.html"
	form_class = forms.EmpresaForm
	success_url = reverse_lazy("carga:crear-empresa")

class UpdateEmpresa(LoginRequiredMixin, generic.UpdateView):
	login_url = "/"
	redirect_field_name = "login"

	model = models.Empresa
	template_name = "crear-empresa.html"
	form_class = forms.EmpresaForm
	success_url = reverse_lazy("api:polizas")

# Import/export plugin
def export(request):
	obra_resource = ObraResource()
	dataset = obra_resource.export()
	response = HttpResponse(dataset.csv, content_type="text/csv")
	response["Content-Disposition"] = 'attachment; filename="obra.csv"'
	return response
		 

