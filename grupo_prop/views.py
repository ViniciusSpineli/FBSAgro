from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from .models import GrupoPropriedade

def inicio(request):
    # Pega o usuário da sessão, ou exibe 'Usuário não identificado' se não houver
    #usuario = request.session.get('usuario', 'Usuário não identificado')
    # Renderiza a página inicial passando o nome do usuário
    usuario = request.session.get('usuario', 'Visitante')
    #usuario = getattr(request, 'usuario_temp', 'Visitante')
    return render(request, 'telas/inicio.html', {'usuario': usuario})

    #return render(request, 'telas/inicio.html', {'usuario': usuario})


def listar_propriedades(request):
    # Busca todas as propriedades da tabela GrupoPropriedade usando o ORM do Django
    grupo_propriedade = GrupoPropriedade.objects.all()
    # Renderiza a página de listagem de propriedades, passando os dados obtidos
    return render(request, 'telas/lista.html', {'grupo_propriedade': grupo_propriedade})

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

        else:
            
            print('usuario ou senha invalida')
            # Caso não encontre usuário/senha, mostra uma mensagem de erro
            messages.error(request, 'Usuário ou senha inválidos.')

    # Caso a requisição seja GET (ou login falhou), renderiza a página de login
    # login.html está direto na pasta templates
    return render(request, 'login.html')




