from django.urls import path

from . import views

app_name = 'enquetes'

urlpatterns = [
    path('objetos/novo/', views.index, name='cadastro_objeto'),
    path('objetos/', views.lista_objetos, name='lista_objetos'),
]
