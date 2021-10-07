class Cont:
    a = 0
    def get_a(self):
        return self.a

    def set_a(self, valor):
        if valor < 0:
            return False
        else:
            self.a = valor
            return True