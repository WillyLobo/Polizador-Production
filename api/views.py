from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets, renderers, generics
from rest_framework.renderers import TemplateHTMLRenderer

from api import serializers

from carga import models

@login_required(redirect_field_name="login")
def index(request):
	return render(request, "lista-polizas.html")

@login_required(redirect_field_name="login")
def listaempresas(request):
	return render(request, "lista-empresas.html")

@login_required(redirect_field_name="login")
def listaobras(request):
	return render(request, "lista-obras.html")

# class PolizaDetail(APIView):
# 	renderer_classes = [TemplateHTMLRenderer]
# 	template_name = "test.html"

# 	def get(self, request, pk):
# 		poliza = get_object_or_404(models.Poliza, pk=pk)
# 		serializer = serializers.PolizaAPI(poliza)
# 		return Response({"serializer":serializer, "profile":poliza})

class PolizaViewSet(LoginRequiredMixin, viewsets.ReadOnlyModelViewSet):
	login_url = "/"
	redirect_field_name = "login"

	queryset = models.Poliza.objects.all().order_by("-pk")
	serializer_class = serializers.PolizaAPI

class EmpresaViewSet(LoginRequiredMixin, viewsets.ReadOnlyModelViewSet):
	login_url = "/"
	redirect_field_name = "login"
	
	queryset = models.Empresa.objects.all().order_by("-pk")
	serializer_class = serializers.EmpresaAPI

class ObraViewSet(LoginRequiredMixin, viewsets.ReadOnlyModelViewSet):
	login_url = "/"
	redirect_field_name = "login"

	queryset = models.Obra.objects.all().order_by("-pk")
	serializer_class = serializer_class = serializers.ObraAPI
