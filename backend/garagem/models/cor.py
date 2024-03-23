from django.db import models


class Cor(models.Model):
    descricao: str = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.descricao}"

    class Meta:
        verbose_name = "Cor"
        verbose_name_plural = "Cores"
