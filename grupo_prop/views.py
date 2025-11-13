from django.shortcuts import render
from .models import GrupoPropriedade

def login(request):
    # Como o arquivo está em templates/login.html (sem subpasta)
    return render(request, 'login.html')

def inicio(request):
    # Aqui está dentro de templates/telas/inicio.html
    return render(request, 'telas/inicio.html')

def listar_propriedades(request):
    grupo_propriedade = GrupoPropriedade.objects.all()
    return render(request, 'telas/lista.html', {'grupo_propriedade': grupo_propriedade})
