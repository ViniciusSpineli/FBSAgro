from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),           # Tela padrão é login
    #path('login/', views.login, name='login'),  
    path('inicio/', views.inicio, name='inicio'),  # Painel após login
    path('produtos/', views.listar_propriedades, name='listar_propriedades'),
]

