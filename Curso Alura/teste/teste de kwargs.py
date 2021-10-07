class a:
    def __init__(self,**kwargs):
        self.seila = None

    def run(self):
        print('Executando!!!!!!!!!')


ab = a(seila='hapa')
print(ab.seila)