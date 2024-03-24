from rest_framework.serializers import ModelSerializer

from garagem.models import Veiculo


class VeiculosSerializer(ModelSerializer):
    """Criação e Alteração de veículos"""
    class Meta:
        model = Veiculo
        fields = "__all__"


class VeiculoDetailSerializer(ModelSerializer):
    """Detalhamento de um único veículo"""
    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 1


class VeiculosListSerializer(ModelSerializer):
    """Listagem de veículos"""
    class Meta:
        model = Veiculo
        fields = ['id', 'modelo', 'ano']
