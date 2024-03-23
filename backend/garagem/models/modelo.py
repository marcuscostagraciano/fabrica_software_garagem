from django.db import models

from garagem.models import Categoria, Marca


class Modelo(models.Model):
    categoria: Categoria = models.ForeignKey(Categoria,
                                             on_delete=models.PROTECT,
                                             related_name="modelo")
    marca: Marca = models.ForeignKey(Marca, on_delete=models.PROTECT,
                                     related_name="modelo")
    nome: str = models.CharField(max_length=100)

    def __str__(self) -> str:
        return (f"{self.categoria} - {self.marca}"
                f" - {self.nome}")

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"
