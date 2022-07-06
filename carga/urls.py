from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from carga import views, models

app_name = "carga"

urlpatterns = [
	#path("imprimir/<pk>", views.ImprimirLegacyPoliza.as_view(), name="imprimir-poliza"),
	#path("update/<pk>", views.UpdateLegacyPoliza.as_view(), name="update"),
	#path("crear/poliza/", views.CrearLegacyPoliza.as_view(), name="legacy-crear-poliza"),
	path("crear/empresa/", views.CrearEmpresa.as_view(), name="crear-empresa"),
	path("crear/empresa/<pk>", views.UpdateEmpresa.as_view(), name="update-empresa"),
	path("crear/certificado/", views.CrearCertificado.as_view(), name="crear-certificado"),
	path("crear/certificado/<pk>", views.UpdateCertificado.as_view(), name="update-certificado")
]
obra_patterns = [
	path("crear/obra/", views.CrearObra.as_view(), name="crear-obra"),
	path("crear/obra/<pk>", views.UpdateObra.as_view(), name="update-obra"),
	path("crear/obra/estado/<pk>", views.EstadoObra.as_view(), name = "estado-obra"),
]
poliza_patterns = [
	path("crear/poliza/", views.CrearPoliza.as_view(), name="crear-poliza"),
	path("crear/poliza/<pk>", views.UpdatePoliza.as_view(), name="update-poliza"),
	path("crear/poliza/estado/<pk>", views.EstadoPoliza.as_view(), name="estado-poliza"),
]
movimiento_patterns = [
	path("crear/poliza/movimiento/", views.CrearPolizaMovimiento.as_view(), name="crear-poliza-movimiento"),
	path("crear/poliza/movimiento/<pk>", views.UpdatePolizaMovimiento.as_view(), name="update-poliza-movimiento"),
	path("crear/poliza/movimiento/imprimir/<pk>", views.ImprimirPolizaMovimiento.as_view(), name="imprimir-poliza-movimiento"),

]
legacy_patterns = [
	path("crear/legacy_poliza/", views.CrearLegacyPoliza.as_view(), name="legacy-crear-poliza"),
	path("legacy_imprimir/<pk>", views.ImprimirLegacyPoliza.as_view(), name="legacy-imprimir-poliza"),
	path("legacy_update/<pk>", views.UpdateLegacyPoliza.as_view(), name="legacy-update-poliza"),
]

urlpatterns += legacy_patterns
urlpatterns += poliza_patterns
urlpatterns += movimiento_patterns
urlpatterns += obra_patterns