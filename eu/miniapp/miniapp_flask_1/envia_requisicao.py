import requests

server = 'http://localhost:5000/parametro'
response = requests.post(server, json={'username': 'jose123@email.com', 'password': 'jose123'})
# retorna status de erro na requisicao levantando uma excecao
response.raise_for_status()
print(response)
print(response.status_code)
print(response.json())

suc = requests.post(server, json={'username': 'jose123@email.com',
                                   'password': 'jose123'})
aut = requests.post(server, json={
    'username': 'jose123@email.com',
    'passsword': 'jose123'})
camp = requests.post(server, json={
    'username': 'jose123@email.com',
    'password': 'jose123',
    'campoAMais': 'sla'})

print(suc, suc.status_code, suc.json())
print(aut, aut.status_code, aut.json())
print(camp, camp.status_code, camp.json())