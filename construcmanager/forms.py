from django import forms
from .models import Produto, Categoria, Fornecedor, Cliente, Venda, Compra, ProdutoVenda, ProdutoCompra, Vendedor

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
        if cnpj and len(cnpj) != 14:  # Somente validação se o CNPJ for informado
            raise forms.ValidationError('O CNPJ deve ter 14 caracteres.')
        return cnpj

    def clean_cliente_cpf(self):
        cpf = self.cleaned_data.get('cliente_cpf')
        if cpf and len(cpf) != 11:  # Somente validação se o CPF for informado
            raise forms.ValidationError('O CPF deve ter 11 caracteres.')
        return cpf
    

class ProdutoForm(forms.ModelForm):
    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False,
        label='Categorias'
    )

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
        fields = ['categoria_nome']  # Adjust fields as per your Categoria model
        widgets = {
            'categoria_nome': forms.TextInput(attrs={'class': 'form-control'}),
        }