from django import forms

class RelatorioFiltroForm(forms.Form):
    tipo = forms.ChoiceField(
        choices=[
            ('estoque', 'Estoque'),
            ('vendas', 'Vendas'),
            ('clientes', 'Clientes'),
        ],
        required=False,
        label='Tipo de Relatório'
    )
    data_inicio = forms.DateField(required=False, label='Data Início')
    data_fim = forms.DateField(required=False, label='Data Fim')
