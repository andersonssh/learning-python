from flask import Flask, render_template, jsonify, abort
from arq_decorador import meu_decorador
app = Flask(__name__)

@app.route('/<seila>')
@meu_decorador
def index(seila):
    return jsonify({'message': 'm'}), 203


app.run(debug=True)