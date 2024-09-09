from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Produto(models.Model):
    produto_nome = models.CharField('Nome do produto', max_length=255)
    produto_marca = models.CharField('Marca do produto', max_length=255)
    produto_preco_a_vista = models.DecimalField('Preço a vista do produto', decimal_places=2, max_digits=18)
    produto_preco_parcelado = models.DecimalField('Preço parcelado do produto', decimal_places=2, max_digits=18)
    produto_quantidade_em_estoque = models.IntegerField('Quantidade em estoque do produto')
    produto_codigo = models.IntegerField('Código do produto', unique=True)
    produto_ponto_reposicao = models.IntegerField('Ponto de reposição do produto')
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['produto_nome']
        
    def __str__(self) -> str:
        return f"{self.produto_nome}"
        
        
class Categoria(models.Model):
    categoria_nome = models.CharField('Nome da categoria', max_length=255)
    
    
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
        unique_together = ('produto', 'categoria')
        
    def __str__(self):
        return f"{self.produto.produto_nome} - {self.categoria.categoria_nome}"
    

class Fornecedor(models.Model):
    fornecedor_nome = models.CharField('Nome do fornecedor', max_length=255)
    fornecedor_cnpj = models.CharField('CNPJ do fornecedor', max_length=14, blank=True, null=True)
    fornecedor_cpf = models.CharField('CPF do fornecedor', max_length=11, blank=True, null=True)
    fornecedor_email = models.EmailField('Email do fornecedor', max_length=127)
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
        
    def __str__(self) -> str:
        return f"{self.fornecedor_nome}"
    
    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        constraints = [
            models.UniqueConstraint('fornecedor_cpf', name='fornecedor_cpf_unico'),
            models.UniqueConstraint('fornecedor_cnpj', name='fornecedor_cnpj_unico')
        ]


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


class Cliente(models.Model):
    cliente_nome = models.CharField('Nome do cliente', max_length=255)
    cliente_apelido = models.CharField('Apelido do cliente', max_length=127)
    cliente_cnpj = models.CharField('CNPJ do cliente', max_length=14, blank=True, null=True)
    cliente_cpf = models.CharField('CPF do cliente', max_length=11, blank=True, null=True)
    cliente_email = models.EmailField('Email do cliente', max_length=127, blank=True, null=True)
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
        constraints = [
            models.UniqueConstraint('cliente_cpf', name='cliente_cpf_unico'),
            models.UniqueConstraint('cliente_cnpj', name='cliente_cnpj_unico')
        ]
        
class TelefoneCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    telefone = models.CharField('Telefone do fornecedor', max_length=14)
    
    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'
        
    def __str__(self) -> str:
        return f"{self.cliente.cliente_nome} - {self.telefone}"
