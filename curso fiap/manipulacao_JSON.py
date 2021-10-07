import json
import os
import sys
# inventario={}
# opcao=int(input("Digite: <1> para registrar ativo<2> para exibir ativos armazenados: "))
# while opcao>0 and opcao<3:
#     if opcao==1:
#         resp = "S"
#         while resp == "S":
#             inventario[input("Digite o número patrimonial: ")] = [
#                 input("Digite a data da última atualização: "),
#                 input("Digite a descrição: "),
#                 input("Digite o departamento: ")]
#             resp = input("Digite <S> para continuar.").upper()
#         with open("inventario_json.json", "w") as arq_json:
#             json.dump(inventario, arq_json)
#         print("JSON gerado!!!!")
#     elif opcao==2:
#             with open("inventario_json.json", "r") as arq_json:
#              resultado = json.load(arq_json)
#              for chave, dado in resultado.items():
#                     print("Data.........: ", dado[0])
#                     print("Descrição....: ", dado[1])
#                     print("Departamento.: ", dado[2])
#     opcao = int(input("Digite: <1> para registrar ativo<2> para exibir ativos armazenados: "))
# a = 1
# print(a, type(a), sys.getsizeof(a))
# a = 'a'
# print(a, type(a), sys.getsizeof(a))
# a = 'aa'
# print(a, type(a), sys.getsizeof(a))
# a = 'aasddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
# print(a, type(a), sys.getsizeof(a))

print(sys.getsizeof(1))
b = 12
print(sys.getsizeof(b))

if not os.path.exists('inventario_json.json'):
    print('Criando iventario_json.json')
    with open('inventario_json.json', 'w') as l:
        json.dump({}, l)

with open('inventario_json.json', 'r') as js:
    dic = json.load(js)
print('dic: ', sys.getsizeof(dic))
# for i in range(200000):
#     if str(i) not in dic:
#         dic[str(i)] = []
#     dic[str(i)].append('k')

with open('inventario_json.json', 'w') as js:
    json.dump(dic, js)
