from django.urls import path
from .views import index, login
from . import views

urlpatterns = [
    path('', login),
    path('',index),
    path('produtos/', views.listar_propriedades, name='listar_propriedades'),
]
