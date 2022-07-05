from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets, renderers, generics
from rest_framework.renderers import TemplateHTMLRenderer

from api import serializers

from carga import models

@login_required(redirect_field_name="login")
def index(request):
	return render(request, "lista-legacy-polizas.html")

@login_required(redirect_field_name="login")
def listapolizas(request):
	return render(request, "lista-polizas.html")

@login_required(redirect_field_name="login")
def listaempresas(request):
	return render(request, "lista-empresas.html")

@login_required(redirect_field_name="login")
def listaobras(request):
	return render(request, "lista-obras.html")

@login_required(redirect_field_name="login")
def listacertificados(request):
	return render(request, "lista-certificados.html")

class PolizaViewset(LoginRequiredMixin, viewsets.ReadOnlyModelViewSet):
	login_url = "/"
	redirect_field_name = "login"

	queryset = models.Poliza.objects.all().order_by("-pk")
	serializer_class = serializers.PolizaAPI

# class PolizaMovimientoViewset(LoginRequiredMixin, viewsets.ReadOnlyModelViewSet):
# 	login_url = "/"
# 	redirect_field_name = "login"
# 	queryset = models.Poliza_Movimiento.objects.all().latest("id")
# 	serializer_class = serializers.PolizaMovimientoAPI
		
class LegacyPolizaViewSet(LoginRequiredMixin, viewsets.ReadOnlyModelViewSet):
	login_url = "/"
	redirect_field_name = "login"

	queryset = models.LegacyPoliza.objects.all().order_by("-pk")
	serializer_class = serializers.LegacyPolizaAPI

class EmpresaViewSet(LoginRequiredMixin, viewsets.ReadOnlyModelViewSet):
	login_url = "/"
	redirect_field_name = "login"
	
	queryset = models.Empresa.objects.all().order_by("-pk")
	serializer_class = serializers.EmpresaAPI

class ObraViewSet(LoginRequiredMixin, viewsets.ReadOnlyModelViewSet):
	login_url = "/"
	redirect_field_name = "login"

	queryset = models.Obra.objects.all().order_by("-pk")
	serializer_class = serializers.ObraAPI

class CertificadoViewSet(LoginRequiredMixin, viewsets.ReadOnlyModelViewSet):
	login_url = "/"
	redirect_field_name = "login"

	queryset = models.Certificado.objects.all().order_by("-pk")
	serializer_class = serializers.CertificadoAPI

# class PolizaDetail(APIView):
# 	renderer_classes = [TemplateHTMLRenderer]
# 	template_name = "test.html"

# 	def get(self, request, pk):
# 		poliza = get_object_or_404(models.Poliza, pk=pk)
# 		serializer = serializers.PolizaAPI(poliza)
# 		return Response({"serializer":serializer, "profile":poliza})