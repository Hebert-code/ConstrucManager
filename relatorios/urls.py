from django.urls import path
from .views import pagina_central_relatorios, baixar_relatorio
from .views import baixar_relatorio_com_insights, pagina_central_relatorios_insights, view_baixar_relatorio

urlpatterns = [
    path('', pagina_central_relatorios, name='central_relatorios'),
    path('baixar/<str:tipo_relatorio>/', baixar_relatorio, name='baixar_relatorio'),
    path('pagina_central_relatorios_insights/', pagina_central_relatorios_insights, name='pagina_central_relatorios_insights'),
    path('download-relatorio/<str:tipo_relatorio>/', view_baixar_relatorio, name='baixar_relatorio_com_insights'),
]
