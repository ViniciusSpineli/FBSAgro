from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from django.db.models import Max
from .models import GrupoPropriedade


def login(request):
    # Verifica se a requisição enviada pelo navegador é do tipo POST (ou seja, o usuário enviou o formulário de login)
    if request.method == 'POST':
        # Pega o valor do campo 'usuario' enviado pelo formulário HTML
        usuario = request.POST.get('usuario')
        # Pega o valor do campo 'senha' enviado pelo formulário e converte para maiúsculas
        senha = request.POST.get('senha').upper()
        
        # Se ambos os campos não foram preenchidos, envia mensagem de erro e retorna a página de login
        if not usuario and not senha: 
            messages.error(request, 'Usuario e senha não preenchido')
            return render(request, 'login.html')

        # Se o campo usuário estiver vazio, envia mensagem de erro e retorna a página de login
        if not usuario:
            messages.error(request, 'O campo usuário não pode estar vazio.')
            return render(request, 'login.html')
        
        # Se o campo senha estiver vazio, envia mensagem de erro e retorna a página de login
        if not senha:
            messages.error(request, 'O campo senha não pode estar vazio.')
            return render(request, 'login.html')

        # Abre um cursor para executar comandos SQL diretamente no banco de dados Oracle
        with connection.cursor() as cursor:
            # Executa a consulta SQL para verificar se existe um usuário com o login e senha fornecidos
            cursor.execute("""
                SELECT COD_USUARIO, DES_USUARIO
                  FROM TAB_USUARIO
                 WHERE COD_USUARIO = UPPER(:usuario)
                   AND SENHA_USUARIO = PCK_CONTROLE_ACESSO_UTIL.FUN_ENCRYPT(:senha)
            """, {'usuario': usuario, 'senha': senha})

            # Retorna a primeira linha do resultado da consulta (ou None caso não exista)
            row = cursor.fetchone()
        
        # Se a consulta encontrou um usuário válido
        if row:
            # Armazena o código do usuário na sessão para que possa ser usado em outras páginas
            request.session['usuario'] = row[0]
            #request.usuario_temp = row[0]  # Comentado: só existiria durante esta requisição
            # Retorna a página inicial já logado, passando a mesma request
            return inicio(request)  # opcionalmente poderia usar redirect('inicio')
        else:
            # Caso o login seja inválido, adiciona uma mensagem de erro para ser exibida no template
            messages.error(request, 'Usuário ou senha inválidos.')

    # Caso a requisição seja GET (ou seja, apenas acessou a página) ou login falhou
    # Renderiza a página de login normalmente
    return render(request, 'login.html')


def inicio(request):
    # Recupera o usuário logado da sessão. Se não existir, retorna 'Visitante'
    usuario = request.session.get('usuario', 'Visitante')
    # Renderiza a página inicial passando o nome do usuário como contexto para o template
    return render(request, 'telas/inicio.html', {'usuario': usuario})


def listar_propriedades(request):
    # Busca todas as propriedades da tabela GrupoPropriedade usando o ORM do Django
    grupo_propriedade = GrupoPropriedade.objects.all()
    
    # Calcula o próximo código disponível da propriedade
    # Primeiro, obtém o maior código já existente na tabela
    max_codigo = GrupoPropriedade.objects.aggregate(Max('cod_grupo_propriedade'))['cod_grupo_propriedade__max']
    # Incrementa 1 para gerar o próximo código, se não houver registros, começa com 1
    proximo_codigo = (max_codigo or 0) + 1
    
    # Prepara o contexto para enviar ao template
    context = {
        'grupo_propriedade': grupo_propriedade,  # lista de todos os grupos
        'proximo_codigo': proximo_codigo         # próximo código disponível
    }

    # Renderiza o template 'lista.html' e passa o contexto
    return render(request, 'telas/lista.html', context)

def add_grupo(request):
    if request.method == "POST":

        codigo = request.POST.get("codigo")
        descricao = request.POST.get("descricao")

        if not codigo or not descricao:
            messages.error(request, "Código e descrição são obrigatórios.")
            return redirect("inicio")   # <<< SEMPRE redirect

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO TAB_GRUPO_PROPRIEDADE (
                        COD_GRUPO_PROPRIEDADE,
                        DES_GRUPO_PROPRIEDADE
                    ) VALUES (:codigo, :descricao)
                """, {
                    "codigo": codigo,
                    "descricao": descricao
                })

            messages.success(request, "Grupo cadastrado com sucesso!")
            return redirect("inicio")

        except Exception as e:
            messages.error(request, f"Erro ao inserir grupo: {e}")
            return redirect("inicio")



