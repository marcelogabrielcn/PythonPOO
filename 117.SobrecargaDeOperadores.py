class Retangulo:
    pass

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)


r1 = Retangulo(20, 20)
r2 = Retangulo(10, 10)

print(r1 + r2)
