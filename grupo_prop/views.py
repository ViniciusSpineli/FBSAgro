from django.shortcuts import render
from .models import GrupoPropriedade    # Importa o modelo (vamos criar já já)

def login(request):
    return render (request, 'login.html')

def index(request):
    return render(request, 'index.html')

def listar_propriedades(request):
    grupo_propriedade = GrupoPropriedade.objects.all()
    return render(request, 'produtos/lista.html', {'grupo_propriedade': grupo_propriedade})