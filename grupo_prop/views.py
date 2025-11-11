from django.shortcuts import render
from .models import TabItem  # Importa o modelo (vamos criar já já)

def index(request):
    return render(request, 'index.html')

def lista_produtos(request):
    produtos = TabItem.objects.all().order_by('id_item')
    return render(request, 'produtos/lista.html', {'produtos': produtos})
