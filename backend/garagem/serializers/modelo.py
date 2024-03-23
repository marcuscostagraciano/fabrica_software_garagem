from rest_framework.serializers import ModelSerializer

from garagem.models import Modelo


class ModelosSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"
        depth = 1
