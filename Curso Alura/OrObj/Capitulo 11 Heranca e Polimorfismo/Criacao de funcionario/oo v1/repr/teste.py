class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Ponto({self.x}, {self.y})'

    def __repr__(self):
        return f'Ponto({self.x + 1}, {self.y + 1})'


if __name__ == '__main__':
    p1 = Ponto(1,2)
    p2 = eval(repr(p1))

    print(p1)
    print(p2)