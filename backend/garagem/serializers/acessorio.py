from rest_framework.serializers import ModelSerializer
from garagem.models import Acessorio


class AcessoriosSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"
