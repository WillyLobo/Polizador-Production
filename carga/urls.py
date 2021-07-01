from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from carga import views, models

app_name = "carga"

urlpatterns = [
	# path("lista/", views.Listado.as_view(), name="poliza-lista"),
	path("imprimir/<pk>", views.Imprimir.as_view(), name="imprimir-poliza"),
	path("update/<pk>", views.UpdatePoliza.as_view(), name="update"),
	path("crear/poliza/", views.CrearPoliza.as_view(), name="crear-poliza"),
	path("crear/empresa/", views.CrearEmpresa.as_view(), name="crear-empresa"),
	path("crear/empresa/<pk>", views.UpdateEmpresa.as_view(), name="update-empresa")

]