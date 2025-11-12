from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', index),
    path('produtos/', views.listar_propriedades, name='listar_propriedades'),
]
