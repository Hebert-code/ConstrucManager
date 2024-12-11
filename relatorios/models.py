from django.db import models

class Relatorio(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(
        max_length=50,
        choices=[
            ('estoque', 'Estoque'),
            ('vendas', 'Vendas'),
            ('clientes', 'Clientes'),
        ]
    )

    def __str__(self):
        return self.titulo

