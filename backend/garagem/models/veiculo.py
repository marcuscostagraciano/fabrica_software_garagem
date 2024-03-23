from django.db import models

from garagem.models import (Acessorio,
                            Cor,
                            Modelo)


class Veiculo(models.Model):
    cor: Cor = models.ForeignKey(Cor, on_delete=models.PROTECT,
                                 related_name="veiculos")
    modelo: Modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT,
                                       related_name="veiculos")
    acessorio: Acessorio = models.ManyToManyField(Acessorio,
                                                  related_name="veiculos")
    ano: int = models.IntegerField(null=True, default=0)
    descricao: str = models.CharField(max_length=100)
    preco: float = models.DecimalField(max_digits=10, decimal_places=2,
                                       default=0)

    def __str__(self) -> str:
        return f"{self.modelo} - {self.ano}"

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
