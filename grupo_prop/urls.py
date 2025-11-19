from django.urls import path
from . import views

##urlpatterns = [
 ##   path('', views.login, name='login'),           # Tela padrão é login
    #path('login/', views.login, name='login'),  
 ##   path('inicio/', views.inicio, name='inicio'),  # Painel após login
 ##   path('produtos/', views.listar_propriedades, name='listar_propriedades'),
##]

urlpatterns = [
    path('', views.login, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('produtos/', views.listar_propriedades, name='lista_grupo'),
    path('grupo_prop/add/', views.add_grupo, name='add_grupo'),
    path('delete-grupo/<int:grupo_id>/', views.delete_grupo, name='delete_grupo'),

]
