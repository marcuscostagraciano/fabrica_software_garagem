from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Swagger e Redoc
from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularRedocView,
                                   SpectacularSwaggerView)

from usuario.router import router as usuario_router
from garagem.views import (AcessorioViewSet,
                           CategoriaViewSet,
                           CorViewSet,
                           MarcaViewSet,
                           ModeloViewSet,
                           VeiculoViewSet)

router = DefaultRouter()
router.register(r"acessorios", AcessorioViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"cores", CorViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"modelos", ModeloViewSet)
router.register(r"veiculos", VeiculoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("", include(usuario_router.urls)),

    # OpenAPI 3
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"),
         name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"),
         name="redoc"),
]
