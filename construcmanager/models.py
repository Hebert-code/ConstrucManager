from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.

class PagamentoTipo(models.TextChoices):
    A_VISTA ='À VISTA'
    PARCELADO = 'PARCELADO'
    
class StatusTransacao(models.TextChoices):
        PENDENTE = 'PENDENTE'
        PAGO = 'PAGO'
        CANCELADO = 'CANCELADO'

class Produto(models.Model):
    produto_nome = models.CharField('Nome do produto', max_length=255)
    produto_marca = models.CharField('Marca do produto', max_length=255)
    produto_preco_a_vista = models.DecimalField('Preço a vista do produto', decimal_places=2, max_digits=18)
    produto_preco_parcelado = models.DecimalField('Preço parcelado do produto', decimal_places=2, max_digits=18)
    produto_quantidade_em_estoque = models.PositiveIntegerField('Quantidade em estoque do produto')
    produto_codigo = models.PositiveBigIntegerField('Código do produto', unique=True)
    produto_ponto_reposicao = models.PositiveIntegerField('Ponto de reposição do produto')
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['produto_nome']
        
    def __str__(self) -> str:
        return f"{self.produto_nome}"
        
        
class Categoria(models.Model):
    categoria_nome = models.CharField('Nome da categoria', max_length=255, unique=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name = 'Categorias'
        ordering = ['categoria_nome']
        
    def __str__(self) -> str:
        return f"Categoria: {self.categoria_nome}"
    

class ProdutoCategoria(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    class Meta: 
        verbose_name = 'Junção entre Produto e Categoria'
        verbose_name_plural = 'Junções entre Produto e Categoria'
        unique_together = ['produto', 'categoria']
        
    def __str__(self):
        return f"{self.produto.produto_nome} - {self.categoria.categoria_nome}"
    

class Fornecedor(models.Model):
    fornecedor_nome = models.CharField('Nome do fornecedor', max_length=255)
    fornecedor_cnpj = models.CharField('CNPJ do fornecedor', max_length=14, blank=True, null=True, unique=True)
    fornecedor_cpf = models.CharField('CPF do fornecedor', max_length=11, blank=True, null=True, unique=True)
    fornecedor_email = models.EmailField('Email do fornecedor', max_length=320)
    endereco_numero = models.CharField('Numero do endereço', max_length=31)
    endereco_rua = models.CharField('Rua do endereço', max_length=127)
    endereco_bairro = models.CharField('Bairro do endereço', max_length=127)
    endereco_cidade = models.CharField('Cidade do endereço', max_length=127)
    endereco_estado = models.CharField('Estado do endereço', max_length=127)
    
    def clean(self):
        if not self.fornecedor_cpf and not self.fornecedor_cnpj:
            raise ValidationError('Você deve fornecer um CPF ou um CNPJ.')
        if self.fornecedor_cpf and self.fornecedor_cnpj:
            raise ValidationError('Forneça apenas um CPF ou um CNPJ, não ambos.')
    
    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        
    def __str__(self) -> str:
        return f"{self.fornecedor_nome}"


class TelefoneFornecedor(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    telefone = models.CharField('Telefone do fornecedor', max_length=14)
    
    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'
        
    def __str__(self) -> str:
        return f"{self.fornecedor.fornecedor_nome} - {self.telefone}"


class ProdutoFornecedor(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Junção entre produto e fornecedor'
        verbose_name_plural = 'Junções entre produto e fornecedor'
        unique_together = ('produto', 'fornecedor')
    
    def __str__(self) -> str:
        return f'{self.produto.produto_nome} - {self.fornecedor.fornecedor_nome}'


class Cliente(models.Model):
    cliente_nome = models.CharField('Nome do cliente', max_length=255)
    cliente_apelido = models.CharField('Apelido do cliente', max_length=127)
    cliente_cnpj = models.CharField('CNPJ do cliente', max_length=14, blank=True, null=True, unique=True)
    cliente_cpf = models.CharField('CPF do cliente', max_length=11, blank=True, null=True, unique=True)
    cliente_email = models.EmailField('Email do cliente', max_length=320, blank=True, null=True)
    endereco_numero = models.CharField('Numero do endereço', max_length=31)
    endereco_rua = models.CharField('Rua do endereço', max_length=127)
    endereco_bairro = models.CharField('Bairro do endereço', max_length=127)
    endereco_cidade = models.CharField('Cidade do endereço', max_length=127)
    endereco_estado = models.CharField('Estado do endereço', max_length=127)
    
    def clean(self):
        if not self.cliente_cpf and not self.cliente_cnpj:
            raise ValidationError('Você deve fornecer um CPF ou um CNPJ.')
        if self.cliente_cpf and self.cliente_cnpj:
            raise ValidationError('Forneça apenas um CPF ou um CNPJ, não ambos.')
        
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self) -> str:
        return f'{self.cliente_nome}'
        
class TelefoneCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    telefone = models.CharField('Telefone do fornecedor', max_length=14)
    
    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'
        
    def __str__(self) -> str:
        return f"{self.cliente.cliente_nome} - {self.telefone}"

class Vendedor(models.Model):
    vendedor_nome = models.CharField('Nome do vendedor', max_length=255)
    vendedor_cpf = models.CharField('CPf do vendedor', max_length=11, unique=True)
    
    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'
    
    def __str__(self) -> str:
        return f'{self.vendedor_nome}'

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    venda_data = models.DateTimeField('Data da venda', default=timezone.now)
    venda_valor_total = models.DecimalField('Valor total da venda', decimal_places=2, max_digits=18, default=0.0)
    venda_local_entrega = models.CharField('Local de entrega da venda', max_length=511, default='Sem local de entrega')
    venda_status = models.CharField('Status do pagamanento da venda', max_length=10, choices=StatusTransacao.choices, default=StatusTransacao.PENDENTE)
    venda_pagamento_tipo = models.CharField('Tipo do pagamento da venda', max_length=10, choices=PagamentoTipo.choices, default=PagamentoTipo.A_VISTA)
    venda_pagamento_quantidade_parcelas = models.PositiveIntegerField('Quantidade de parcelas do pagamento da venda', default=1, validators=[MinValueValidator(1)])
    venda_data_pagamento = models.DateTimeField('Data do pagamento da venda', default=timezone.now)
    
    def __str__(self) -> str:
        return f'Venda-{self.id}: {self.cliente.cliente_nome} - {self.vendedor.vendedor_nome} ({self.venda_data})'
    
    class Meta: 
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
    
class ProdutoVenda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    quantidade_produto = models.PositiveIntegerField('Quantidade do produto na venda')

    class Meta: 
        verbose_name = 'Junção entre produto e venda'
        verbose_name_plural = 'Junções entre produto e venda'
        unique_together = ['produto', 'venda']
        
    def __str__(self) -> str:
        return f'Produto: {self.produto.produto_nome} - Venda: {self.venda.id}'
    
class Compra(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    compra_data = models.DateTimeField('Data da compra', default=timezone.now)
    compra_valor_total = models.DecimalField('Valor da compra', decimal_places=2, max_digits=18, default=0.0)
    compra_status = models.CharField('Stats da compra',max_length=10, choices=StatusTransacao.choices, default=StatusTransacao.PENDENTE)
    compra_pagamento_tipo = models.CharField('Tipo do pagamento da compra', max_length=10, choices=PagamentoTipo.choices, default=PagamentoTipo.A_VISTA)
    compra_pagamento_quantidade_parcelas = models.PositiveIntegerField('Quantidade de parcelas do pagamento da compra', default=1, validators=[MinValueValidator(1)])
    compra_pagamento_data = models.DateTimeField('Data do pagamento da compra', default=timezone.now)
    
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
    
    def __str__(self) -> str:
        return f'Compra-{self.id}: {self.fornecedor.fornecedor_nome} ({self.compra_data})'
    
class ProdutoCompra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    quantidade_produto = models.PositiveIntegerField('Quantidade do produto na venda')

    class Meta: 
        verbose_name = 'Junção entre produto e compra'
        verbose_name_plural = 'Junções entre produto e compra'
        unique_together = ['produto', 'compra']
        
    def __str__(self) -> str:
        return f'Produto: {self.produto.produto_nome} - Compra: {self.compra.id}'