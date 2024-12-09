from django.urls import path
from construcmanager.views import listar_clientes, criar_cliente, atualizar_cliente, deletar_cliente
from construcmanager.views import cadastro_produtos, listar_produtos, atualizar_produto, delete_produto
from construcmanager.views import listar_fornecedor, cadastro_fornecedor, atualizar_fornecedor, deletar_fornecedor
from construcmanager.views import listar_vendas, nova_venda, editar_venda, deletar_venda
from construcmanager.views import listar_compras, nova_compra, detalhar_compra, cancelar_compra
from construcmanager.views import consultar_estoque, atualizar_estoque, alertas_estoque
from construcmanager.views import home
from . import views

urlpatterns = [
    path('home/', home, name='home'),

    path('clientes/', listar_clientes, name='listar_clientes'),
    path('clientes/novo/', criar_cliente, name='criar_cliente'),
    path('clientes/editar/<int:pk>/', atualizar_cliente, name='atualizar_cliente'),
    path('clientes/deletar/<int:pk>/', deletar_cliente, name='deletar_cliente'),
    
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('produtos/novo/', cadastro_produtos, name='cadastro_produtos'),
    path('produtos/editar/<int:pk>/', atualizar_produto, name='atualizar_produto'),
    path('produtos/excluir/<int:pk>/', delete_produto, name='delete_produto'), 

    path('fornecedores/', listar_fornecedor, name='listar_fornecedor'),
    path('fornecedores/novo/', cadastro_fornecedor, name='cadastro_fornecedor'),
    path('fornecedores/editar/<int:pk>/', atualizar_fornecedor, name='atualizar_fornecedor'),
    path('fornecedores/excluir/<int:pk>/', deletar_fornecedor, name='deletar_fornecedor'),

    path('vendas/', listar_vendas, name='listar_vendas'),
    path('vendas/novo/', nova_venda, name='nova_venda'),
    path('vendas/editar/<int:venda_id>/', editar_venda, name='editar_venda'),
    path('vendas/excluir/<int:venda_id>/', deletar_venda, name='deletar_venda'),

    path('compras/', listar_compras, name='listar_compras'), 
    path('compras/novo/', nova_compra, name='nova_compra'),  
    path('compras/detalhar/<int:compra_id>/', detalhar_compra, name='detalhar_compra'),  
    path('compras/cancelar/<int:compra_id>/', cancelar_compra, name='cancelar_compra'),  

    path('estoque/', consultar_estoque, name='consultar_estoque'),
    path('estoque/atualizar/<int:produto_id>/', atualizar_estoque, name='atualizar_estoque'),
    path('estoque/alertas/', alertas_estoque, name='alertas_estoque'),

    path('relatorios/', views.pagina_relatorios, name='pagina_relatorios'),
    path('relatorios/vendas/', views.relatorio_vendas, name='relatorio_vendas'),
    path('relatorios/vendas/exportar/csv/', views.exportar_vendas_csv, name='exportar_vendas_csv'),
    path('relatorios/vendas/exportar/pdf/', views.exportar_vendas_pdf, name='exportar_vendas_pdf'),
    path('relatorios/compras/', views.relatorio_compras, name='relatorio_compras'),
    path('relatorios/compras/exportar/csv/', views.exportar_compras_csv, name='exportar_compras_csv'),
    path('relatorios/estoque/', views.relatorio_estoque, name='relatorio_estoque'),
    path('relatorios/estoque/exportar/csv/', views.exportar_estoque_csv, name='exportar_estoque_csv'),
]