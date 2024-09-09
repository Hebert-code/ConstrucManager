from django.urls import path
from construcmanager.views import index

urlpatterns = [
    path('', index, name='index')
]