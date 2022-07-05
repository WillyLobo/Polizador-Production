from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from rest_framework.routers import DefaultRouter

from carga import views, models
from api import views as restviews

app_name = "api"

router = DefaultRouter()
router.register(r"legacy_polizas", restviews.LegacyPolizaViewSet)
router.register(r"polizas", restviews.PolizaViewset)
router.register(r"empresas", restviews.EmpresaViewSet)
router.register(r"obras", restviews.ObraViewSet)
router.register(r"certificados", restviews.CertificadoViewSet)

urlpatterns = [
	url(r"^api/", include(router.urls)),
	url("polizas/", restviews.listapolizas, name="polizas"),
	url("legacy_polizas_dt/", restviews.index, name="legacy_polizas"),
	url("empresas/", restviews.listaempresas, name="empresas"),
	url("obras/", restviews.listaobras, name="obras"),
	url("certificados/", restviews.listacertificados, name="certificados")
	#path("test/<pk>", restviews.PolizaDetail.as_view(), name="profile-detail")
]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from snippets import views

# # Crear Router y registrar los viewsets
# router = DefaultRouter()
# router.register(r"snippets", views.SnippetViewSet)
# router.register(r"user", views.UserViewSet)

# urlpatterns = [
#     path("", include(router.urls))
# ]