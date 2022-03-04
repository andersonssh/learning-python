def argss(*arg):
    for i in arg:
        print(i, end=' ')
    print('')


argss('sss', 1, 2, 3333 ,34,32, 23, 23, 32, 23)


kwa	=	{'arg3':	3,	'arg2':	'dois',	'arg1':	'um'}

def k(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print(k, v)

k(ar='seila', kk = 12) #chave valor