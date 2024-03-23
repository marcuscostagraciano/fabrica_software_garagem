from rest_framework.viewsets import ModelViewSet

from garagem.models import Marca
from garagem.serializers import MarcasSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcasSerializer
