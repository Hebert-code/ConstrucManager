from django.shortcuts import render
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from construcmanager.models import Produto, Venda, Fornecedor, Compra, Cliente

def pagina_central_relatorios(request):
    return render(request, 'construcmanager/relatorios/central_relatorios.html')

def gerar_relatorio_pdf(tipo_relatorio):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setTitle(f"Relatório de {tipo_relatorio}")

    if tipo_relatorio == 'Produto':
        dados = Produto.objects.all()
        pdf.drawString(100, 750, "Relatório de Produtos")
        y = 700
        for produto in dados:
            pdf.drawString(50, y, f"Produto: {produto.produto_nome}, Quantidade em Estoque: {produto.produto_quantidade_em_estoque}")
            y -= 20

    elif tipo_relatorio == 'Venda':
        dados = Venda.objects.all()
        pdf.drawString(100, 750, "Relatório de Vendas")
        y = 700
        for venda in dados:
            pdf.drawString(50, y, f"Cliente: {venda.cliente.cliente_nome}, Valor: {venda.venda_valor_total}, Data: {venda.venda_data}")
            y -= 20

    elif tipo_relatorio == 'Fornecedor':
        dados = Fornecedor.objects.all()
        pdf.drawString(100, 750, "Relatório de Fornecedores")
        y = 700
        for fornecedor in dados:
            pdf.drawString(50, y, f"Nome: {fornecedor.fornecedor_nome}, CNPJ: {fornecedor.fornecedor_cnpj}, Email: {fornecedor.fornecedor_email}")
            y -= 20

    elif tipo_relatorio == 'Compra':
        dados = Compra.objects.all()
        pdf.drawString(100, 750, "Relatório de Compras")
        y = 700
        for compra in dados:
            pdf.drawString(50, y, f"Produto: {compra.produto.produto_nome}, Quantidade: {compra.quantidade_produto}, Preço: {compra.produto.produto_preco_a_vista}")
            y -= 20

    elif tipo_relatorio == 'Estoque':
        dados = Produto.objects.all()
        pdf.drawString(100, 750, "Relatório de Estoque")
        y = 700
        for produto in dados:
            pdf.drawString(50, y, f"Produto: {produto.produto_nome}, Quantidade em Estoque: {produto.produto_quantidade_em_estoque}")
            y -= 20

    elif tipo_relatorio == 'Cliente':
        dados = Cliente.objects.all()
        pdf.drawString(100, 750, "Relatório de Clientes")
        y = 700
        for cliente in dados:
            pdf.drawString(50, y, f"Nome: {cliente.cliente_nome}, Apelido: {cliente.cliente_apelido},E-mail: {cliente.cliente_email}")
            y -= 20

    pdf.save()
    buffer.seek(0)
    return buffer


def baixar_relatorio(request, tipo_relatorio):
    buffer = gerar_relatorio_pdf(tipo_relatorio)
    response = FileResponse(buffer, as_attachment=True, filename=f'relatorio_{tipo_relatorio}.pdf')
    return response
