from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/auth')
def authentication():
    return {'request.authorizarion': request.authorization, 'request.headers': dict(request.headers)}


if __name__ == '__main__':
    app.run(debug=True)
