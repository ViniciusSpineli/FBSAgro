# Mock simples do módulo cgi para compatibilidade com Python 3.13
FieldStorage = object
parse_header = lambda x: (x, {})
escape = lambda s, quote=None: s
