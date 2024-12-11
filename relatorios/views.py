from django.shortcuts import render
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from construcmanager.models import Produto, Venda, Fornecedor, Compra, Cliente
from .api import gerar_insights_relatorio
from .api import baixar_relatorio_com_insights 

def pagina_central_relatorios(request):
    return render(request, 'construcmanager/relatorios/central_relatorios.html')

def pagina_central_relatorios_insights(request):
    return render(request, 'construcmanager/relatorios/central_relatorios_insights.html')

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


def gerar_relatorio_com_insights_pdf(tipo_relatorio):
    """
    Gera o relatório com insights da API Gemini, ajustando para quebra de linha e tratamento de markdown.
    """
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setTitle(f"Relatório de {tipo_relatorio}")

    y = 750  # Posição inicial no PDF
    max_width = 500  # Largura máxima para o texto antes de quebrar a linha
    line_height = 15  # Altura entre linhas

    def check_page_break():
        nonlocal y
        if y < 50:  # Se estiver próximo do rodapé
            pdf.showPage()  # Cria uma nova página
            y = 750  # Reinicia a posição no topo da nova página

    def draw_wrapped_text(x, y, text, bold=False, italic=False):
        """
        Quebra o texto automaticamente se ultrapassar a largura máxima.
        """
        from reportlab.lib.utils import simpleSplit
        from reportlab.pdfgen.canvas import Canvas
        font_name = "Helvetica-Bold" if bold else "Helvetica-Oblique" if italic else "Helvetica"
        pdf.setFont(font_name, 10)
        lines = simpleSplit(text, font_name, 10, max_width)
        for line in lines:
            pdf.drawString(x, y, line)
            y -= line_height
            check_page_break()
        return y

    def sanitize_text(text):
        """
        Remove markdown como ** ou * e organiza o texto.
        """
        import re
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # Remove ** para negrito
        text = re.sub(r'\*(.*?)\*', r'\1', text)  # Remove * para itálico
        return text.strip()

    # Relatórios baseados no tipo
    pdf.drawString(100, y, f"Relatório de {tipo_relatorio}")
    y -= 20

    if tipo_relatorio == 'Produto':
        dados = Produto.objects.all()
        pdf.drawString(100, y, "Relatório de Produtos")
        y -= 20
        for produto in dados:
            y = draw_wrapped_text(
                50, y,
                f"Produto: {produto.produto_nome}, Quantidade em Estoque: {produto.produto_quantidade_em_estoque}"
            )

    # Gerar os insights usando a API Gemini
    try:
        insights = gerar_insights_relatorio(
            titulo=f"Relatório de {tipo_relatorio}",
            conteudo="Conteúdo relevante do relatório aqui"  # Substituir com dados reais para gerar insights
        )
        insights = sanitize_text(insights)  # Sanitizar texto da API
        y -= 20
        pdf.drawString(100, y, "Insights gerados:")
        y -= 20
        for linha in insights.split("\n"):
            if linha.startswith("**"):
                linha = linha.strip("**")
                y = draw_wrapped_text(50, y, linha, bold=True)
            elif linha.startswith("*"):
                linha = linha.strip("*")
                y = draw_wrapped_text(50, y, linha, italic=True)
            else:
                y = draw_wrapped_text(50, y, linha)
    except Exception as e:
        y = draw_wrapped_text(50, y, f"Erro ao gerar insights: {str(e)}")

    pdf.save()
    buffer.seek(0)
    return buffer



def baixar_relatorio_com_insights(request, tipo_relatorio):
    """
    Gera e retorna o arquivo PDF do relatório, com insights.
    """
    buffer = gerar_relatorio_com_insights_pdf(tipo_relatorio)
    response = FileResponse(buffer, as_attachment=True, filename=f'relatorio_{tipo_relatorio}_com_insights.pdf')
    return response

 # Certifique-se de ajustar o caminho de import

def view_baixar_relatorio(request, tipo_relatorio):
    """
    View para chamar a função de geração de relatório com insights.
    """
    return baixar_relatorio_com_insights(request, tipo_relatorio)