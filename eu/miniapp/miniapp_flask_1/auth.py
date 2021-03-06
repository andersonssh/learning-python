from functools import wraps
from types import FunctionType
from flask import abort, request

def authentication_hardcoded(username, password) -> FunctionType:
    """ Verifica se a o usuario e senha corresponde ao que foi colocado como parametros no decorator
    da rota

    Returns:
        function
    """
    def wrapper(func: FunctionType) -> FunctionType:
        @wraps(func)
        def decorated(*args, **kwargs):
            requisition_username = request.json['username']
            requisiton_password = request.json['password']
            print('args: ', args)
            print('kwargs: ', kwargs)

            if requisition_username != username or requisiton_password != requisiton_password:
                abort(401)
            return func(*args, **kwargs)
        return decorated
    return wrapper
