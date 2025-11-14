# grupo_prop/context_processors.py

def usuario_logado(request):
    return {
        'usuario': request.session.get('usuario', '')
    }
