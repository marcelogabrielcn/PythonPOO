class Pessoas:
    def __init__(self):
        self.atributo = '_ValorInicial'

    @property
    def nome(self):
        return 'Marcelo Gabriel'
    # return self.atributo

    @nome.setter
    def nome(self, nome):
        self.atributo = nome


p1 = Pessoas()
p1.nome = 'Binho'
print(p1.atributo)
print(p1.nome)
