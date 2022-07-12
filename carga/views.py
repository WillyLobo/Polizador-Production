from distutils.log import Log
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from carga import models, forms

class CrearPoliza(LoginRequiredMixin, generic.CreateView):
	login_url = "/"
	redirect_field_name = "login"
	model = models.Poliza
	template_name = "crear-poliza.html"
	form_class = forms.PolizaForm
	success_url = reverse_lazy("carga:crear-poliza")

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.poliza_creador = self.request.user
		self.object.poliza_editor = self.request.user
		self.object.save()
		return super().form_valid(form)

class UpdatePoliza(LoginRequiredMixin, generic.UpdateView):
	login_url = "/"
	redirect_field_name = "login"
	model = models.Poliza
	template_name = "update-poliza.html"
	form_class = forms.PolizaForm
	success_url = reverse_lazy("api:polizas")

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.poliza_editor = self.request.user
		self.object.save()
		return super().form_valid(form)

class CrearPolizaMovimiento(LoginRequiredMixin, generic.CreateView):
	login_url = "/"
	redirect_field_name = "login"
	model = models.Poliza_Movimiento
	template_name = "crear-movimiento-poliza.html"
	form_class = forms.PolizaMovimientoForm
	success_url = reverse_lazy("api:polizas")

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.poliza_movimiento_editor = self.request.user
		self.object.save()
		return super().form_valid(form)

class UpdatePolizaMovimiento(LoginRequiredMixin, generic.UpdateView):
	login_url = "/"
	redirect_field_name = "login"
	model = models.Poliza_Movimiento
	template_name = "update-movimiento-poliza.html"
	form_class = forms.PolizaMovimientoForm
	success_url = reverse_lazy("api:polizas")

	def form_valid(self,form):
		self.object = form.save(commit=False)
		self.object.poliza_movimiento_editor = self.request.user
		self.object.save()
		return super().form_valid(form)

class EstadoPoliza(LoginRequiredMixin, generic.DetailView):
	login_url = "/"
	redirect_field_name = "login"
	model = models.Poliza
	template_name = "estado-poliza.html"

class ImprimirPolizaMovimiento(LoginRequiredMixin, generic.DetailView):
	login_url = "/"
	redirect_field_name = "login"
	model = models.Poliza_Movimiento
	template_name = "imprimir-poliza.html"

class ImprimirLegacyPoliza(LoginRequiredMixin, generic.DetailView):
	login_url = "/"
	redirect_field_name = "login"

	model 			= models.LegacyPoliza
	template_name 	= "legacy-imprimir-poliza.html"
	
class CrearLegacyPoliza(LoginRequiredMixin, generic.CreateView):
	login_url = "/"
	redirect_field_name = "login"

	model = models.LegacyPoliza
	template_name = "legacy-crear-poliza.html"
	form_class = forms.LegacyPolizaForm
	success_url = reverse_lazy("carga:legacy-crear-poliza")

	def form_valid(self, form):
		"""
		Deja constancia del Usuario que carga la póliza en object.poliza_creador
		"""
		self.object = form.save(commit=False)
		self.object.legacy_poliza_creador = self.request.user
		self.object.legacy_poliza_editor = self.request.user
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())

class UpdateLegacyPoliza(LoginRequiredMixin, generic.UpdateView):
	login_url = "/"
	redirect_field_name = "login"

	model = models.LegacyPoliza
	template_name = "legacy-update-poliza.html"
	form_class = forms.LegacyPolizaForm
	success_url = reverse_lazy("api:legacy_polizas")

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.legacy_poliza_editor = self.request.user
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

class CrearObra(LoginRequiredMixin, generic.CreateView):
	login_url = "/"
	redirect_field_name = "login"

	model = models.Obra
	template_name = "crear-obra.html"
	form_class = forms.ObraForm
	success_url = reverse_lazy("carga:crear-obra")

class UpdateObra(LoginRequiredMixin, generic.UpdateView):
	login_url = "/"
	redirect_field_name = "login"

	model = models.Obra
	template_name = "update-obra.html"
	form_class = forms.ObraForm
	success_url = reverse_lazy("api:obras")

class CrearCertificado(LoginRequiredMixin, generic.CreateView):
	login_url = "/"
	redirect_field_name = "login"

	model = models.Certificado
	template_name = "crear-certificado.html"
	form_class = forms.CertificadoForm
	success_url = reverse_lazy("carga:crear-certificado")

class UpdateCertificado(LoginRequiredMixin, generic.UpdateView):
	login_url = "/"
	redirect_field_name = "login"

	model = models.Certificado
	template_name = "update-certificado.html"
	form_class = forms.CertificadoForm
	success_url = reverse_lazy("api:certificados")

class EstadoObra(LoginRequiredMixin, generic.DetailView):
	login_url = "/"
	redirect_field_name = "login"
	model = models.Obra
	template_name = "estado-obra.html"

class CertificadoView(LoginRequiredMixin, generic.DetailView):
	login_url = "/"
	redirect_field_name = "login"
	model = models.Certificado
	template_name = "certificado.html"


# Import/export plugin
# def export(request):
# 	obra_resource = ObraResource()
# 	dataset = obra_resource.export()
# 	response = HttpResponse(dataset.csv, content_type="text/csv")
# 	response["Content-Disposition"] = 'attachment; filename="obra.csv"'
# 	return response
		 

