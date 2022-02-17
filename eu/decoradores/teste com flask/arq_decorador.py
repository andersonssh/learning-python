from functools import wraps
from flask import abort

def meu_decorador(funcao):
    # funcao wraps guarda metadados de funcao
    @wraps(funcao)
    def envelope(*args, **kwargs):
        print('mostrando conteudo de args e kwargs')
        print(args)
        print(kwargs)
        print(kwargs['seila'])
        print('executando funcao envelopada')

        return funcao(*args, **kwargs)

    return envelope
