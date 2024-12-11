from django.urls import path
from .views import pagina_central_relatorios, baixar_relatorio

urlpatterns = [
    path('', pagina_central_relatorios, name='central_relatorios'),
    path('baixar/<str:tipo_relatorio>/', baixar_relatorio, name='baixar_relatorio'),
]
