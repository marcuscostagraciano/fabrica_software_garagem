from rest_framework.viewsets import ModelViewSet

from garagem.models import Veiculo
from garagem.serializers import (VeiculosSerializer,
                                 VeiculoDetailSerializer,
                                 VeiculosListSerializer)


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculosSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return VeiculosListSerializer
        if self.action == "retrive":
            return VeiculosSerializer
        return VeiculoDetailSerializer
