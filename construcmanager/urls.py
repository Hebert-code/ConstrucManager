from django.urls import path
from construcmanager.views import index, cadastro_clientes, cadastro_fornecedores
from construcmanager.views import cadastro_produtos, vendas, compras, estoque, controle_vendas, nova_categoria, sucesso
urlpatterns = [
    path('', index, name='index'),
    path('cadastro_clientes', cadastro_clientes, name='cadastro_clientes'),
    path('cadastro_fornecedores/', cadastro_fornecedores, name='cadastro_fornecedores'),
    path('cadastro_produtos/', cadastro_produtos, name='cadastro_produtos'),
    path('vendas/', vendas, name='vendas'),
    path('compras/', compras, name='compras'),
    path('estoque/', estoque, name='estoque'),
    path('controle_vendas/', controle_vendas, name='controle_vendas'),
    path('nova_categoria/', nova_categoria, name='nova_categoria'),
    path('/sucesso', sucesso, name='sucesso')
]