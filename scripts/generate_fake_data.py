import os
import django
import sys
import random
from faker import Faker
from decimal import Decimal
from django.utils import timezone

# Adiciona a raiz do projeto ao caminho
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Define o módulo de configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

# Configura o Django
django.setup()

from construcmanager.models import Produto, Categoria, Fornecedor, Cliente, Vendedor, Compra, ProdutoCompra, ProdutoCategoria, ProdutoFornecedor, TelefoneFornecedor, TelefoneCliente, Venda, ProdutoVenda

# Inicializa o Faker
faker = Faker('pt_BR')

# Função para gerar um preço falso (a vista e parcelado)
def gerar_preco():
    preco_a_vista = Decimal(random.uniform(10.0, 1000.0)).quantize(Decimal("0.01"))
    preco_parcelado = preco_a_vista + Decimal(random.uniform(10.0, 200.0)).quantize(Decimal("0.01"))
    return preco_a_vista, preco_parcelado

# Função para gerar um CPF ou CNPJ
def gerar_cpf_ou_cnpj():
    if random.choice([True, False]):
        return faker.cpf(), None
    else:
        return None, faker.cnpj()

# Geração de dados falsos para os modelos
def gerar_dados_fakes():
    # Categorias
    categorias = []
    for _ in range(5):
        categoria = Categoria.objects.create(categoria_nome=faker.word().capitalize())
        categorias.append(categoria)
    
    # Fornecedores
    fornecedores = []
    for _ in range(10):
        cpf, cnpj = gerar_cpf_ou_cnpj()
        fornecedor = Fornecedor.objects.create(
            fornecedor_nome=faker.company(),
            fornecedor_cnpj=cnpj,
            fornecedor_cpf=cpf,
            fornecedor_email=faker.email(),
            endereco_numero=faker.building_number(),
            endereco_rua=faker.street_name(),
            endereco_bairro=faker.bairro(),
            endereco_cidade=faker.city(),
            endereco_estado=faker.state()
        )
        fornecedores.append(fornecedor)

        # Telefones do fornecedor
        for _ in range(random.randint(1, 3)):
            TelefoneFornecedor.objects.create(
                fornecedor=fornecedor,
                telefone=faker.phone_number()
            )
    
    # Produtos
    produtos = []
    for _ in range(20):
        preco_a_vista, preco_parcelado = gerar_preco()
        produto = Produto.objects.create(
            produto_nome=faker.word().capitalize(),
            produto_marca=faker.company(),
            produto_preco_a_vista=preco_a_vista,
            produto_preco_parcelado=preco_parcelado,
            produto_quantidade_em_estoque=random.randint(10, 100),
            produto_codigo=faker.random_number(digits=13, fix_len=True),
            produto_ponto_reposicao=random.randint(5, 20)
        )
        produtos.append(produto)

        # Associação produto e categoria
        for categoria in random.sample(categorias, random.randint(1, 3)):
            ProdutoCategoria.objects.create(produto=produto, categoria=categoria)

        # Associação produto e fornecedor
        for fornecedor in random.sample(fornecedores, random.randint(1, 2)):
            ProdutoFornecedor.objects.create(produto=produto, fornecedor=fornecedor)
    
    # Clientes
    clientes = []
    for _ in range(10):
        cpf, cnpj = gerar_cpf_ou_cnpj()
        cliente = Cliente.objects.create(
            cliente_nome=faker.name(),
            cliente_apelido=faker.first_name(),
            cliente_cnpj=cnpj,
            cliente_cpf=cpf,
            cliente_email=faker.email(),
            endereco_numero=faker.building_number(),
            endereco_rua=faker.street_name(),
            endereco_bairro=faker.bairro(),
            endereco_cidade=faker.city(),
            endereco_estado=faker.state()
        )
        clientes.append(cliente)

        # Telefones do cliente
        for _ in range(random.randint(1, 2)):
            TelefoneCliente.objects.create(
                cliente=cliente,
                telefone=faker.phone_number()
            )
    
    # Vendedores
    vendedores = []
    for _ in range(5):
        vendedor = Vendedor.objects.create(
            vendedor_nome=faker.name(),
            vendedor_cpf=faker.cpf()
        )
        vendedores.append(vendedor)

    # Vendas e ProdutoVenda
    for _ in range(15):
        cliente = random.choice(clientes)
        vendedor = random.choice(vendedores)
        venda = Venda.objects.create(
            cliente=cliente,
            vendedor=vendedor,
            venda_valor_total=Decimal(random.uniform(100.0, 5000.0)).quantize(Decimal("0.01")),
            venda_local_entrega=faker.address(),
            venda_pagamento_quantidade_parcelas=random.randint(1, 12),
            venda_data_pagamento=timezone.now(),
            venda_status=random.choice(['PENDENTE', 'PAGO', 'CANCELADO']),
            venda_pagamento_tipo=random.choice(['À VISTA', 'PARCELADO']),
        )

        # Adicionar produtos à venda
        for produto in random.sample(produtos, random.randint(1, 5)):
            ProdutoVenda.objects.create(
                produto=produto,
                venda=venda,
                quantidade_produto=random.randint(1, 10)
            )

    # Compras e ProdutoCompra
    for _ in range(15):
        fornecedor = random.choice(fornecedores)
        compra = Compra.objects.create(
            fornecedor=fornecedor,
            compra_valor_total=Decimal(random.uniform(100.0, 5000.0)).quantize(Decimal("0.01")),
            compra_pagamento_quantidade_parcelas=random.randint(1, 12),
            # compra_pagamanento_data=timezone.now(),
            compra_status=random.choice(['PENDENTE', 'PAGO', 'CANCELADO']),
            compra_pagamento_tipo=random.choice(['À VISTA', 'PARCELADO']),
        )

        # Adicionar produtos à compra
        for produto in random.sample(produtos, random.randint(1, 5)):
            ProdutoCompra.objects.create(
                produto=produto,
                compra=compra,
                quantidade_produto=random.randint(1, 10)
            )

# Execute the function to populate the database
gerar_dados_fakes()
