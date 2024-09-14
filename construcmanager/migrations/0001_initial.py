# Generated by Django 5.1.1 on 2024-09-14 15:15

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_nome', models.CharField(max_length=255, unique=True, verbose_name='Nome da categoria')),
            ],
            options={
                'verbose_name': 'Categorias',
                'ordering': ['categoria_nome'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_nome', models.CharField(max_length=255, verbose_name='Nome do cliente')),
                ('cliente_apelido', models.CharField(max_length=127, verbose_name='Apelido do cliente')),
                ('cliente_cnpj', models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='CNPJ do cliente')),
                ('cliente_cpf', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='CPF do cliente')),
                ('cliente_email', models.EmailField(blank=True, max_length=320, null=True, verbose_name='Email do cliente')),
                ('endereco_numero', models.CharField(max_length=31, verbose_name='Numero do endereço')),
                ('endereco_rua', models.CharField(max_length=127, verbose_name='Rua do endereço')),
                ('endereco_bairro', models.CharField(max_length=127, verbose_name='Bairro do endereço')),
                ('endereco_cidade', models.CharField(max_length=127, verbose_name='Cidade do endereço')),
                ('endereco_estado', models.CharField(max_length=127, verbose_name='Estado do endereço')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fornecedor_nome', models.CharField(max_length=255, verbose_name='Nome do fornecedor')),
                ('fornecedor_cnpj', models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='CNPJ do fornecedor')),
                ('fornecedor_cpf', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='CPF do fornecedor')),
                ('fornecedor_email', models.EmailField(max_length=320, verbose_name='Email do fornecedor')),
                ('endereco_numero', models.CharField(max_length=31, verbose_name='Numero do endereço')),
                ('endereco_rua', models.CharField(max_length=127, verbose_name='Rua do endereço')),
                ('endereco_bairro', models.CharField(max_length=127, verbose_name='Bairro do endereço')),
                ('endereco_cidade', models.CharField(max_length=127, verbose_name='Cidade do endereço')),
                ('endereco_estado', models.CharField(max_length=127, verbose_name='Estado do endereço')),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto_nome', models.CharField(max_length=255, verbose_name='Nome do produto')),
                ('produto_marca', models.CharField(max_length=255, verbose_name='Marca do produto')),
                ('produto_preco_a_vista', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Preço a vista do produto')),
                ('produto_preco_parcelado', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Preço parcelado do produto')),
                ('produto_quantidade_em_estoque', models.PositiveIntegerField(verbose_name='Quantidade em estoque do produto')),
                ('produto_codigo', models.PositiveBigIntegerField(unique=True, verbose_name='Código do produto')),
                ('produto_ponto_reposicao', models.PositiveIntegerField(verbose_name='Ponto de reposição do produto')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['produto_nome'],
            },
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendedor_nome', models.CharField(max_length=255, verbose_name='Nome do vendedor')),
                ('vendedor_cpf', models.CharField(max_length=11, unique=True, verbose_name='CPf do vendedor')),
            ],
            options={
                'verbose_name': 'Vendedor',
                'verbose_name_plural': 'Vendedores',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compra_data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data da compra')),
                ('compra_valor_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=18, verbose_name='Valor da compra')),
                ('compra_status', models.CharField(choices=[('PENDENTE', 'Pendente'), ('PAGO', 'Pago'), ('CANCELADO', 'Cancelado')], default='PENDENTE', max_length=10, verbose_name='Stats da compra')),
                ('compra_pagamento_tipo', models.CharField(choices=[('À VISTA', 'A Vista'), ('PARCELADO', 'Parcelado')], default='À VISTA', max_length=10, verbose_name='Tipo do pagamento da compra')),
                ('compra_pagamento_quantidade_parcelas', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Quantidade de parcelas do pagamento da compra')),
                ('compra_pagamanento_data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data do pagamento da compra')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construcmanager.fornecedor')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
        migrations.CreateModel(
            name='TelefoneCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=14, verbose_name='Telefone do fornecedor')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construcmanager.cliente')),
            ],
            options={
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
            },
        ),
        migrations.CreateModel(
            name='TelefoneFornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=14, verbose_name='Telefone do fornecedor')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construcmanager.fornecedor')),
            ],
            options={
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
            },
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venda_data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data da venda')),
                ('venda_valor_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=18, verbose_name='Valor total da venda')),
                ('venda_local_entrega', models.CharField(default='Sem local de entrega', max_length=511, verbose_name='Local de entrega da venda')),
                ('venda_status', models.CharField(choices=[('PENDENTE', 'Pendente'), ('PAGO', 'Pago'), ('CANCELADO', 'Cancelado')], default='PENDENTE', max_length=10, verbose_name='Status do pagamanento da venda')),
                ('venda_pagamento_tipo', models.CharField(choices=[('À VISTA', 'A Vista'), ('PARCELADO', 'Parcelado')], default='À VISTA', max_length=10, verbose_name='Tipo do pagamento da venda')),
                ('venda_pagamento_quantidade_parcelas', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Quantidade de parcelas do pagamento da venda')),
                ('venda_data_pagamento', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data do pagamento da venda')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='construcmanager.cliente')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construcmanager.vendedor')),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
            },
        ),
        migrations.CreateModel(
            name='ProdutoCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construcmanager.categoria')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construcmanager.produto')),
            ],
            options={
                'verbose_name': 'Junção entre Produto e Categoria',
                'verbose_name_plural': 'Junções entre Produto e Categoria',
                'unique_together': {('produto', 'categoria')},
            },
        ),
        migrations.CreateModel(
            name='ProdutoCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_produto', models.PositiveIntegerField(verbose_name='Quantidade do produto na venda')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construcmanager.compra')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construcmanager.produto')),
            ],
            options={
                'verbose_name': 'Junção entre produto e compra',
                'verbose_name_plural': 'Junções entre produto e compra',
                'unique_together': {('produto', 'compra')},
            },
        ),
        migrations.CreateModel(
            name='ProdutoFornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construcmanager.fornecedor')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construcmanager.produto')),
            ],
            options={
                'verbose_name': 'Junção entre produto e fornecedor',
                'verbose_name_plural': 'Junções entre produto e fornecedor',
                'unique_together': {('produto', 'fornecedor')},
            },
        ),
        migrations.CreateModel(
            name='ProdutoVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_produto', models.PositiveIntegerField(verbose_name='Quantidade do produto na venda')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construcmanager.produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construcmanager.venda')),
            ],
            options={
                'verbose_name': 'Junção entre produto e venda',
                'verbose_name_plural': 'Junções entre produto e venda',
                'unique_together': {('produto', 'venda')},
            },
        ),
    ]