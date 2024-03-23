from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from garagem.views import (AcessorioViewSet,
                           CategoriaViewSet)

router = DefaultRouter()
router.register(r"acessorios", AcessorioViewSet)
router.register(r"categorias", CategoriaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
