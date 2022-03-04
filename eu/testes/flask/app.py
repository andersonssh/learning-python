from flask import Flask
from auth import authentication_hardcoded

app = Flask(__name__)

@app.route('/')
@authentication_hardcoded('jozenildson@gmail.com', 'senha123')
def req():
    return {'status': 'success'}

if __name__ == '__main__':
    app.run(debug=True)
