from flask import Flask, jsonify, abort, request
import logging

logger = logging.getLogger(__name__)
app = Flask(__name__)
"""
USANDO REQUEST DENTRO DE FUNCAO
"""
def exibir(funcao):
    def decorador(funcao):
        def funcao_decorada(*args, **kwargs):
            rota = request.path
            variavel = 'variavel hehe'
            metodo = request.method
            print(f'ROTA: {rota}\nVALOR DA VARIAVEL: {variavel}\nMETODO: {metodo}')
            return funcao(*args, **kwargs)
        return funcao_decorada
    return decorador

@app.route('/<string:teste>')
def index(teste):
    return jsonify({'message': teste}), 404


app.run(debug=True)