from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', index),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
]
