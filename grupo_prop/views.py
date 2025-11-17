from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from django.db.models import Max
from .models import GrupoPropriedade


# def modal_gp(request):
#     return render(request, 'telas/modal_gp.html')

def login(request):
    # Verifica se o método da requisição é POST (ou seja, se o formulário foi enviado)
    if request.method == 'POST':
        # Pega o valor do campo 'usuario' enviado pelo formulário
        usuario = request.POST.get('usuario')
        # Pega o valor do campo 'senha' enviado pelo formulário
        senha = request.POST.get('senha').upper()
        
        if not usuario and not senha: 
            messages.error(request, 'Usuario e senha não preenchido')
            return render(request, 'login.html')

        if not usuario:
            messages.error(request, 'O campo usuário não pode estar vazio.')
            return render(request, 'login.html')
        
        if not senha:
            messages.error(request, 'O campo senha não pode estar vazio.')
            return render(request, 'login.html')


        # Abre um cursor para executar SQL diretamente no banco de dados
        with connection.cursor() as cursor:
            # Executa uma consulta SQL para verificar se existe um usuário com o login e senha informados
            cursor.execute("""
                SELECT COD_USUARIO, DES_USUARIO
                  FROM TAB_USUARIO
                 WHERE COD_USUARIO = UPPER(:usuario)
                   AND SENHA_USUARIO = PCK_CONTROLE_ACESSO_UTIL.FUN_ENCRYPT(:senha)
            """, {'usuario': usuario, 'senha': senha})

            # Retorna a primeira linha encontrada na consulta (ou None se não existir)
            row = cursor.fetchone()
        # Verifica se a consulta retornou algum resultado (usuário válido)
        if row:
            
            request.session['usuario'] = row[0]
            #request.usuario_temp = row[0]  # só existe nesta requisição
            return inicio(request)  # passa a mesma request
            #return redirect('inicio')
        else:
            
            # Caso não encontre usuário/senha, mostra uma mensagem de erro
            messages.error(request, 'Usuário ou senha inválidos.')

    # Caso a requisição seja GET (ou login falhou), renderiza a página de login
    # login.html está direto na pasta templates
    
    return render(request, 'login.html')


def inicio(request):
    usuario = request.session.get('usuario', 'Visitante')
    return render(request, 'telas/inicio.html', {'usuario': usuario})


def listar_propriedades(request):
    # Busca todas as propriedades da tabela GrupoPropriedade usando o ORM do Django
    grupo_propriedade = GrupoPropriedade.objects.all()
    
    max_codigo = GrupoPropriedade.objects.aggregate(Max('cod_grupo_propriedade'))['cod_grupo_propriedade__max']
    proximo_codigo = (max_codigo or 0) + 1
    
    context = {
        'grupo_propriedade': grupo_propriedade,
        'proximo_codigo': proximo_codigo
    }

    return render(request, 'telas/lista.html', context)
