from rest_framework.viewsets import ModelViewSet

from garagem.models import Modelo
from garagem.serializers import ModelosSerializer


class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModelosSerializer
