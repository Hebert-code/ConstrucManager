from django import forms
from .models import Produto, Categoria, Fornecedor, Cliente, Venda, Compra, ProdutoVenda, ProdutoCompra, Vendedor

from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        user.email = self.cleaned_data['email']
        user.save()
        return user

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'cliente_nome',
            'cliente_apelido',
            'cliente_cnpj',
            'cliente_cpf',
            'cliente_email',
            'endereco_numero',
            'endereco_rua',
            'endereco_bairro',
            'endereco_cidade',
            'endereco_estado',
        ]
        widgets = {
            'cliente_nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Cliente'}),
            'cliente_apelido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apelido do Cliente'}),
            'cliente_cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CNPJ do Cliente'}),
            'cliente_cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF do Cliente'}),
            'cliente_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email do Cliente'}),
            'endereco_numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número do Endereço'}),
            'endereco_rua': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rua do Endereço'}),
            'endereco_bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro do Endereço'}),
            'endereco_cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade do Endereço'}),
            'endereco_estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado do Endereço'}),
        }

    def clean_cliente_cnpj(self):
        cnpj = self.cleaned_data.get('cliente_cnpj')
        if cnpj and len(cnpj) != 14:  
            raise forms.ValidationError('O CNPJ deve ter 14 caracteres.')
        return cnpj

    def clean_cliente_cpf(self):
        cpf = self.cleaned_data.get('cliente_cpf')
        if cpf and len(cpf) != 11:
            raise forms.ValidationError('O CPF deve ter 11 caracteres.')
        return cpf
    

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'produto_nome',
            'produto_marca',
            'produto_preco_a_vista',
            'produto_preco_parcelado',
            'produto_quantidade_em_estoque',
            'produto_codigo',
            'produto_ponto_reposicao'
        ]
        widgets = {
            'produto_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'produto_marca': forms.TextInput(attrs={'class': 'form-control'}),
            'produto_preco_a_vista': forms.NumberInput(attrs={'class': 'form-control'}),
            'produto_preco_parcelado': forms.NumberInput(attrs={'class': 'form-control'}),
            'produto_quantidade_em_estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'produto_codigo': forms.NumberInput(attrs={'class': 'form-control'}),
            'produto_ponto_reposicao': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria_nome']
        widgets = {
            'categoria_nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Categoria'}),
        }

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = [
            'fornecedor_nome',
            'fornecedor_cnpj',
            'fornecedor_cpf',
            'fornecedor_email',
            'endereco_numero',
            'endereco_rua',
            'endereco_bairro',
            'endereco_cidade',
            'endereco_estado',
        ]
        widgets = {
            'fornecedor_nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Fornecedor'}),
            'fornecedor_cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CNPJ'}),
            'fornecedor_cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}),
            'fornecedor_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'endereco_numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número'}),
            'endereco_rua': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rua'}),
            'endereco_bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
            'endereco_cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'endereco_estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        cnpj = cleaned_data.get('fornecedor_cnpj')
        cpf = cleaned_data.get('fornecedor_cpf')
        if not cnpj and not cpf:
            raise forms.ValidationError("Informe pelo menos o CNPJ ou o CPF.")
        if cnpj and cpf:
            raise forms.ValidationError("Informe apenas o CNPJ ou o CPF, não ambos.")
        return cleaned_data

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = [
            'vendedor_nome',
            'vendedor_cpf',
        ]
        widgets = {
            'vendedor_nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Vendedor'}),
            'vendedor_cpf' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}),
        }

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = [
            'cliente',
            'vendedor',
            'venda_data',
            'venda_valor_total',
            'venda_local_entrega',
            'venda_status',
            'venda_pagamento_tipo',
            'venda_pagamento_quantidade_parcelas',
            'venda_data_pagamento',
        ]
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'vendedor': forms.Select(attrs={'class': 'form-control'}),
            'venda_data': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'venda_valor_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'venda_local_entrega': forms.TextInput(attrs={'class': 'form-control'}),
            'venda_status': forms.Select(attrs={'class': 'form-control'}),
            'venda_pagamento_tipo': forms.Select(attrs={'class': 'form-control'}),
            'venda_pagamento_quantidade_parcelas': forms.NumberInput(attrs={'class': 'form-control'}),
            'venda_data_pagamento': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

class ProdutoVenda(forms.ModelForm):
    class Meta:
        model = ProdutoVenda
        fields = [
            'produto',
            'venda',
            'quantidade_produto',
        ]
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'venda': forms.Select(attrs={'class': 'form-control'}),
            'quantidade_produto': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ProdutoCompraForm(forms.ModelForm):
    class Meta:
        model = ProdutoCompra
        fields = [
            'produto',
            'compra',
            'quantidade_produto',
        ]
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'compra': forms.Select(attrs={'class': 'form-control'}),
            'quantidade_produto': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        produto_compra = super().save(commit=False)
        produto = produto_compra.produto
        quantidade = produto_compra.quantidade_produto

        # Atualiza o estoque do produto
        produto.produto_estoque += quantidade
        produto.save()

        if commit:
            produto_compra.save()
        return produto_compra


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = [
            'fornecedor',
            'compra_data',
            'compra_valor_total',
            'compra_status',
            'compra_pagamento_tipo',
            'compra_pagamento_quantidade_parcelas',
            'compra_pagamento_data', 
        ]
        widgets = {
            'fornecedor': forms.Select(attrs={'class': 'form-control'}),
            'compra_data': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'compra_valor_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'compra_status': forms.Select(attrs={'class': 'form-control'}),
            'compra_pagamento_tipo': forms.Select(attrs={'class': 'form-control'}),
            'compra_pagamento_quantidade_parcelas': forms.NumberInput(attrs={'class': 'form-control'}),
            'compra_pagamento_data': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

class AtualizarEstoqueForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['produto_nome', 'produto_quantidade_em_estoque']
        widgets = {
            'produto_nome': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'produto_quantidade_em_estoque': forms.NumberInput(attrs={'class': 'form-control'}),
        }