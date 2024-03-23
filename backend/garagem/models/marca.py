from django.db import models


class Marca(models.Model):
    nome: str = models.CharField(max_length=50)
    nacionalidade: str = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nome.upper()}"
