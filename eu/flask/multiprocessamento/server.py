from flask import Flask, request, jsonify
from time import sleep

app = Flask(__name__)

@app.route('/', methods=['POST'])
def teste():
    name = request.json['name']

    for i in range(3):
        print('loop user: ', name)
        sleep(5)

    return jsonify({'status': f'{name} finalizado!'})


if __name__ == '__main__':
    app.run()