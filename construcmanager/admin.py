from django.contrib import admin
from .models import Cliente, ProdutoFornecedor, Produto, Categoria, ProdutoCategoria, Fornecedor, TelefoneFornecedor, Vendedor, Venda, ProdutoVenda, Compra, ProdutoCompra

admin.site.register(Cliente)
admin.site.register(ProdutoFornecedor)
admin.site.register(Produto)
admin.site.register(Categoria)  # Registro do modelo Categoria
admin.site.register(ProdutoCategoria)  # Registro do modelo ProdutoCategoria
admin.site.register(Fornecedor)  # Registro do modelo Fornecedor
admin.site.register(TelefoneFornecedor)  # Registro do modelo TelefoneFornecedor
admin.site.register(Vendedor)  # Registro do modelo Vendedor
admin.site.register(Venda)  # Registro do modelo Venda
admin.site.register(ProdutoVenda)  # Registro do modelo ProdutoVenda
admin.site.register(Compra)  # Registro do modelo Compra
admin.site.register(ProdutoCompra)  # Registro do modelo ProdutoCompra
