from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

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

	def form_valid(self, form):
		"""
		Deja constancia del Usuario que carga la póliza en object.poliza_creador
		"""
		self.object = form.save(commit=False)
		self.object.poliza_creador = self.request.user
		self.object.poliza_editor = self.request.user
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())

class UpdatePoliza(LoginRequiredMixin, generic.UpdateView):
	login_url = "/"
	redirect_field_name = "login"

	model = models.Poliza
	template_name = "update.html"
	form_class = forms.PolizaForm
	success_url = reverse_lazy("api:polizas")

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.poliza_editor = self.request.user
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())
	
class CrearEmpresa(LoginRequiredMixin, generic.CreateView):
	login_url = "/"
	redirect_field_name = "login"

	model = models.Empresa
	template_name = "crear-empresa.html"
	form_class = forms.EmpresaForm
	success_url = reverse_lazy("api:empresas")

class UpdateEmpresa(LoginRequiredMixin, generic.UpdateView):
	login_url = "/"
	redirect_field_name = "login"

	model = models.Empresa
	template_name = "update-empresa.html"
	form_class = forms.EmpresaForm
	success_url = reverse_lazy("api:empresas")

# Import/export plugin
def export(request):
	obra_resource = ObraResource()
	dataset = obra_resource.export()
	response = HttpResponse(dataset.csv, content_type="text/csv")
	response["Content-Disposition"] = 'attachment; filename="obra.csv"'
	return response
		 

