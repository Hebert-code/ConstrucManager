import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import google.generativeai as genai
from dotenv import load_dotenv
import os
from construcmanager.models import Produto, Venda, Fornecedor, Compra, Cliente  # Certifique-se de que os modelos estão importados corretamente

# Configuração da API Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 1000,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
]

def gerar_insights_relatorio(titulo, conteudo):
    """
    Gera insights a partir do título e conteúdo de um relatório.
    """
    prompt = f"""
    Você é um assistente de análise de dados especializado. Sua tarefa é gerar insights a partir dos dados fornecidos no relatório.

    Título do Relatório: {titulo}
    Conteúdo do Relatório:
    {conteudo}

    Forneça um resumo do relatório e identifique possíveis tendências, padrões e recomendações baseados nos dados fornecidos.
    """

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(
            {"parts": [{"text": prompt}], "role": "user"},
            generation_config=generation_config,
            safety_settings=safety_settings,
        )
        return response.text
    except Exception as e:
        raise RuntimeError(f"Erro ao gerar insights: {e}")

def gerar_relatorio_com_insights_pdf(tipo_relatorio):
    """
    Gera o relatório com insights da API Gemini.
    """
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setTitle(f"Relatório de {tipo_relatorio}")

    y = 700  # Posição inicial no PDF

    # Mapear tipo de relatório para dados correspondentes
    tipo_dados = {
        "Produto": Produto.objects.all(),
        "Venda": Venda.objects.all(),
        "Fornecedor": Fornecedor.objects.all(),
        "Compra": Compra.objects.all(),
        "Estoque": Produto.objects.all(),
        "Cliente": Cliente.objects.all(),
    }

    if tipo_relatorio in tipo_dados:
        dados = tipo_dados[tipo_relatorio]
        pdf.drawString(100, y, f"Relatório de {tipo_relatorio}")
        y -= 20
        for item in dados:
            if tipo_relatorio == "Produto" or tipo_relatorio == "Estoque":
                pdf.drawString(50, y, f"Produto: {item.produto_nome}, Quantidade em Estoque: {item.produto_quantidade_em_estoque}")
            elif tipo_relatorio == "Venda":
                pdf.drawString(50, y, f"Cliente: {item.cliente.cliente_nome}, Valor: {item.venda_valor_total}, Data: {item.venda_data}")
            elif tipo_relatorio == "Fornecedor":
                pdf.drawString(50, y, f"Nome: {item.fornecedor_nome}, CNPJ: {item.fornecedor_cnpj}, Email: {item.fornecedor_email}")
            elif tipo_relatorio == "Compra":
                pdf.drawString(50, y, f"Produto: {item.produto.produto_nome}, Quantidade: {item.quantidade_produto}, Preço: {item.produto.produto_preco_a_vista}")
            elif tipo_relatorio == "Cliente":
                pdf.drawString(50, y, f"Nome: {item.cliente_nome}, Apelido: {item.cliente_apelido}, E-mail: {item.cliente_email}")
            y -= 20

    # Gerar os insights usando a API Gemini
    try:
        conteudo_relatorio = f"Dados de {tipo_relatorio}: {len(dados)} registros encontrados."
        insights = gerar_insights_relatorio(f"Relatório de {tipo_relatorio}", conteudo_relatorio)

        y -= 20
        pdf.drawString(100, y, "Insights gerados:")
        y -= 20
        for linha in insights.split("\n"):
            pdf.drawString(50, y, linha)
            y -= 20
    except Exception as e:
        pdf.drawString(50, y, f"Erro ao gerar insights: {str(e)}")

    pdf.save()
    buffer.seek(0)
    return buffer

def baixar_relatorio_com_insights(request, tipo_relatorio):
    """
    Gera e retorna o arquivo PDF do relatório, com insights.
    """
    try:
        buffer = gerar_relatorio_com_insights_pdf(tipo_relatorio)
        return FileResponse(buffer, as_attachment=True, filename=f"relatorio_{tipo_relatorio}_com_insights.pdf")
    except Exception as e:
        return FileResponse(io.BytesIO(f"Erro ao gerar o relatório: {e}".encode()), as_attachment=True, filename="erro_relatorio.pdf")
    