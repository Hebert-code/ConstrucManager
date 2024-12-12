from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Produto, Fornecedor, Venda, Compra
from .forms import ClienteForm, ProdutoForm, FornecedorForm, VendaForm, CompraForm, ProdutoCompraForm, AtualizarEstoqueForm
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.db import transaction
from django.db.models import F
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from allauth.account.views import SignupView
from construcmanager.forms import CustomSignupForm

class CustomSignupView(SignupView):
    def get_form_class(self):
        return CustomSignupForm


@login_required
def home(request):
    return render(request, 'construcmanager/home.html')

#Clientes

@login_required
def listar_clientes(request):
    clientes_list = Cliente.objects.all()
    paginator = Paginator(clientes_list, 10) 
    page = request.GET.get('page')

    try:
        clientes = paginator.page(page)
    except PageNotAnInteger:
        clientes = paginator.page(1)
    except EmptyPage:
        clientes = paginator.page(paginator.num_pages)

    return render(request, 'construcmanager/clientes/listar.html', {'clientes': clientes})


@login_required
def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente criado com sucesso!')
            return redirect('criar_cliente')
    else:
        form = ClienteForm()
    return render(request, 'construcmanager/clientes/form.html', {'form': form})

@login_required
def atualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'construcmanager/clientes/form.html', {'form': form})

@login_required
def deletar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'construcmanager/clientes/confirmar_exclusao.html', {'cliente': cliente})

#Clientes


#Produtos

@login_required
def listar_produtos(request):
    produtos_list = Produto.objects.all()
    paginator = Paginator(produtos_list, 10) 

    page = request.GET.get('page')
    try:
        produtos = paginator.page(page)
    except PageNotAnInteger:
        produtos = paginator.page(1)
    except EmptyPage:
        produtos = paginator.page(paginator.num_pages)

    return render(request, 'construcmanager/produto/listar.html', {'produtos': produtos})

@login_required
def cadastro_produtos(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!') 
            return redirect('cadastro_produtos')
    else:
        form = ProdutoForm()
    
    produtos = Produto.objects.all()
    return render(request, 'construcmanager/produto/cadastro_produtos.html', {'form': form, 'produtos': produtos})

@login_required
def atualizar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'construcmanager/produto/editar_produto.html', {'form': form, 'produto': produto})

@login_required
def delete_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete() 
        return redirect('listar_produtos')
    return render(request, 'construcmanager/produto/excluir_produto.html', {'produto': produto})

#Produtos



#Fornecedores

@login_required
def listar_fornecedor(request):
    fornecedor_list = Fornecedor.objects.all()
    paginator = Paginator(fornecedor_list, 10)  
    page = request.GET.get('page')

    try:
        fornecedores = paginator.page(page)
    except PageNotAnInteger:
        fornecedores = paginator.page(1)
    except EmptyPage:
        fornecedores = paginator.page(paginator.num_pages)

    return render(request, 'construcmanager/fornecedor/listar_fornecedor.html', {'fornecedores': fornecedores})

@login_required
def cadastro_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fornecedor salvo com sucesso!')
            return redirect('cadastro_fornecedor')
    else:
        form = FornecedorForm()
    return render(request, 'construcmanager/fornecedor/cadastro_fornecedor.html', {'form': form})

@login_required
def atualizar_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('listar_fornecedor')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'construcmanager/fornecedor/atualizar_fornecedor.html', {'form': form, 'fornecedor': fornecedor})

@login_required
def deletar_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('listar_fornecedor')
    return render(request, 'construcmanager/fornecedor/deletar_fornecedor.html', {'fornecedor': fornecedor})

#Fornecedores



#Vendas

@login_required
def listar_vendas(request):
    vendas_list = Venda.objects.all()
    paginator = Paginator(vendas_list, 10) 
    page = request.GET.get('page')

    try:
        vendas = paginator.page(page)
    except PageNotAnInteger:
        vendas = paginator.page(1)
    except EmptyPage:
        vendas = paginator.page(paginator.num_pages)

    return render(request, 'construcmanager/vendas/listar_vendas.html', {'vendas': vendas})

@login_required
def nova_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            venda = form.save(commit=False) 
            produto = venda.produto

            if produto.quantidade >= venda.quantidade: 
                try:
                    with transaction.atomic():  
                        produto.quantidade -= venda.quantidade 
                        produto.save() 
                        venda.save() 
                    messages.success(request, 'Venda realizada com sucesso!')
                    return redirect('listar_vendas')
                except Exception as e:
                    form.add_error(None, f"Ocorreu um erro ao salvar a venda: {str(e)}")
            else:
                form.add_error('quantidade', 'Estoque insuficiente para realizar a venda.')
    else:
        form = VendaForm()
    
    return render(request, 'construcmanager/vendas/nova_venda.html', {'form': form})


@login_required
def editar_venda(request, pk): 
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        form = FornecedorForm(request.POST,instance=venda)
        if form.is_valid:
            form.save()
            return redirect('listar_vendas')
    else:
        form = VendaForm(instance=venda)
    return(request, 'construcmanager/vendas/editar_vendas.html', {'form': form})

@login_required
def deletar_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        venda.delete()
        return redirect('listar_vendas')
    return render(request, 'construcmanager/vendas/deletar_venda.html', {'venda': venda})

#Vendas


#Compras

@login_required
def listar_compras(request):
    compras_list = Compra.objects.all()
    paginator = Paginator(compras_list, 10)
    page = request.GET.get('page')

    try:
        compras = paginator.page(page)
    except PageNotAnInteger:
        compras = paginator.page(1)
    except EmptyPage:
        compras = paginator.page(paginator.num_pages)

    return render(request, 'construcmanager/compra/listar_compras.html', {'compras': compras})

@login_required
def nova_compra(request):
    ProdutoCompraFormSet = formset_factory(ProdutoCompraForm, extra=1)

    if request.method == 'POST':
        compra_form = CompraForm(request.POST)
        formset = ProdutoCompraFormSet(request.POST)

        if compra_form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic(): 
                    compra = compra_form.save()
                    for form in formset:
                        produto_compra = form.save(commit=False)
                        produto_compra.compra = compra 
                        produto_compra.save()

                    messages.success(request, "Compra realizada com sucesso!")

            except Exception as e:
                messages.error(request, f"Erro ao salvar a compra: {str(e)}")

            return redirect('listar_compras')
    else:
        compra_form = CompraForm()
        formset = ProdutoCompraFormSet()

    return render(request, 'construcmanager/compra/nova_compra.html', {
        'compra_form': compra_form,
        'formset': formset,
    })
@login_required
def detalhar_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id) 
    return render(request, 'construcmanager/compra/detalhar_compra.html', {'compra': compra})

@login_required
def cancelar_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    compra.compra_status = 'CANCELADO' 
    compra.save()
    return redirect('listar_compras') 

#Compras 

#Estoque

@login_required
def consultar_estoque(request):
    produtos_list = Produto.objects.all()
    paginator = Paginator(produtos_list, 10)
    page = request.GET.get('page')

    try:
        produtos = paginator.page(page)
    except PageNotAnInteger:
        produtos = paginator.page(1)
    except EmptyPage:
        produtos = paginator.page(paginator.num_pages)

    return render(request, 'construcmanager/estoque/consultar_estoque.html', {'produtos': produtos})

@login_required
def atualizar_estoque(request, produto_id):
    """Atualiza o estoque de um produto específico."""
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        form = AtualizarEstoqueForm(request.POST, instance=produto)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, f"Estoque do produto {produto.produto_nome} atualizado com sucesso!")
                return redirect('consultar_estoque') 
            except Exception as e:
                messages.error(request, f"Erro ao atualizar o estoque: {str(e)}")
        else:
            messages.error(request, "Erro no formulário. Verifique os dados inseridos.")
    else:
        form = AtualizarEstoqueForm(instance=produto)

    return render(request, 'construcmanager/estoque/atualizar_estoque.html', {'form': form, 'produto': produto})

@login_required
def alertas_estoque(request):
    """Exibe os produtos com estoque abaixo do ponto de reposição."""
    produtos = Produto.objects.filter(produto_quantidade_em_estoque__lt=F('produto_ponto_reposicao'))
    return render(request, 'construcmanager/estoque/alertas_estoque.html', {'produtos': produtos})

#Estoque