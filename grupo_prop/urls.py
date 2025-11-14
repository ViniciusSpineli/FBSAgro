from django.urls import path
from . import views

#URLS do APP

urlpatterns = [
    path('', views.login, name='home'),            # http://127.0.0.1:8000/
    path('login/', views.login, name='login'),     # http://127.0.0.1:8000/login/
    path('inicio/', views.inicio, name='inicio'),  # http://127.0.0.1:8000/inicio/
    path('produtos/', views.listar_propriedades, name='listar_propriedades'),
]
