from rest_framework.serializers import ModelSerializer

from garagem.models import Cor


class CoresSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"
