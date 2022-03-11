from flask import Flask
from auth import authentication_hardcoded
from http_ import validate_schema
import json

with open('schemas/post.json') as f:
    POST_SCHEMA = json.load(f)

app = Flask(__name__)


@app.route('/<teste>', methods=['POST'])
@validate_schema(POST_SCHEMA)
@authentication_hardcoded('jose123@email.com', 'jose123')
def req(teste):
    return {'status': 'success'}


if __name__ == '__main__':
    app.run(debug=True)
