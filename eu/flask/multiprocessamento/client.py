import requests
import json
import threading

def func(name):
    print(f'Request para "{name}", iniciado!')
    r = requests.post('http://localhost:5000', json={'name': name})
    print(r.json())
    print(f'FIM CLIENTE {name}')



names = ['Joana', 'Joao', 'Abeilarde', 'Abelamo', 'Josef', 'Iasmim', 'Bartolomeu', 'Irineu', 'Filho']

for name in names:
    print('Iniciando request para:', name )
    threading.Thread(target=func, args=(name, )).start()
