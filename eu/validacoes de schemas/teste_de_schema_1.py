import jsonschema
import json

with open('./teste.json', 'r') as f:
    schema_req = json.load(f)

conteudo = {
    'productId': 1231,
    'productName': 'jusenildson',
    'price': 1,
    'tags': ['a'],
    'option': 'queijo',
    'dimensions': {
        'lat': '10',
        'long': 90
    }
}
# a chave "option" tem valores predefinidos
print(jsonschema.validate(instance=conteudo,
                          schema=schema_req))