from django.shortcuts import render, redirect, get_object_or_404

from .models import Cliente, Produto, Fornecedor, Venda, Compra
from .forms import ClienteForm, ProdutoForm, FornecedorForm, VendaForm, CompraForm, ProdutoCompraForm, AtualizarEstoqueForm
from django.contrib.auth.decorators import login_required


from django.forms import formset_factory
from django.db import transaction
from django.db.models import F

import csv
from datetime import datetime
from django.db.models import Sum
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import render_to_string

@login_required
def home(request):
    return render(request, 'construcmanager/home.html')

#Clientes

@login_required
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'construcmanager/clientes/listar.html', {'clientes': clientes})

@login_required
def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
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
    produtos = Produto.objects.all()
    return render(request, 'construcmanager/produto/listar.html', {'produtos': produtos})

@login_required
def cadastro_produtos(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
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
    fornecedor = Fornecedor.objects.all()
    return render(request, 'construcmanager/fornecedor/listar_fornecedor.html', {'fornecedores': fornecedor})

@login_required
def cadastro_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_fornecedor')
    else:
        form = FornecedorForm
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
    vendas = Venda.objects.all()
    return render(request, 'construcmanager/vendas/listar_vendas.html', {'vendas': vendas})

@login_required
def nova_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            venda = form.save(commit=False)  # Salva a venda sem enviar ao banco ainda
            produto = venda.produto  # Acessa o produto relacionado

            if produto.quantidade >= venda.quantidade:  # Verifica se há estoque suficiente
                try:
                    with transaction.atomic():  # Garante que as operações são atômicas
                        produto.quantidade -= venda.quantidade  # Atualiza o estoque
                        produto.save()  # Salva a atualização do produto
                        venda.save()  # Salva a venda no banco
                    return redirect('listar_vendas')
                except Exception as e:
                    # Captura qualquer erro durante o salvamento e adiciona ao formulário
                    form.add_error(None, f"Ocorreu um erro ao salvar a venda: {str(e)}")
            else:
                # Adiciona um erro ao formulário se o estoque for insuficiente
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
    compras = Compra.objects.all() 
    return render(request, 'construcmanager/compra/listar_compras.html', {'compras': compras})

@login_required
def nova_compra(request):
    ProdutoCompraFormSet = formset_factory(ProdutoCompraForm, extra=1)

    if request.method == 'POST':
        compra_form = CompraForm(request.POST)
        formset = ProdutoCompraFormSet(request.POST)

        if compra_form.is_valid() and formset.is_valid():
            with transaction.atomic():  # Garante consistência dos dados
                compra = compra_form.save()
                for form in formset:
                    produto_compra = form.save(commit=False)
                    produto_compra.compra = compra  # Associa o produto à compra
                    produto_compra.save()
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
    """Lista todos os produtos no estoque."""
    produtos = Produto.objects.all()
    return render(request, 'construcmanager/estoque/consultar_estoque.html', {'produtos': produtos})

@login_required
def atualizar_estoque(request, produto_id):
    """Atualiza o estoque de um produto específico."""
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = AtualizarEstoqueForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('consultar_estoque')
    else:
        form = AtualizarEstoqueForm(instance=produto)
    return render(request, 'construcmanager/estoque/atualizar_estoque.html', {'form': form, 'produto': produto})

@login_required
def alertas_estoque(request):
    """Exibe os produtos com estoque abaixo do ponto de reposição."""
    produtos = Produto.objects.filter(produto_quantidade_em_estoque__lt=F('produto_ponto_reposicao'))
    return render(request, 'construcmanager/estoque/alertas_estoque.html', {'produtos': produtos})

#Estoque

#Relatorio

# Página central de relatórios
@login_required
def pagina_relatorios(request):
    return render(request, 'construcmanager/relatorios/pagina_relatorios.html')

# Relatório de Vendas
@login_required
def relatorio_vendas(request):
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    vendas = Venda.objects.all()

    if data_inicial and data_final:
        vendas = vendas.filter(data__range=[data_inicial, data_final])
    
    total_vendas = vendas.aggregate(Sum('valor_total'))['valor_total__sum'] or 0

    return render(request, 'construcmanager/relatorios/relatorio_vendas.html', {
        'vendas': vendas,
        'total_vendas': total_vendas,
        'data_inicial': data_inicial,
        'data_final': data_final,
    })

@login_required
def exportar_vendas_csv(request):
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    vendas = Venda.objects.all()

    if data_inicial and data_final:
        vendas = vendas.filter(data__range=[data_inicial, data_final])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="vendas.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Cliente', 'Data', 'Valor Total'])
    for venda in vendas:
        writer.writerow([venda.id, venda.cliente, venda.data, venda.valor_total])

    return response

@login_required
def exportar_vendas_pdf(request):
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    vendas = Venda.objects.all()

    if data_inicial and data_final:
        vendas = vendas.filter(data__range=[data_inicial, data_final])

    context = {'vendas': vendas, 'data_inicial': data_inicial, 'data_final': data_final}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="vendas.pdf"'
    html = render_to_string('construcmanager/relatorios/relatorio_vendas_pdf.html', context)
    pisa.CreatePDF(html, dest=response)
    return response

# Relatório de Compras
@login_required
def relatorio_compras(request):
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    compras = Compra.objects.all()

    if data_inicial and data_final:
        compras = compras.filter(data__range=[data_inicial, data_final])

    total_compras = compras.aggregate(Sum('valor_total'))['valor_total__sum'] or 0

    return render(request, 'construcmanager/relatorios/relatorio_compras.html', {
        'compras': compras,
        'total_compras': total_compras,
        'data_inicial': data_inicial,
        'data_final': data_final,
    })

@login_required
def exportar_compras_csv(request):
    compras = Compra.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="compras.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Fornecedor', 'Data', 'Valor Total'])
    for compra in compras:
        writer.writerow([compra.id, compra.fornecedor, compra.data, compra.valor_total])

    return response

# Relatório de Estoque
@login_required
def relatorio_estoque(request):
    produtos = Produto.objects.all()
    return render(request, 'construcmanager/relatorios/relatorio_estoque.html', {'produtos': produtos})

@login_required
def exportar_estoque_csv(request):
    produtos = Produto.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="estoque.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Nome', 'Quantidade', 'Preço'])
    for produto in produtos:
        writer.writerow([produto.id, produto.nome, produto.quantidade, produto.preco])

    return response

#Relatorio