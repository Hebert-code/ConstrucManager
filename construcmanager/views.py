from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto, Categoria, Fornecedor, Venda, Compra, ProdutoCategoria
from .forms import ClienteForm, ProdutoForm, CategoriaForm

def index(request):
    return render(request, 'construcmanager/index.html') 

def cadastro_produtos(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            # Save the product
            produto = form.save()

            # Create ProdutoCategoria relations
            categorias = form.cleaned_data['categorias']
            for categoria in categorias:
                ProdutoCategoria.objects.create(produto=produto, categoria=categoria)

            return redirect('sucesso')  # Replace with your success URL
    else:
        form = ProdutoForm()
    return render(request, 'construcmanager/cadastro_produtos.html', {'form': form})


def nova_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = CategoriaForm()
    
    return render(request, 'construcmanager/nova_categoria.html', {'form': form})

def cadastro_fornecedores(request):
    return render(request, 'construcmanager/cadastro_fornecedores.html') 

def cadastro_clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes') 
    else:
        form = ClienteForm()

    return render(request, 'construcmanager/cadastro_clientes.html', {'form': form})

def vendas(request):
    return render(request, 'construcmanager/vendas.html') 

def compras(request):
    return render(request, 'construcmanager/compras.html') 

def estoque(request):
    return render(request, 'construcmanager/estoque.html') 

def controle_vendas(request):
    return render(request, 'construcmanager/controle_vendas.html') 

def sucesso(request):
    return render(request, 'construcmanager/sucesso.html')