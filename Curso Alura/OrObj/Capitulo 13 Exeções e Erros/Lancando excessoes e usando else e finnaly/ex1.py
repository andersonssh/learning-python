# class ErroLokao(Exception):
#     def __init__(self, valor):
#         self.valor = valor
#
#     def __str__(self):
#         return repr(self.valor)
#
#
# try:
#     raise ErroLokao('Kara tu ta muuuuuito loko irmao kkkk calma parça')
# except ErroLokao as e:
#     print(e)
#
# try:
#     a = 1/1
# except:
#     print('Erro detectado mano')
# else:
#     print('Nenhum erro lokao detectado')
# finally:
#     print('Executando comando independente do resultado')
#

try:
    for i in range(10000000):
        print(i)
except KeyboardInterrupt:
    while True:
        try:
            print('HAHAHAH')
        except (KeyboardInterrupt, SystemExit, SystemError):
            print('KKKKKKKKKKK')

