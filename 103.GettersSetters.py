class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, porcentagem):
        self.preco = self.preco - (self.preco/100) * porcentagem

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor


p1 = Produtos('Lenço', 15)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produtos('PRENDEDOR', 'R$18')
p2.desconto(20)
print(p2.nome, p2.preco)
